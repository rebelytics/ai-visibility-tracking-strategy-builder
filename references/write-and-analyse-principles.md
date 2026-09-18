# Write and Analyse — platform-agnostic principles (§12, §13)

Part of the **ai-visibility-tracking-strategy-builder** skill (CC BY 4.0 — Eoghan Henn / [rebelytics.com](https://rebelytics.com)). Section numbers are global across the skill family — the section map in `SKILL.md` says where each § lives; platform companions extend some sections with their own "Peec implementation" / "Sistrix implementation" parts.

**Load trigger:** Read before the first Write of a loop and at the start of every Analyse step; then load the platform companion's §12 (before executing any write wave) and §13 (before pulling any report). This file holds the principles every companion relies on; the companion holds the mechanics — wave order, call patterns, field names, platform-specific analyses. Section numbers below are the source numbers; a companion's §12.x / §13.x extends the principle of the same number.

**Contents:**

- 12. Phase A — Write: principles
  - 12.1 Sign-off before writes
  - 12.5 Verification after writes
  - 12.6 Verification output
  - 12.7 Measurement window
  - 12.8 Hand-off to Analyse
- 13. Phase A — Analyse: principles
  - 13.3 Cohort separation (branded / other-brand / non-branded)
  - 13.4 Empty responses are a different state from "brand not mentioned"
  - 13.5 Per-answer share, not per-question presence
  - 13.6 Findings hand-off shape
  - 13.7 Maturity tiers (quantitative vs qualitative)
  - 13.7.1 Cross-page verification before calling a content element a weakness
  - 13.8 Qualitative chat reading is peer analysis
  - 13.10 Fanout mining is a continuous refinement signal
  - 13.16 Deferred-items queue (mandatory hand-off to next loop)

---

## 12. Phase A — Write: principles

Goal: turn the signed-off Strategy output into direct writes to the tracking
platform. No intermediate operations artefact — the Strategy sign-off (§9.8)
is the audit trail.

### 12.1 Sign-off before writes

Before executing any write:

1. **User sign-off on the Strategy output.** The sign-off artefact (§9.8)
   must be in place — whatever format it took — before any write runs.
   Capture the sign-off timestamp in the persisted intake state (§7).
2. **Freshness check.** Re-read the platform state (brands, grouping
   entities, prompts) immediately before the Write sub-phase to catch any
   drift since Intake.
3. **Count reconciliation preview.** For each entity type, predict
   `expected_final = initial − deleted + created`. Print the prediction.

Platform mechanics: see §12 in the platform companion.

### 12.5 Verification after writes

After the last wave completes:

1. **Arithmetic count reconciliation** against the Write prediction (§12.1).
   For each entity type, re-read the full platform state (paginate to
   completion — a truncated list reconciles falsely) and verify
   `actual_final == expected_final`. Mismatches signal a missed or
   duplicated write.
2. **Spot-check 5–10 random prompts** — grouping, tags and market match the
   strategy.
3. **Brand list spot-check** — new brands present with correct domains /
   aliases / detection pattern; old brands absent.
4. **Fresh aggregate report** — the post-write baseline for the next Analyse
   loop.

Platform mechanics: see §12 in the platform companion.

### 12.6 Verification output

Verification results are persisted so the next Analyse loop can reference
them. Format is agent/user choice (§3.7); the required content is: date,
project and sign-off reference; the count-reconciliation table (entity,
initial, delta predicted, delta actual, match); the prompt spot-check table
(prompt, expected vs actual grouping and tags, match); the brand-list
spot-check; the baseline report summary; anomalies and follow-ups.

If anomalies exist, link back to the specific wave and operation. A clean
reconciliation closes the Write sub-phase; a mismatch triggers a replay of
the missing operations against the recorded strategy.

Platform mechanics: see §12 in the platform companion.

### 12.7 Measurement window

Fresh prompts start collecting data within roughly 24 hours on most platforms
(the companion states the platform's own figure).

- **Default pace: daily iterations.** The next Analyse loop can run ~24 hours
  after a write, once the platform has processed the prompts. Don't introduce
  multi-day gaps unless a specific analytical need calls for it. Before 24
  hours, new prompts haven't necessarily produced responses; after, they have.
- **7–14 day windows for trend-level analyses** (SoV shifts, sentiment drift,
  baseline comparisons) — a longer window stabilises the signal and removes
  first-48-hour noise. Use them when the question requires it, not as a
  default gate on every loop.
- **Detection spot-checks and hygiene questions** need only 24 hours of
  data — they check configuration, not trends.
- Comparisons against pre-write baselines use matching window lengths (7-day
  post-write vs 7-day pre-write, not full history).

**Never test run frequency by running different populations at different
frequencies.** Where the platform lets the run frequency be chosen (the
companion says whether it does), the obvious experiment — some markets daily,
the rest weekly, then compare — answers nothing: frequency is fully confounded
with market and with prompt set, so every difference between the two groups is
equally well explained by the groups differing. The richer measurement already
contains the poorer one. **Run a representative subset at the higher frequency
for two to three weeks, then subsample it** — take one run per week and compare
the subsample against all runs — and measure how often a prompt × engine result
flips between consecutive runs. A low flip rate says the extra runs resolve
noise the deliverable smooths away; a high one says the coarser frequency would
miss real movement. The general form, worth carrying beyond frequency: a
comparison is only informative if the thing being compared is the only thing
that varies, and when the richer measurement contains the poorer one, derive
the poorer one from it rather than running it on a different population.

**After a mixed-frequency setup, the first optimisation read rests on uneven
evidence — limit changes to low-run markets to breakage only.** Whatever the
reason a set ended up on mixed frequencies, the consequence for the next
Analyse loop is that run counts differ by market, often badly: the largest
market can have a single run while the smallest has seven. Prompt-set changes
driven by that read would be reallocating the plan on one market's noise
against another's signal. So in that loop, act on the high-run markets
normally, and in the low-run markets change only what is **broken** — a prompt
that returns nothing, drifts to the wrong subject, or was authored against the
wrong market. Everything else waits until the run counts are comparable. Record
the run count per market alongside the findings so the next loop knows which
markets were held back and why.

The principle is §3.4 — calendar time is a resource; pace analyses around
signal maturity, not an arbitrary schedule. Signal maturity for most
operational questions is 24 hours, not weeks, and the skill bakes in no
30-day or 90-day cadence. But don't analyse early: a loop run before the
window has elapsed reads an empty or half-populated cohort as a finding.

Platform mechanics: see §12 in the platform companion.

### 12.8 Hand-off to Analyse

Every Write sub-phase must hand off enough state that the next Analyse loop
(§13) can resume without re-deriving context. Mechanism is agent/user choice
(§3.7); the content is required:

- **Write-wave summary:** which entities changed, counts, verification
  anomalies.
- **Earliest re-analysis date** (per §12.7 — typically tomorrow for
  operational questions, longer for trend-level analyses).
- **Pending verification items:** anything that didn't reconcile cleanly.
- **Findings file location (if used):** previous loop's output and where the
  new one will go.
- **Cohort maturity map:** for each prompt cohort, when it was written and
  how old the signal is.

With persistence (§7) this lives in the intake state or a dated handover
file; without it, in a dedicated section of the session-end handoff doc.

Platform mechanics: see §12 in the platform companion.

---

## 13. Phase A — Analyse: principles

Goal: close the loop on the Write sub-phase. Read what the platform's data
actually says, produce findings, feed them back into the next Strategy
iteration. The number and depth of analyses is not hardcoded — the agent
assesses what's needed each loop from current priorities, data maturity and
user input.

### 13.3 Cohort separation (branded / other-brand / non-branded)

Produce parallel findings sections — one per cohort. Never merge them.

- *Branded cohort:* coverage gaps (an engine that doesn't name the own brand
  even with the brand in the prompt); sentiment drift — **sentiment is read
  from this cohort**; detection failures (brand in prompt, not counted).
- *Non-branded cohort:* visibility share vs tracked competitors —
  **competitive comparison is computed on this cohort only**; gap-to-close
  progress; per-engine disparities; source-retrieval patterns.
- **Forbidden ("tautological") findings:** "brand leads on branded prompts"
  (~100% by construction); any number that aggregates branded and
  non-branded without disclosure (§3.1, §9.7).

**Computation recipe** when the platform doesn't filter cohorts natively, in
order of cleanness:

1. **Multi-valued grouping filter (preferred).** Filter the report by the
   brand-mention tag (§9.7). Survives topic restructuring.
2. **Single-valued container filter (fallback).** If all branded prompts
   live under one container, exclude it. Brittle: one branded prompt
   drifting elsewhere breaks the math silently.
3. **Arithmetic subtraction (always available).**
   `non_branded_visible = total_visible − branded_visible`;
   `non_branded_chats = total_chats − branded_chats`;
   `non_branded_visibility = non_branded_visible / non_branded_chats`. Two
   report calls. **Limit:** subtraction only ever yields two cohorts — the
   `other-brand` cohort must come from its own filtered call, or it is
   silently folded into whichever side it was taken from.

**Where the project tracks `other-brand` (§4.10, §9.7), report three lines,
not two.** The middle line answers the intermediary question — *when a
customer asks about a brand we stock, are we named as a place to buy it?* —
which is neither a tautology nor cold discovery, and often the most
actionable of the three. It never merges into the branded headline, and
folding it into `non-branded` understates that cohort's difficulty.

**Cross-tool calibration.** When Loop 1 is the first data on this platform
after a strategy built on another tool's baselines, compare the two metrics
topic-by-topic; a divergence >15 percentage points flags the topic for
posture review. Cross-tool metrics rarely agree — treat this as posture
validation, not data-quality debugging.

Platform mechanics: see §13 in the platform companion.

### 13.4 Empty responses are a different state from "brand not mentioned"

Some chats come back with no meaningful response (engine refused, timed out,
returned a generic "I can't help"). **Filter them out** of headline
visibility — missing data, not negative data — and **report** the
empty-response rate as a separate metric so the user sees it.

Regulated verticals (pharma, gambling, finance, alcohol) are especially prone
to refusals; that is a structural reality of the niche, not a detection
problem. Keeping empty-response distinct from brand-not-mentioned stops the
visibility math silently punishing the brand for a refusal. The same
discipline applies before calling a cohort "parametric": a refusal, an empty
placeholder and a genuine no-retrieval answer share the empty-sources
signature and call for different actions — sample the response text first.

Platform mechanics: see §13 in the platform companion.

### 13.5 Per-answer share, not per-question presence

**A per-question ever-flag and a per-answer share are different metrics, and
the first is an upper bound on the second.** Most platforms run each prompt
many times over a window — several engines × several runs — so every prompt
carries two very different numbers:

- a **per-question flag**: was the brand named in *any* answer to this prompt,
  at any point in the window;
- a **per-answer share**: of all the answers generated for this prompt,
  in how many was the brand named.

One mention in a hundred answers sets the flag. Counting flags therefore
measures *at-least-once presence*, which reads as visibility and is not. The
gap is not academic: on one observed prompt set the per-question figure was
77% while the per-answer share over the same prompts and the same window was
41.6%, with a gap of the same size inside individual groupings — one grouping
flagged on every question sat at 61.5% of answers, another flagged on three of
eight questions at 20%.

**The rule for any stakeholder deliverable: visibility is the share of answers
(executions) naming the brand, with executions as the denominator, over a
stated period.** Report it as **"named in x of N answers"**, with the answer
count and the window in the caption. Never write "present in N of M questions"
unless it is explicitly labelled as an at-least-once figure and sits beside the
per-answer share — and never let an at-least-once figure be the headline.

The same discipline applies to any derived cut: a per-grouping, per-market or
per-engine breakdown built from flags inherits the same inflation, so the split
that decides where effort goes is the one built on answers.

Where a platform's API exposes only the flag, say so and take the per-answer
figure from wherever the platform does publish it — often the UI rather than
the API. The companion's §13 says which surface carries executions on that
platform and how to extract them; if neither surface has them, the honest
report is the flag with its label, not the flag with a visibility caption.

Platform mechanics: see §13 in the platform companion.

### 13.6 Findings hand-off shape

Findings feed the next Strategy iteration. Format is agent/user choice
(§3.7); regardless of format, findings must have:

- Each finding traceable to a platform call or export (§3.2 provenance).
- Separate branded / other-brand / non-branded sections (§3.1).
- Concrete implications for the next Strategy iteration — what would change,
  what needs more data, what can be closed out.
- **Strategy proposals section (mandatory)**, three buckets: (1) low-risk
  additive writes proposed for immediate execution — new tags, competitor
  brands, tag applications, containers, prompts — each with the finding, call
  and threshold that justifies it; (2) higher-risk writes with a decision
  gate — reframes, deletions, restructuring, roster removals — each with the
  evidence threshold that triggers execution; (3) writes considered but NOT
  recommended, with reasoning. A reporter stops at "here's what the data
  shows"; a strategist produces "here's what we should do, and what we
  shouldn't."

**Execute-now handoff (mandatory).** A proposal in the findings file is not a
proposal surfaced to the user. Any loop with a non-empty bucket 1 MUST close
its hand-off message with an explicit yes/no execution offer naming each
item inline. Empty bucket 1: omit the ask. User absent (scheduled or
non-interactive run): **do not execute autonomously** — flag the bucket and
wait for the next interactive turn. The loop is not complete until bucket-1
items are executed or explicitly declined. Bucket 2 and deferred items
(§13.16) are surfaced separately, as context.

**Mid-loop additive writes** (strictly additive bucket-1 items) need no fresh
§9.8 sign-off — the proposals table is the audit trail. Anything that
removes state, reframes prompts or restructures taxonomy still goes through
the full sign-off; the ceremony is calibrated to reversibility risk.

**Prompt-set-stability check before any trend / drift finding.** Confirm
from the intake state's write-wave timestamps (§7) that no prompt creation,
reframe or deletion landed inside the window. If one did, truncate to the
longest stable sub-window or use snapshot metrics, and document the wave
dates alongside the finding.

**Carry-forward claim re-verification.** Findings files are working memory,
not source of truth. Label every claim consumed from a prior findings file:
(a) re-verified this session, (b) carried forward unverified — caveat or drop
before any stakeholder surface, (c) pulled fresh from the platform this
session. Only (a) and (c) belong on stakeholder slides.

Platform mechanics: see §13 in the platform companion.

### 13.7 Maturity tiers (quantitative vs qualitative)

Analyse maturity has two axes that progress at different rates —
**quantitative** (aggregated metrics) and **qualitative** (chat, URL and
fanout reading). Treat them as separate tiers so qualitative work is never
deferred until metrics stabilise.

| Tier | Quantitative threshold | Qualitative threshold | Agent posture |
|---|---|---|---|
| Tier 0 — Seed | < 7 days of data, OR within 24h of a major prompt write wave | Sample 3–5 chats, enough to confirm detection is firing | No metrics as findings; chat reading to spot-check config |
| Tier 1 — Directional | ≥ 7 days, ≥ 1 chat per prompt per engine | 1 chat from the highest-mention engine per topic; top-5 gap URLs | Metrics directional; named findings corroborated by chat reading |
| Tier 2 — Analysable | ≥ 30 days, ≥ 10 chats per prompt per engine | 1 chat per active engine per priority topic; all gap URLs with ≥3 competitors | Metrics stand as findings under cohort-separation discipline |
| Tier 3 — Stable | ≥ 60 days, cross-loop trend visible | As Tier 2 plus longitudinal narrative | Trend findings and comparative deltas legitimate |

The tiers gate quantitative findings only; Tier 0 does not block chat
reading, which interprets specific responses rather than aggregating them.

- **Observable Tier 0 signal** is time since the last major write wave, read
  from the persistence store (§7) — not a platform status field. A wave
  < 24h ago means Tier 0 for metrics even if chat counts look sufficient.
- **Stable-cohort gate for trends.** Trend findings require the prompt set
  unchanged for the full window plus a 24-hour buffer before it. A write
  inside the window collapses the trend tier to Tier 0 *for trend purposes*;
  use snapshots or truncate. Cross-loop deltas across a changed prompt set
  are apples-to-oranges — flag or drop.
- **Engine-side drift** is the gate's second instrument: the measuring
  engine's own behaviour changes with model updates. Observed shape: a
  named-source share in fanout queries rose from single digits to roughly a
  third over a few weeks on an unchanged prompt set while daily fanout volume
  roughly halved. Trend claims on engine-generated denominators report volume
  alongside share and frame shifts as engine + landscape movement, not brand
  movement.
- **Day windows are a recommendation, not a hard gate.** Deadline-driven
  projects run earlier, state the window size, and flag that longitudinal
  claims need more data (§3.4).
- **Benchmark-goal vs trajectory-goal.** Tiers say what the data supports,
  not when a deliverable is due. "Where do we stand today" is legitimately
  answered by a Tier 0/1 snapshot; "how are we moving" needs Tier 2+. Capture
  the goal in the intake state (§7) so Phase B timing (§14.5) can read it.

Platform mechanics: see §13 in the platform companion.

### 13.7.1 Cross-page verification before calling a content element a weakness

Before framing an element on a low-performing page as a **weakness** ("it
underperforms because it has X / lacks Y"), check that element on at least
three other pages of the same template family — including at least one
strong and one mid performer. A single page cannot validate a causal claim;
the element may be a template feature shared regardless of citation outcome.
If a strong performer also has it, or a mid performer lacks it, drop the
framing.

**Worked example.** A promotional banner carousel was framed as a weakness on
a low-citing category page of a bicycle retailer. Across five category
pages: low-citer (carousel), mid-citer 1 (carousel), mid-citer 2 (none),
strong performer (none), weak performer (none). No pattern with citation;
the real driver was specific quantitative content (spec tables, named test
results with years, review counts) on the strong pages. Framing dropped.

**Why this is its own gate.** §13.7 governs when quantitative findings can
stand; this governs when *causal* content claims can stand. The numbers
underneath can be defensible while the attribution above them is wrong — and
a false-positive critique erodes credibility and wastes dev cycles.

Platform mechanics: see §13 in the platform companion.

### 13.8 Qualitative chat reading is peer analysis

Reading responses is prescribed as a detection quality gate — but that
under-specifies it. Chat reading is **first-class analysis**: it surfaces
engine parametric biases, source-authority patterns, competitive positioning
and narrative framings that aggregates cannot express.

**Minimum chat-count target.** For any topic with more than five prompts,
read **at least one chat per active engine** — the full topic × engine
matrix, not single-dimension sampling. This is a floor. Engine personality
differences within a topic are where the strategic insight usually lives;
reading around twenty chats across a ten-topic × three-engine matrix, versus
a handful read opportunistically, surfaced whole classes of findings
(parametric fabrications, retrieved-but-not-cited authority signals,
generalist vs specialist sentiment asymmetries) absent from the smaller
sample. Topics with ≤5 prompts can use single-per-topic sampling.

Prescribed activities: (1) **per-engine comparison** per priority topic —
which brands, in what order, with what framing and sources; (2)
**competitive positioning reading** — when a competitor outperforms, read
2–3 chats for *why*, not just *that*; (3) **narrative framing audit** — in
regulated verticals, the cautionary or hedging language around the category
propagates into brand representation and never shows in sentiment scores.

One well-read chat often beats a thousand aggregated rows. Budget
qualitative time as analysis, not as a verification tax.

Platform mechanics: see §13 in the platform companion.

### 13.10 Fanout mining is a continuous refinement signal

Where the platform exposes query fanout (the sub-queries an engine issued
while generating a response), intake uses it to seed the prompt set — but the
data keeps producing signal afterwards, and most projects never exploit it.
Run fanout mining as a standing Analyse activity:

1. **Parametric-bias detection.** High visibility with zero fanout: the brand
   lives in the model's priors, not in content it controls. Zero visibility
   with rich fanout: the retrieval surface is busy but the brand isn't on it.
   Wherever the pattern holds (§11.13): shift content effort to
   retrieval-based engines, set long-horizon expectations for the parametric
   engine, prioritise training-data-influencing work. Regulated verticals
   are the sharpest case, not the only one.
2. **Adjacent-intent discovery.** A prompt for "best insurers for classic
   cars" that fans out to "specialist brokers for agreed-value classic-car
   policies" is telling you where the next prompt slot goes.
3. **Platform-mention mining (ranking-dominated verticals).** Grep fanout
   text for candidate ranking bodies by name; a high named-source share
   identifies *which* bodies gate visibility, one step earlier in the causal
   chain than outcome metrics (§11.19). Observed shape: roughly a fifth of
   all fanout queries in one such vertical named one of a small handful of
   ranking bodies, with tier vocabulary and year qualifiers, and none named
   any other directory.
4. **Trend caveat.** Fanout-derived series carry the engine-side drift
   confounder (§13.7): always report daily fanout volume alongside a share.
5. **Engine-scope caveat.** Fanout is usually exposed for a subset of engines
   only; phrase findings as "what engine X searches for" and use the
   response-level sources list as the retrieval signal elsewhere.

Platform mechanics: see §13 in the platform companion.

### 13.10.1 Reading an audience-exploration band

Where the strategy carries an audience-exploration band (§9.9), read it
through the platform's sources or citations view — the companion names the
view — and **never** through the visibility views. Every prompt in the band
scores zero by construction; a visibility read of it measures nothing. The
band is excluded from every headline, which its `signal:diagnostic` tag
already does provided the filter is actually applied (§13.3).

A tracker measures two independent things — whether the brand is named, and
what the engines cite — and a prompt that scores zero on the first can be
fully informative on the second. The deliverable from this band is the ranked
list of cited third-party domains per audience, not a metric.

Two hand-off consequences: the output goes to a consumer **outside** the
tracking tool, so it does not belong in the strategy-proposals buckets of
§13.6; and once a category's sources have been harvested the band rotates
(§9.9), which is a prompt write — record it as a write wave so the
stable-cohort gate (§13.7) sees it.

Platform mechanics: see §13 in the platform companion.

### 13.16 Deferred-items queue (mandatory hand-off to next loop)

§12.8 is the Write hand-off; §13.16 is the Analyse equivalent. Every Analyse
loop must produce a **deferred-items queue** as a discrete, named artefact
the next loop reads first — not a bullet inside the findings file. Without
it, "review next loop" items live only in session memory and are quietly
lost; the failure is invisible until weeks later.

**Required sections:** (1) verification required; (2) deferred decisions,
each with the evidence threshold that triggers execution; (3) strategy-level
items for the next Strategy iteration; (4) outstanding analyses not run for
data-maturity reasons; (5) recommended loop sequence.

**Mandatory `deferral_type` on every item:** `awaiting_signoff` (executable
now, blocked only on a user yes/no — surface at the next hand-off per
§13.6), `awaiting_data` (revisit at the named data window),
`awaiting_external` (dependency outside the agent's control). Without types
the queue drifts — sign-off items sit dormant, data items run prematurely.
Untyped items fail the Pre-Analyse gate (§15): a hard validation
requirement, not a format nicety.

**Format and storage:** agent/user choice (§3.7) — a three-column table
(`item`, `deferral_type`, `trigger/owner`), YAML, a named intake-state
section, a per-loop handoff doc — but a discrete artefact, not a prose
paragraph mixing the classes. Produce it every loop, even with empty
sections: an empty section is itself a signal. If no action emerges from the
findings, the strategy may have reached a stable state and Phase B may be
ready (§14).

Platform mechanics: see §13 in the platform companion.

---
