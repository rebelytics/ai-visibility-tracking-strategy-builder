#!/usr/bin/env python3
"""Damped revenue-weighted prompt allocation for an AI visibility prompt set.

Part of the ai-visibility-tracking-strategy-builder skill (CC BY 4.0 — Eoghan
Henn / rebelytics.com). Implements the core §9.1.2 method on any platform.

Why damping rather than a cap: pure revenue weighting lets one cluster
swallow the budget; a hard cap flattens exactly the cross-market differences
the intake established. A power transform around 0.6-0.7 compresses the
extremes while preserving order and relative difference.

Usage:
    python allocate.py revenue.json --budget 300 --damp 0.65 --floor 8 \
        --fixed "Brand & Competitive=7"

revenue.json maps cluster -> {market: revenue_share_pct}, e.g.
    {"Running Shoes": {"DE": 62.0, "FR": 38.5}, ...}
Clusters named in --fixed are excluded from the weighting and given a fixed
percentage of the budget instead.
"""
import argparse, json, sys


def allocate(shares, budget, damp=0.65, floor=8, cap=None):
    """shares: {cluster: pct}. Returns {cluster: n} summing exactly to budget."""
    w = {k: (max(v, 0.0) ** damp) for k, v in shares.items()}
    s = sum(w.values())
    if s <= 0:
        raise ValueError("all shares are zero — nothing to weight on")
    frac = {k: v / s for k, v in w.items()}

    if cap:  # optional; prefer damping alone
        for _ in range(50):
            over = {k: v for k, v in frac.items() if v > cap}
            if not over:
                break
            excess = sum(v - cap for v in over.values())
            for k in over:
                frac[k] = cap
            rest = {k: v for k, v in frac.items() if k not in over}
            rs = sum(rest.values())
            if rs <= 0:
                break
            for k in rest:
                frac[k] += excess * rest[k] / rs

    n = {k: max(floor, round(v * budget)) for k, v in frac.items()}
    # reconcile to an exact total: add to the most under-allocated cluster,
    # remove from the largest, never breaching the floor
    guard = 0
    while sum(n.values()) != budget and guard < 10000:
        guard += 1
        d = budget - sum(n.values())
        if d > 0:
            k = max(frac, key=lambda x: frac[x] * budget - n[x])
            n[k] += 1
        else:
            cand = [k for k in n if n[k] > floor]
            if not cand:
                raise ValueError("floors exceed the budget — lower the floor "
                                 "or raise the budget")
            k = max(cand, key=lambda x: n[x])
            n[k] -= 1
    return n


def main():
    p = argparse.ArgumentParser()
    p.add_argument("revenue_json")
    p.add_argument("--budget", type=int, required=True)
    p.add_argument("--damp", type=float, default=0.65)
    p.add_argument("--floor", type=int, default=8)
    p.add_argument("--cap", type=float, default=None,
                   help="optional max fraction per cluster, e.g. 0.40")
    p.add_argument("--fixed", action="append", default=[],
                   help='cluster=pct, excluded from weighting, e.g. "Brand=7"')
    a = p.parse_args()

    rev = json.load(open(a.revenue_json, encoding="utf-8"))
    markets = sorted({m for v in rev.values() for m in v})
    fixed = {}
    for f in a.fixed:
        k, _, v = f.partition("=")
        fixed[k.strip()] = float(v)

    out = {}
    for mkt in markets:
        shares = {k: v.get(mkt, 0.0) for k, v in rev.items() if k not in fixed}
        fixed_n = {k: round(a.budget * pct / 100) for k, pct in fixed.items()}
        n = allocate(shares, a.budget - sum(fixed_n.values()),
                     a.damp, a.floor, a.cap)
        n.update(fixed_n)
        out[mkt] = n

    width = max(len(k) for k in list(rev) + list(fixed)) + 2
    hdr = f"{'Cluster':{width}}" + "".join(f"{m:>8}" for m in markets)
    print(hdr)
    print("-" * len(hdr))
    for k in list(rev) + [f for f in fixed if f not in rev]:
        print(f"{k:{width}}" + "".join(f"{out[m].get(k, 0):>8}" for m in markets))
    print("-" * len(hdr))
    print(f"{'TOTAL':{width}}" + "".join(f"{sum(out[m].values()):>8}" for m in markets))
    for m in markets:
        if sum(out[m].values()) != a.budget:
            print(f"WARNING: {m} does not sum to budget", file=sys.stderr)


if __name__ == "__main__":
    main()
