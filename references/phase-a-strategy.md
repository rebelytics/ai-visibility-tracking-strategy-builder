# Phase A — Strategy (§9–§10)

Part of the **ai-visibility-tracking-strategy-builder** skill (CC BY 4.0 — Eoghan Henn / [rebelytics.com](https://rebelytics.com)). Section numbers are global across the skill family — the section map in `SKILL.md` says where each § lives; platform companions extend some sections with their own "Peec implementation" / "Sistrix implementation" parts.

**Load trigger:** Read before drafting or revising any strategy recommendation, and again before the strategy sign-off. Load the platform companion's `phase-a-strategy.md` alongside it before writing any recommendation that names a field, a tag string, a plan tier or a write operation — the companion holds those. §10 applies to existing projects only.

**Contents:**

- 9 Phase A — Strategy (hard gate, recommendation block format)
- 9.1 Prompt volume split (load-bearing recommendation) — three complementary allocation methods
  - 9.1.0 Direction first — budget fixed, or budget being sized (the product coverage floor)
  - 9.1.1 Search-volume axis (orthogonal to the funnel split)
  - 9.1.2 Damped revenue-share weighting (across containers)
  - 9.1.3 Breadth across intent clusters (within a container)
  - 9.1.4 Filling a budget from a larger pool — composition is a constraint (incl. the expected-answer-shape classifier)
  - On total size
- 9.2 Country and market scope
  - Cross-market divergence check (before reusing any allocation)
- 9.3 Brand roster
  - Own-brand identity
  - Brand classification step (mandatory, before proposing any roster)
  - Competitor selection
- 9.4 Tag taxonomy
  - Which dimension goes where: allocation by field cardinality
  - The three tool shapes
  - Recommended tag set
  - Namespaces and tag-sprawl discipline
  - Taxonomy hygiene check (existing projects only)
- 9.5 Container structure
  - Prompt disposition and brand-name containers
- 9.6 Model coverage — platform companion
- 9.7 Reporting KPI split — the brand-mention split
- 9.8 Strategy sign-off
- 9.9 Prompt authoring
  - Prompt patterns
  - Authoring rules (incl. service grounding of every named service, template kind, per-language validation)
  - Product detectors (a prompt covers a product only if it names it)
  - Disambiguation pass (mandatory before a set is finalised)
  - Audience-exploration probes (the mirror of owned-territory)
  - Trust / reviews probes (branded, for source diagnosis)
  - Language-specific adaptation
  - Delegating to parallel authors
- 10 Prompt disposition framework (existing projects only)

---

## 9. Phase A — Strategy

**Hard gate:** Strategy cannot begin until the Intake summary block
(§8.4) has been written and contains non-empty entries — or explicit
"skipped because …" rationales — for each of: Ring 1 tools used, Ring 2
steps completed (first loop only), Ring 3 automated inventory + user
ask, and identified gaps. If any row is absent rather than explicitly
skipped, return to §8 Intake. See §3.8 for why this gate exists.

Goal: convert the intake into a concrete, prescriptive strategy
recommendation. The user accepts or calls out an override. No menus,
no "which would you like" questions.

Every recommendation block follows the same structure:

> **Recommended:** *[concrete numbers, categories, or choices]*
>
> **Reasoning:** *[1–2 sentences tied to intake data]*
>
> **Override this if:**
> - *[condition 1]* → *[what to change]*
> - *[condition 2]* → *[what to change]*
> - *[etc.]*

Platform specifics — field names, tag strings, plan tiers, write
operations — are not part of the recommendation text. The platform
companion's `phase-a-strategy.md` carries them under the same section
numbers; read its part of each section before finalising the block.

### 9.1 Prompt volume split (load-bearing recommendation)

The budget has to be split along more than one axis, and the family uses
**three allocation methods**. They are complementary, not rivals; which
one leads is decided by what demand data the intake (§8) actually
produced:

| Method | Splits the budget across | Leads when |
|---|---|---|
| **Funnel-stage split** (this section) | Funnel tiers, within every container | Always applied as the cross-cutting check; leads the whole allocation when no per-category demand data exists |
| **Damped revenue-share weighting** (§9.1.2) | Containers — the commercial categories of §9.5 | Landing-page revenue, or an equivalent per-category outcome signal (leads, pipeline), exists per market (§8, Source 1) |
| **Breadth across intent clusters** (§9.1.3) | Intent clusters, within a container | Filling a container's slots once its size is fixed; or as the rough category split where neither of the above has data |

The search-volume axis (§9.1.1) is orthogonal to all three: it
describes the mix *within* whatever the other methods produced.

#### 9.1.0 Direction first — is the budget fixed, or is the budget being sized?

Every method in this section distributes a budget, so reaching for one
silently assumes the budget is an input. Often it is the question. An
agency working to a client's fixed plan tier and a brand deciding which
tier to buy produce different artefacts from identical intake data, and
nothing in the data says which engagement this is. Settle it in **one
question to the user before any allocation runs** — *"Is the budget
fixed, or are we working out what budget you need?"* — and record the
answer in the sign-off (§9.8).

**Budget fixed → distribute it.** The methods below apply as written.
One mandatory addition: the sign-off reports **how many of the brand's
products or services the budget leaves unmeasurable** — the products
that end with no prompt at all — so the trade-off is visible rather
than buried in the allocation. A product with no prompt returns no
signal, and in the reporting that is indistinguishable from a product
the brand is invisible for: a coverage gap presents as a visibility
finding, and it is least visible precisely where it is largest.

**Budget being sized → coverage is the constraint, the budget is the
output.** Build a **product coverage grid** — every product or service
the brand actually sells (the catalogue baseline of §8.3.2, grounded per
§9.9), by market — and give every cell a **floor of two prompts**: one
asking who provides it (provider-selection shape) and one asking how to
obtain it (how-to shape). The floor is two because below two prompts a
product cannot distinguish a visibility problem from a coverage gap — a
single prompt at zero is either. Demand then decides which products are
**promoted to depth** (more prompts and more instruments inside the
product, sized by §9.1.1–9.1.3), and the sum is the budget to propose.
Demand sets depth; it never sets presence.

**Thin demand in a niche catalogue is not evidence of absent demand.**
In a specialised B2B catalogue most products have no reliable search
volume, and a platform's own per-prompt volume field is conditioned on
the prompts that already exist — a product nobody tracks looks like a
product nobody wants. Applied as written to such a catalogue, the damped
method can leave most of the brand's products out of the set — the
opposite of what a brand whose concern is incomplete coverage asked
for. This does not overturn §4.2: demand
still decides every slot above the floor, and in the fixed-budget
direction it decides the whole allocation. What it may not do is remove
a product the brand sells from the measurement while the budget is still
being decided.

> **Recommended:** 50% discovery, 30% consideration, 15% comparison,
> 5% branded reputation monitoring. Tag each prompt with its funnel
> stage: discovery → `funnel:awareness`, consideration →
> `funnel:consideration`, comparison → `funnel:decision` (the §9.4 tag
> values); "branded reputation monitoring" is not a funnel stage — it is
> the own-brand cohort of §9.7 and is carried by the brand-mention tag.
>
> **Reasoning:** Discovery dominates where the brand needs to attract
> new customers (the overwhelming majority of tracking use cases).
> Comparison slots capture head-to-head competitor queries where AI
> answers frequently rank. Branded reputation monitoring measures how AI
> describes the brand when asked about it by name — useful, but should
> never dominate because branded prompts score near 100% visibility by
> construction (§4.10, §3.1).
>
> **Override this if:**
> - B2B or long sales cycle → flip to 25/45/20/10 (more consideration
>   weight).
> - Strong existing brand equity and branded prompts already at
>   visibility=1.0 → drop branded reputation monitoring to 0%, reclaim
>   slots for discovery.
> - Regulated vertical (pharma, gambling, finance, alcohol) → add a
>   `topic:safety` band at ~10%, taken off discovery; expect
>   legal-caution framing in AI responses (see §11 pattern library,
>   regulatory-aware sentiment).
> - Very small prompt budget (≤50 prompt slots, whether by plan tier or
>   by decision) → drop comparison entirely; focus on discovery +
>   branded reputation monitoring only.

#### 9.1.1 Search-volume axis (orthogonal to the funnel split)

The funnel split above is the **primary** axis. Where the tracking tool
exposes a **search-volume signal per prompt** — an ordinal band or a
number — treat it as a second, orthogonal prompt-portfolio axis
alongside funnel stage; a prompt portfolio that's balanced on funnel but
dominated by "very low" volume prompts is materially under-weighted for
commercial coverage. How the signal is exposed, and how to handle it in
code, is in the platform companion §9.1.1 — read it before sorting or
comparing on volume.

> **Recommended volume mix (within each funnel tier):**
> - **Head (high / very high):** 20–30% — tests whether the brand
>   surfaces on the queries that drive the category.
> - **Mid (medium):** 40–50% — the workhorse prompts that carry most of
>   the signal.
> - **Long tail (low / very low):** 20–30% — captures niche / specific
>   intent and keeps long-tail coverage legible.
>
> **Reasoning:** A portfolio that's all head prompts is great for
> visibility headlines but hides long-tail gaps; all long-tail misses
> the queries that actually drive category traffic. The orthogonal
> distribution means each funnel tier itself has head/mid/tail
> coverage, not just the roster as a whole.
>
> **Override this if:**
> - Existing project with <30 prompts on a capped budget → drop long
>   tail entirely; focus on head + mid so the small budget doesn't
>   fragment.
> - Very niche vertical where head-volume queries don't exist (e.g. a
>   specific B2B SaaS category) → the "head" tier may be empty by
>   nature; concentrate on mid + long tail and note the constraint.
> - Project whose current portfolio is already ≥80% "very low" volume →
>   Loop 2 should prioritise adding head/mid prompts over adding more
>   long-tail. The volume signal makes this measurable.

Where the tool exposes no volume signal, approximate the band from the
demand sources gathered at intake (search-console impressions, keyword
tool volume, site-search frequency) and record the source of the
approximation in the sign-off.

**Keyword-database volume is not an allocation basis for an emerging
category.** Where the category is younger than roughly a year, a zero or
missing volume is a statement about the database's coverage, not about
demand (§8.5.4) — so it cannot size a container, cannot rank a topic and
cannot weight one market against another. Run the coverage control in
§8.5.4 first; where coverage fails, allocate that category from a signal
that observes the market directly (search-console impressions and clicks
in the market's own language, internal site search, community and support
questions) and state in the sign-off which signal carried the allocation
and why the keyword data was set aside. An emerging category sized from
an uncovered database is systematically under-weighted in exactly the
markets where the brand is earliest.

#### 9.1.2 Damped revenue-share weighting (across containers)

Where per-category outcome data exists — landing-page revenue for
e-commerce, leads or pipeline value per landing page for services, B2B
or SaaS (§8, Source 1) — weight the container sizes on revenue share,
**damped**. Pure revenue weighting lets a dominant category swallow the
budget; a hard cap flattens exactly the market differences you just
spent the intake establishing. A power transform around 0.6–0.7
compresses the extremes while preserving order and relative difference.

```
weight_c   = revenue_share_c ** 0.65
n_c        = max(floor, round(weight_c / sum(weights) * budget))
```

with a **floor of ~8 per container** so a strategically-live but
currently tiny category stays measurable, and a **fixed percentage
(~7%) for the brand and competitive container**, which is not
revenue-derived and is taken off the top before the weights are
applied. Any implementation needs cap handling and an integer
reconciliation step so the per-container counts sum exactly to the
budget — off-by-one totals are the most common failure of a hand-rolled
version. `references/allocate.py` implements the method, including cap
handling and the integer reconciliation; run it rather than re-deriving
the arithmetic:

```
python references/allocate.py revenue.json --budget 300 --damp 0.65 \
    --floor 8 --fixed "Brand & Competitive=7"
```

where `revenue.json` maps container → {market: revenue_share_pct}. Run it
once per market set; the columns sum exactly to the budget.

The revenue share feeding this formula must already have the
navigational-denominator exclusion, the product-page classification and
the editorial redistribution from §8 applied; weighting an
unclassified revenue table reproduces its distortions at prompt level.
The funnel split (§9.1 above) is then applied *within* each container
the formula sized.

#### 9.1.3 Breadth across intent clusters (within a container)

When filling a container's slots — and as the rough split where no
per-category demand data exists at all — allocate by intent cluster:

- **~40% core services/products** — the brand's bread and butter, using
  the most commercially direct patterns (best-of, how-to-get, cost —
  §9.9).
- **~25% competitive and comparative** — head-to-head prompts, best-of
  lists, decision-guidance prompts.
- **~20% adjacent topics** — related areas where the brand should appear
  but that aren't its primary offering.
- **~15% emerging/strategic** — newer topics the brand is investing in,
  upcoming regulations, market trends.

These are guidelines, not rigid rules. Adjust based on the brand's
priorities and the data signals from intake (§8). Where §9.1.2 has
already sized the containers, this heuristic only decides what goes
*inside* each one; it never overrides the container sizes.

An **audience-exploration band** (§9.9) is not a fifth cluster. It is a
capped, rotating allowance whose slots are set once and subtracted
before these percentages are applied — the four shares then divide what
remains. Sizing it as a share would let it grow with the container,
which is exactly the failure its cap exists to prevent.

#### 9.1.4 Filling a budget from a larger pool — composition is a constraint

The methods above produce a composition: so many provider-selection
prompts, so many how-to prompts whose value is the citation, a branded
cohort of a given size, a funnel and a volume mix inside each. The set
is then usually *filled* from a pool larger than the budget — parallel
authors' batches, an inherited project being cut down (§10), a merged
set with a ceiling. How that pool is reduced decides whether the
composition survives.

**Fill each band to its share first, then rank within the band.** A
value ranking across the whole pool answers "which are the best N" and
not "does the set still contain the mix the strategy said it would".
It removes whatever it scores lowest wholesale — and the categories
that score lowest on a commercial value score are precisely the ones
the strategy had to argue for: the how-to prompts that carry the
source-citation instrument, the diagnostic probes, the audience-
exploration band. The failure shape: after a ranked cut, whole markets
come out almost entirely provider-selection, and the instrument a
citation-gap workstream depends on has almost nothing left to measure
with. Every individual prompt is defensible and every count matches the
budget; the missing instrument leaves no trace in the artefact. So:

1. Take the specified composition as a **quota per band** — instrument
   × market × container, plus whatever else the strategy states as a
   proportion.
2. Fill each band to its quota from the prompts eligible for that band,
   ranking on value *within the band only*.
3. Where a band's eligible pool is smaller than its quota, author into
   it (§9.9) rather than letting a neighbouring band absorb the slots
   — or, if the demand is genuinely absent, shrink the band and record
   the change in the sign-off (§9.8), so the composition is revised on
   purpose rather than lost by accident.
4. After the fill — and after **every** later selection or
   disposition pass — recompute the realised mix and compare it with
   the specified one (§15.4 gate 12). A composition cannot be recovered
   by inspecting the result; it has to be re-measured.

**Classify the instrument by the head of the question.** The
composition counts prompts by their expected answer shape —
provider-selection ("which companies…", "who provides…", "best
providers for…"), how-to ("how do I obtain / prepare for…"),
definition ("what is X", "what does X mean") and the branded cohort —
and the classifier reads the **head of the question first**, then the
rest. A leading "What is X…" or "What does X mean…" is a definition
whatever follows it: "What is X, and which companies need it?" defines
the scheme and asks nobody who provides it, so it fills no
provider-selection cell even though its trailing clause matches the
provider-selection pattern. Pattern order that let the trailing clause
win once filled three products' provider cells with definitions and left
two dozen carried-over prompts in the wrong instrument (§10). Head the
column **"expected answer shape"** in every artefact until the engines'
answers have been checked against it (§13): the label is a prediction
about the answer, not a property of the prompt, and naming it as a fact
invites it to be trusted before it has been verified.

**Cap head-to-head comparisons in the branded cohort.** "[Own brand] vs
[competitor]" reads as commercial, so a value ranking favours it, and it
is the least informative branded prompt: it measures neither how the
engines describe the brand nor whose sources they draw on. Hold
head-to-head comparisons to at most about a third of the branded cohort;
the rest is reputation, trust / reviews (§9.9) and "what is / is [brand]
good for" prompts, which are what the cohort exists to measure (§9.7).
The competitive signal itself is not lost — the best-of lists
(non-branded) and "[competitor] alternatives" prompts (other-brand) of
§11.26 carry most of it, and the comparisons that remain inside the cap
carry the rest.

#### On total size

Resist the instinct to fill whatever ceiling the user names. Every
prompt should point at a revenue-bearing category, a real site-search
term, a ranking, or an observed AI-citation query. In a niche vertical,
a few hundred per market exhausts genuine demand; beyond that you are
authoring questions nobody asks, which inflates the denominator without
adding measurement value. Propose the defensible number, document an
optional tranche to reach the ceiling, and let the user choose.

### 9.2 Country and market scope

> **Recommended:** Start with the top 2 markets by revenue or traffic.
> Set the market (country) attribute on every prompt from day 0.
>
> **Reasoning:** Multi-market is cheap to add now, painful to backfill
> — every prompt without a market attribute is a prompt that won't be
> filterable by market later. Most tools carry country as a per-prompt
> field and infer language from the prompt text; the platform companion
> §9.2 says exactly which fields exist and which are required.
>
> **Override this if:**
> - Single-market brand → use one market value everywhere, but set
>   it explicitly.
> - Multi-TLD with shared content across markets → track flagship
>   market first, add others once flagship visibility data exists.
> - The brand operates in a country the tool cannot represent → flag
>   and discuss fallback with the user before proceeding (see the
>   platform companion §9.2).

Build each language/market as an independent prompt set. Share the
container structure (§9.5), but let the individual prompts diverge
based on local demand signals. Some services have strong demand in one
country but not another; some regulations and product norms are
region-specific; some competitor landscapes differ by geography.

#### Cross-market divergence check (before reusing any allocation)

**Never inherit one market's prompt allocation into another on structural
grounds.** Where a brand runs several market versions, the structural signals
— one platform, one catalogue, shared templates, numerically identical
category IDs, 1:1 localised slugs — all say "same business, translate the
prompts". They are evidence about the *platform*, not about *demand*, and
they are the most persuasive false signal available precisely because they
are visible, verifiable and beside the point. Two storefronts can share every
implementation detail and sell to populations that want different things in
different proportions.

So before reusing or translating an allocation across markets, run one
demand-side check **per market**:

1. Pick one demand source available for both — internal site search is the
   cheapest, landing-page revenue (§8.3.3a) the strongest, landing-directory
   traffic share from an SEO tool the confirming second opinion.
2. Classify it into the **same** category scheme for every market. Same
   measurement, same classification, or the shares aren't comparable.
3. Put the category shares side by side.

**Decision rule:** where a category's share differs between markets by more
than roughly a factor of two, the markets get **independent allocations**,
not a translated one. Where the shares track closely, translation is
defensible and the structural similarity is finally doing legitimate work.

The cost of skipping it: two storefronts on one catalogue can rank the same
categories in a different order — a category that carries most of the demand
in one market can be a minor one in the other, and the largest revenue
category in one market only the third largest in the next. An inherited
allocation then points a large share of one market's prompt budget at its
weakest category while starving its strongest. Record the check and its
outcome in the sign-off (§9.8); a translated allocation with no divergence
check behind it is an untested assumption wearing the clothes of a decision.

### 9.3 Brand roster

> **Recommended:** Own brand with its full identity (every owned domain,
> every name variant) + 5 tracked competitors, manually curated.
>
> **Reasoning:** Tool-suggested competitor lists skew to reference
> and UGC sites rather than commercial rivals (§4.6). A manually
> curated shortlist of 5 genuine competitors produces cleaner
> share-of-voice data than a sprawling 15+ list.

#### Own-brand identity

> **Recommended:** Configure the own brand as an identity, not a name:
> - **All owned domains** — every TLD and subdomain the brand operates,
>   not just the primary.
> - **All name variants** seen in AI responses — a fuller legal name, a
>   bare domain, an initials shorthand like "ACME" for "Acme Coffee
>   Company", localised and colloquial spellings.
> - A **pattern match** only if the name variants can't capture the
>   variant space (e.g. multiple word-boundary cases); leave it unset
>   otherwise.
>
> The platform companion §9.3 maps these three to the tool's fields.
>
> **Reasoning:** Any owned domain missing from the identity will be
> classified as a third-party domain in domain and citation reports,
> not as own — which silently misreads cross-TLD mentions as
> competitive (§4.6). Missing name variants are the single most common
> cause of understated own-brand mentions: a brand that is being
> mentioned gets recorded as absent.
>
> **Override this if:**
> - Brand genuinely operates only one domain → single domain is correct.
> - Brand has overlapping TLDs with different companies (rare, but
>   possible in regulated trademarks) → omit conflicted TLDs and note
>   in the persisted intake state.

#### Brand classification step (mandatory, before proposing any roster)

Before proposing a brand as a competitor, classify it against the
three-category shape from §4.6:

1. **Commercial competitor** — distinct business, fighting for the same
   customer's wallet. Add to the roster as a competitor; classify in
   the persisted intake state as `direct_competitor`, `aspirational`,
   or `sister_brand`.
2. **Assortment brand** — a brand the own retailer stocks and
   merchandises (typically appears as a product line at
   `/collections/{brand}`, a per-brand collection page, or a brand
   category page on the own site). Detect via a sitemap scan (§8.3.2)
   for `/collections/`, `/brands/`, `/manufacturer/`, or equivalent
   path patterns. Retailing the brand doesn't make it a competitor —
   conflating the two inflates competitor counts and corrupts gap
   analysis. Surface these separately in the Strategy output so
   stakeholders see the distinction.
3. **Marketplace / generic noise** — Amazon, Google Shopping, generic
   directory pages. Not a competitor; not stocked; skip entirely from
   the roster.

**Assortment-brand handling rules:**

- **Don't add as a roster competitor by default.** Assortment brands
  inflate SoV denominators and can turn the own retailer's own
  assortment into a headline "competitor threat".
- **Tag, not track** (preferred). Tag prompts that mention the
  assortment brand with a `brand:<name>` tag so container/tag-filtered
  reports can surface per-assortment-brand signal without polluting
  the competitor SoV.
- **Container sub-structure** (alternative, for assortment-heavy sites).
  If the retailer merchandises by brand as a primary navigation axis
  (e.g. a running-shoe store with per-brand landing pages dominating the
  URL structure), it may make sense to use those brand names as
  sub-containers (§9.5). Prefer the tag approach unless the
  brand roster is very small and assortment coverage dominates the
  commercial structure.
- **User decides.** Surface the classification choice explicitly in
  §8.3.3b (scoping widget) rather than assuming.

#### Competitor selection

> **Recommended:** For each of the 5 commercial competitors (not
> assortment brands — see the classification step above), configure
> the same identity shape as the own brand: name, all domains, all
> name variants; pattern match only if needed. Select them as:
> - **Direct competitors** — companies offering the same products or
>   services in the same markets (these should be the majority).
> - **Aspirational competitors** — market leaders the brand wants to
>   benchmark against.
> - **Emerging competitors** — newer entrants gaining AI visibility.
>
> Classify each competitor in the persisted intake state as
> `direct_competitor`, `aspirational`, or `sister_brand`. Source the
> candidates from existing rank-tracking data (who ranks for the same
> keywords), the brand's own competitive knowledge, citation data from
> any existing tracking, and the tool's own competitor discovery —
> in that order of trust.
>
> **Reasoning:** Sister-brand misclassification is a portfolio-brand
> failure mode (§11 pattern library). A sibling brand in AI responses
> takes share from the own brand on paper, but the group still wins —
> reports that don't distinguish sister brands from rivals will
> systematically overstate competitive pressure.
>
> **Override this if:**
> - Brand is part of a corporate group with sibling brands in the
>   same vertical → mark sister brands so reports self-document. Few
>   tools have a native sister flag; the platform companion §9.3 gives
>   the naming convention and the ordering rule that keeps brand
>   detection intact while applying it (see also §11.2).
> - More than 5 genuine commercial competitors exist and the plan
>   allows → add up to 10, but treat the extras as secondary in
>   SoV calculations.
> - Fewer than 3 real commercial rivals exist (niche / category
>   leader) → populate with 3 aspirational competitors (market leaders
>   the brand wants to benchmark against).

### 9.4 Tag taxonomy

#### Which dimension goes where: allocation by field cardinality

The design question is **not which grouping mechanism to use — it is which
dimension goes in which field**, and the constraint that settles it is
cardinality. This rule governs everything else in §9.4 and §9.5.

**A single-valued field can only ever hold the one dimension that genuinely
partitions the set.** Every dimension that overlaps must live in a
multi-valued field, or it is lost. So:

- The **single-valued grouping field** (the container — brand, topic,
  category, or whatever the tool calls it) carries the one dimension the
  budget is allocated against and that stakeholders own internally —
  normally the commercial category. It partitions, so it can be a budget
  container.
- **Multi-valued fields** (tags) carry every dimension that cuts *across*
  that partition: funnel stage, intent, seasonality, geographic intent,
  regulatory sensitivity, diagnostic status, brand-mention type,
  assortment brand. Multi-membership is only expressible here.
- Where the tool offers a **nested sub-level** under the single-valued
  field, use it for genuine subdivision of its parent, never as a second
  independent axis. Two orthogonal axes in a nested field cannot be filtered
  apart afterwards.
- Where the tool offers a **single-keyword back-reference** field, put the
  demand term the prompt was derived from in it. That is what keeps the set
  auditable — six months later it is the only way to answer "why is this
  prompt here".

#### The three tool shapes

Tools then differ only in which fields they expose:

- **One single-valued field only** (a brand-container model): each
  category is a hard budget container with per-container limits, a prompt
  belongs to exactly one, and every cross-cutting dimension has nowhere to
  live — so record it in the delivery document instead and accept that the
  tool can't filter on it.
- **One multi-valued field only** (a flat-tag model): categories are
  analytical labels, the budget is global, and a prompt can carry several
  tags. The partitioning dimension goes in the first tag by convention, and
  the discipline has to be self-imposed — nothing in the format enforces
  it.
- **Both at once** (a required grouping hierarchy *plus* a required tag
  array on the same record): the common and easily-missed case. Applying the
  single-valued advice alone wastes the tag array; applying the multi-valued
  advice alone leaves the hierarchy arbitrary and the budget unanchored.
  Assign by the cardinality rule above and both fields do real work.

The platform companion §9.4 says which shape the tool is and names the
fields.

#### Recommended tag set

> **Recommended:** Three axes, 15–25 tags total:
> - **Intent:** `intent:commercial`, `intent:comparison`,
>   `intent:transactional`, `intent:informational`
> - **Funnel:** `funnel:awareness`, `funnel:consideration`,
>   `funnel:decision`
> - **Category:** one tag per business category from the container
>   structure (§9.5), prefixed `cat:` — `cat:running-shoes` is a tag,
>   "Running Shoes" is a container.
>
> Plus the brand-mention dimension from §9.7 (tracked brand named /
> other brand named / no brand named), which is a reporting requirement
> rather than an optional axis, and whose exact tag strings the platform
> companion fixes.
>
> Every prompt carries at least one tag from each dimension, and exactly
> one brand-mention tag.
>
> **Don't encode brand-mention twice.** `intent:branded` and
> `funnel:branded` are the same signal as §9.7's brand-mention tag wearing
> a different prefix, and maintaining both guarantees the two drift out of
> agreement. Keep the brand-mention dimension in one place — §9.7's tags,
> because the reporting filters depend on them — and let intent and funnel
> describe what the prompt asks, not who it names.
>
> **Reasoning:** 2–3 dimensional taxonomies stay consistent under
> growth. More dimensions produce orphaned tags and inconsistent
> application. Never parallel two dimensions that measure the same
> thing (e.g. don't maintain both `transactional` and
> `funnel:decision` — pick one).
>
> **Override this if:**
> - Brand already has a taxonomy in use (brand guidelines, search-console
>   query groupings) → mirror it rather than invent a parallel one.
> - Regulated vertical → add a `regulatory` dimension with tags like
>   `regulatory:restricted` so sentiment reports can filter these out
>   of headline numbers (see §11 pattern library). A policy refusal is
>   a different outcome from a brand not being mentioned; without the
>   tag the regulated categories read as systematically worse than they
>   are.
> - Portfolio brand with sister-brand overlap → add a `relationship`
>   dimension with `relationship:sister` vs `relationship:competitor`
>   so SoV reports can distinguish.
> - Tag count would exceed 25 with all planned dimensions → drop the
>   weakest dimension (usually intent or comparison) and fold it into
>   a wider tag.

#### Namespaces and tag-sprawl discipline

Every prompt carries exactly one tag from each of the one-and-only-one
axes (funnel, intent, brand-mention); everything else is **additive** and
lives in its own namespace precisely so it cannot collide with the
one-and-only-one rules:

- `regulatory:restricted` — the prompt touches something an engine may
  refuse.
- `signal:gap-to-close` · `signal:diagnostic` · `signal:deal` — the
  disposition signals of §10, and price-driven intent (sale, discount,
  voucher), which is additive and in the `signal:` namespace precisely so
  it does not collide with the single `intent:` value.
- `source:<origin>` — e.g. `source:cited`, marking prompts derived from
  queries the brand is *already* cited for (§8, AI-citation data;
  §9.9 owned-territory probes).
- `brand:<name>` / `competitor:<name>` — the assortment-brand and
  competitor-name routing tags of §9.3 and §9.5.

An additive tag sharing the `intent:` namespace makes the brief
self-contradictory, and authors will resolve that contradiction
differently from each other.

**Discipline on the multi-valued side:** reserve secondary tags for
genuinely cross-cutting dimensions rather than every possible facet. Tag
sprawl reduces analytical clarity, and a tag applied to almost every
prompt discriminates nothing. Where the tool has no tag field at all,
record the cross-cutting dimensions in the delivery document and, if the
prompts need to remain groupable inside the tool, use naming prefixes in
the prompt records themselves.

#### Taxonomy hygiene check (existing projects only)

For existing projects, before proposing the taxonomy, run a duplication
check:

1. For each pair of tags in the project's tag list (pull it through the
   platform's API — see the companion §9.4 for the call), compute the
   prompt-set overlap (intersection of their prompt IDs, divided by the
   smaller set).
2. Flag any pair with >60% overlap as a duplication candidate.
3. For each flagged pair, propose which tag to retire and which to
   keep.

Common overlaps: `transactional` ↔ `funnel:decision`,
`informational` ↔ `funnel:awareness`, `branded` ↔ `funnel:branded`.

### 9.5 Container structure

"Container" is the single-valued grouping field of §9.4 — the tool may
call it a brand, a topic or a category. The platform companion §9.5 names
it and gives the operations for creating, merging and deleting one.

> **Recommended:** 5–8 containers for single-market projects. Each
> container maps to a business category. Container names should be
> clean (no prefixes duplicating tag dimensions — `cat:running-shoes`
> is a tag, "Running Shoes" is a container). **Containers name
> categories the own brand sells into — never commercial competitor
> names** (§4.8).
>
> **Reasoning:** More than 10 containers usually signals either multiple
> markets mashed into one project (container-per-market is wrong —
> that's the market attribute's job, §9.2) or containers acting as
> tags. Every tag that names a prompt cluster larger than ~3 prompts
> should be considered a candidate container, not just a tag (§4.8). A
> competitor brand name as a container is a strong signal the brand
> roster (§9.3) isn't classified correctly — competitors belong on the
> roster, not as containers.
>
> **Override this if:**
> - Multi-category marketplace with genuinely distinct verticals → up
>   to 12 containers is acceptable if each has 8+ prompts.
> - Single-vertical specialist → as few as 3–4 containers is fine.
> - Existing project has overlapping containers (e.g. "Coffee" and
>   "Coffee Equipment") → propose a merge: move the prompts to the
>   surviving container, then delete the redundant one (companion §9.5
>   for the operations).
> - Assortment-heavy retailer where brand names dominate site structure
>   → assortment brand names may legitimately serve as sub-containers or
>   (preferred) as `brand:<name>` tags; see §9.3's
>   "Brand classification step" for the decision criteria.

How to arrive at the structure:

1. **Map to internal structure.** Containers should reflect how the
   brand organises its business — divisions, product lines, or
   strategic pillars. If they have three divisions, that's likely three
   containers. This makes the tracking data immediately actionable
   because it maps to the people who own those areas internally.
2. **Add strategic containers.** Beyond the business divisions,
   consider:
   - **Training/Education** — if the brand offers courses or
     certifications.
   - **Brand & Competitive** — prompts that test brand awareness and
     head-to-head comparisons; the fixed-percentage container of
     §9.1.2 and the placement home for tracked-brand prompts (§9.7).
   - **Market/Industry** — broader market-level prompts that test
     general awareness.
3. **Size by demand, prune by value — inside each band.** Container
   sizes come from §9.1. Where the tool enforces a fixed per-container
   limit instead, some categories will need more aggressive pruning
   than others; prioritise by commercial value, not by the number of
   possible topics — but rank within each instrument or funnel band,
   never across the whole container, or the pruning deletes the
   composition (§9.1.4).
4. **Mirror across languages.** The same container structure should
   work across all markets, and **container names should be
   language-neutral and identical across markets** — the market
   attribute already carries the market. Individual prompts differ; the
   containers stay consistent. Localising the container label buys
   nothing and destroys cross-market comparison, which on a
   multi-market project is most of the value.

For e-commerce, product category breadth matters more than internal
team structure: build containers around the largest/highest-value
categories rather than mirroring the org chart.

**Example structure for an insurance broker:**
- Container 1: Personal Lines (motor, home, travel, life)
- Container 2: Commercial Lines (liability, property, fleet)
- Container 3: Advice & Claims Support
- Container 4: Brand, Competitive & Market

**Example structure for an e-commerce brand:**
- Container 1: Product Category A
- Container 2: Product Category B
- Container 3: Brand & Reputation
- Container 4: Purchase Intent & Comparison
- Container 5: Market & Trends

#### Prompt disposition and brand-name containers

When reviewing an existing project's prompt set against the new
container structure, watch for prompts whose container is a brand name.
Two sub-cases:

- **Container is a commercial competitor name** → move the prompt to the
  relevant category container and add a `competitor:<name>` tag. This
  preserves the data while routing the signal to the right axis.
- **Container is an assortment brand name** → apply §9.3's
  classification rules. If the retailer merchandises by brand at
  primary-navigation depth, the container may be legitimate; otherwise
  move the prompt to a category container and tag with `brand:<name>`.

Either move is a container reassignment, not a text edit — on platforms
where prompt text is immutable, a reassignment keeps the history that a
delete-and-recreate would lose (companion §9.5, §10).

### 9.6 Model coverage — platform companion

Which AI engines a project tracks is plan-tier specific, so the whole of
§9.6 (engine selection, plan detection) and §9.6.1 (prompt-credit
detection) lives in the platform companion. Read it before the sign-off;
the sign-off must record the engine set as a recommendation like any
other §9 block. The one platform-independent rule: every tracked engine
inflates run count and cost proportionally, so match engines to the
audience rather than defaulting to "all models" — and on a capped plan,
the productive question is "am I getting maximum signal from the engines
I have?", which is answered by prompt quality and brand-detection
configuration (§9.3), not engine rotation.

### 9.7 Reporting KPI split — the brand-mention split

> **Recommended:** Report branded-prompt metrics and non-branded-prompt
> metrics as **separate KPIs**. Never average them into one headline
> visibility number.
>
> **Reasoning:** Branded prompts score near 100% visibility by
> construction (the prompt mentions the brand). Rolling them into
> overall SoV inflates headline metrics and obscures the real
> "unprompted discovery" signal (§4.10, §3.1). Observed gap in a
> comparable set: branded visibility in the nineties against unbranded
> in the teens — a blended figure is meaningless.
>
> **Override this if:**
> - Brand has no branded prompts tracked → skip this split (it's a
>   non-issue). Still recommended to add 2–3 branded prompts for
>   brand-awareness tracking, but keep them tagged as branded
>   and filter them out of discovery reports.

**Strict-with-disclosure rule.** Separate reporting of branded vs
non-branded is required (§3.1). If a combined metric is ever produced —
e.g. because a stakeholder insists on a single headline — it must be
accompanied by an explicit "this is an anti-pattern" disclosure and a
breakdown showing both cohorts underneath. Never silently produce a
blended figure. The disclosure isn't a formality; it's the mechanism
that prevents the blended number from becoming the canonical one.

**Three cases, not two.** Before adopting any brand-mention taxonomy,
ask **what fraction of the tracked entity's value comes from entities it
does not own**. For a single-brand business the answer is "none", and a
branded/unbranded binary works. For an intermediary — a retailer, a
marketplace, a distributor, an agency — the answer is "most of it",
because an intermediary's whole business is other people's brands. There
the binary quietly breaks, and the case it loses is the main case rather
than an edge case.

Tag on the only question with a stable answer: **who is named in the
prompt text?** Three values, set at prompt creation:

- **Tracked brand named.** Near-guaranteed mention. Tests brand
  awareness and how the AI *describes* the brand, not whether it
  discovers it.
- **Another brand named, tracked brand not.** A commercial competitor,
  or an assortment brand — a manufacturer or supplier whose products the
  brand stocks or represents (§4.6 / §9.3). Whether that brand competes
  or supplies does not change the tag — the same company is frequently
  both, and "who is named" is the only question with a stable answer.
- **No brand named.** Generic category queries. The hardest and most
  valuable signal — whether the brand appears when nobody asked about
  it.

Few tools have a native branded/non-branded concept; the user-defined
tag is the standard, and the platform companion §9.7 fixes the three tag
strings and the report filters that consume them.

**Two tags or three?** Where the own brand's value is essentially all its
own — a manufacturer, a single-brand D2C business — the other-brand value
will be a handful of comparison prompts and folding it into no-brand-named
is defensible. Where the brand is an **intermediary** (retailer,
marketplace, distributor, agency), the third value is mandatory: most of
what it sells belongs to somebody else, so "someone else's brand is named"
is the main case and the biggest cohort, not an edge case. §4.10 states the
test — what fraction of the tracked entity's value comes from entities it
does not own. Decide this at Strategy time and record it in the sign-off
(§9.8); retrofitting a third cohort onto an already-authored set means
re-reading every prompt. Leaving it undefined guarantees inconsistent
labelling — where a two-value scheme has been handed to several people
authoring in parallel, the same prompt construction has been tagged both
ways by different authors, each defensibly.

**Other-brand prompts are not easy wins.** The own brand has to be
surfaced as a place to buy the named brand — it is not named in the
prompt, so nothing guarantees it appears. So: report the cohort on its own
line rather than merging it into either neighbour, keep it out of the
branded cohort, and let these prompts live under whatever category
container they are actually about rather than concentrating them in a
brand container (§9.5). For an intermediary this line is frequently the
most actionable of the three, because it measures whether the brand gets
surfaced as a place to buy brands it actually stocks.

**Placement.** Keep tracked-brand prompts concentrated in one container
(usually Brand & Competitive) rather than scattering them, so the easy
wins don't inflate every container's score. Other-brand prompts belong
wherever they naturally sit — forcing them into the brand container hides
them inside a cohort they don't behave like.

**Ratio.** There's no fixed target. Some brands work well with only 5%
tracked-brand prompts; others need more. Optimise on what the brand
actually needs to measure — but where the other-brand case is
commercially large, size it deliberately rather than letting it fall out
of the authoring. Whatever ratio is chosen is a composition, and is
filled and re-measured as one (§9.1.4, §15.4 gate 12); inside the
tracked-brand cohort, head-to-head comparisons stay under the §9.1.4 cap.

Exactly one brand-mention tag must be applied at creation time (a prompt
with no brand-mention tag is a configuration bug — it can't be filtered
into any cohort). Tags are the cleanest split because they survive
container restructuring (§9.5), they cross container boundaries (a
branded prompt can live under any container), and they flow through the
tool's report filters natively. Document the tag identifiers in the
intake state (§7) so downstream loops can compute the split without
re-deriving.

**Codify this as a value-add.** Whenever a project is built or
rationalised, the brand-mention tag set is part of the strategy
deliverable, not an implementation detail. The tag naming, the
convention, and the rationale appear in the sign-off artefact (§9.8) —
it's a piece of methodology the strategy adds on top of what the tool
ships natively.

### 9.8 Strategy sign-off

Before the Write sub-phase (§12) runs, the user must sign off on the
Strategy output. The **sign-off is required; the format is not.**

The sign-off artefact can take whatever form fits the engagement:

- A full markdown strategy document (one example — see the schema below
  for a concrete structure).
- A concise structured message in the chat confirming each §9.1–9.7
  recommendation.
- An interactive list the user ticks through.
- A handoff doc in environments without persistence.

What the sign-off must capture, regardless of format:

- Loop number and date.
- Each §9.1–9.7 recommendation as accepted or overridden, with the
  override reasoning where applicable — including the allocation
  direction (§9.1.0: budget fixed, with the count of products left
  unmeasurable, or budget being sized, with the resulting total), which
  §9.1 allocation method led and why, the cross-market divergence check
  and its outcome (§9.2), the two-or-three-tags decision (§9.7), and
  the engine set (§9.6, from the companion).
- Prompt disposition decisions (existing projects) — see §10.
- The implementation plan preview (what the Write sub-phase will do).
- The measurement plan (earliest sensible next Analyse per §12.7).
- Any content-strategy findings surfaced during intake that live
  outside the tracking tool.

Example full-strategy-document structure (one of several valid formats):

```
# [Brand] AI Visibility Tracking Strategy — Loop N
Date | Project | Build or Refine | Prepared by

1. Executive summary (1 paragraph)
2. Intake & data sources (what was consulted, what was provided,
   what gaps remain)
3. Strategic recommendations (one block per §9.1–9.7 with Recommended /
   Reasoning / Override blocks)
4. Prompt disposition — existing projects only (§10 six-bucket table)
5. Implementation plan (Write preview: what will be written to the
   tool, in what order)
6. Measurement plan (what to watch, earliest re-analysis date, baseline)
7. Content strategy findings (non-tool actions surfaced during intake)
8. Appendix: intake state snapshot, data sources table, override decisions log
```

If the full-document format is chosen, it's **presentation quality** —
formatted for a stakeholder to read without further explanation. Use
tables, headings, and numbered blocks. Avoid agent-internal jargon.

If a shorter format is chosen, the sign-off still needs to be a concrete
artefact (not implicit) — something the user can point at and say "yes,
this is what I signed off on". The Analyse sub-phase (§13) will refer
back to it.

### 9.9 Prompt authoring

The strategy fixes how many prompts go where; this section fixes how
each one is written. Apply it whether the agent authors the set itself or
delegates batches. The core principles of §4 (every prompt earns its
slot; the wildcard principle and its non-determinism counterargument)
apply throughout.

#### Prompt patterns

These patterns recur across industries. Use them as building blocks:

| Pattern | Example | When to use |
|---------|---------|-------------|
| Best-of | "Best [service] providers" | Core commercial intent |
| How-to-get | "How do I get [product/service]" | Purchasing journey |
| Cost | "What does [service] cost" | High commercial intent |
| Comparison | "[Brand] vs [Competitor]" | Competitive awareness |
| Best-for | "Best [service] for [industry/size]" | Segmented commercial |
| Provider-choice | "How to choose a [provider type]" | Decision-stage |
| Geographic | "Best [service] in [location]" | Local intent |
| Duration | "How long does [service] take" | Buying timeline |
| Requirements | "[Service] requirements" | Pre-purchase research |
| Branded | "What is [brand]" | Brand awareness |

#### Authoring rules

Rules worth keeping whatever the brand:

- **Conversational, not keyword.** Prompts are questions someone asks an
  assistant, not search-engine keywords. "How do I get my bike serviced
  before a long tour?" — not "bike service".
- **One prompt per intent — the wildcard principle.** Each prompt
  represents a cluster of related queries, not a single exact phrase.
  "Best running shoe shops", "Which running shoe store is best" and "Top
  running shoe retailers" are one prompt, not three. The platform re-runs
  prompts on a schedule, so non-determinism is handled at the measurement
  layer; phrasing variants at the prompt-set layer buy nothing and cost
  breadth (§4).
- **Commercial intent is the default.** For each prompt ask: if an AI
  answers this and names the brand, could that plausibly lead to a sale
  or enquiry? Include "best [service] providers", "how do I get
  [service]", "[A] vs [B]", "what does [service] cost". Exclude "what is
  [concept]", "history of [standard]", "[acronym] meaning" — unless the
  brand's business model is inherently educational (a training academy),
  in which case training-intent queries qualify. Anything else needs a
  deliberate justification.
- **Ban the educational openers.** "Analyse", "What is", "How does …
  work", "Difference between" and their equivalents in every target
  language produce essays in which no provider is named. Apply the
  filter *at authoring time*: in one prior engagement several prompts
  were created and deleted inside 48 hours because the intent filter
  ran after authoring rather than during. List the exact banned strings
  per language in the brief so the rule is checkable.
- **The deliberate exception: owned-territory probes.** Around 15% of the
  set should probe the informational ground the brand is already cited
  for (§8, AI-citation data), tagged `intent:informational` plus a
  `source:` tag, and `signal:diagnostic` where no provider would ever be
  named. Without them a commercial-only set reads as a flat near-zero
  line and cannot answer whether owned authority converts. Without the
  tag they inflate the headline. Both halves matter. Its mirror image —
  prompts whose value is the citation map rather than the brand's
  standing — is the audience-exploration band below.
- **Use real vocabulary.** Product, model, variety and brand names come
  from the brand's own data — site-search terms, the live brand
  subcategories, the grounding queries. Never invent them, and never
  assert what the brand stocks beyond what the data shows.
- **Ground every named offering in the brand's catalogue.** A prompt
  that names a product, product line, service, programme or standard
  is a claim that the brand could plausibly be the answer. Verify the
  claim against the brand's own pages (the §8.3.2 sitemap baseline,
  fetched) before the prompt is written — not against what the industry
  offers, and not from memory. Where the brand does not offer it,
  either drop the prompt or keep it only in a non-commercial shape
  ("how do I prepare for X", tagged as an owned-territory or diagnostic
  probe); a provider-selection shape ("best providers for X", "who
  should I hire for X") for a service the brand does not sell can only
  surface competitors. The same check runs on every prompt carried over
  from an existing project — inheriting is not grounding (§10, §15.4
  gate 13).
- **Match the template kind to the service actually sold, not to the
  catalogue label.** When prompts are generated from templates per
  product, the template kind for a product (purchase, subscription,
  installation, repair, consultation, course, managed service…) is read
  from what the brand delivers for that product on its own page, not
  inferred from the catalogue heading it sits under. A software vendor
  that lists an integration under "Products" but only documents it does
  not sell it; a clinic that lists a treatment under "Services" but only
  refers patients elsewhere does not provide it. "How much does
  [product] cost" or "who installs [product]" templated onto such an
  entry asks for something nobody sells — a wrong kind is a structural
  zero exactly like a service the brand does not offer (§15.4 gate 13).
- **Validate every generated prompt, in every language, before any
  write.** Template substitution breaks grammar in ways a spot check in
  one language never sees: in English the article before an initialism
  follows its pronunciation, not its first letter ("an SME…" but "a
  UK…"); a product name that already ends in its noun doubles it ("…
  Analytics Platform platform providers"); a name carrying a leading
  article or preposition produces "for of X" and "best the X"; a
  parenthetical in the name lands inside the question. Run a
  language-aware validator over the full set **per language** — not only
  the language the author reads best (§15.4 gate 15). The failure shape:
  one language has a validator, the other has none, and the unchecked
  language's broken prompts go live on a platform where prompt text
  cannot be edited after creation.
- **Placement.** Tracked-brand prompts belong only in the Brand &
  Competitive container (§9.7); other-brand prompts go wherever they
  naturally sit.
- **Exact count.** Every batch has an exact target per container from
  §9.1. Hit it precisely and state the count.
- **Run the disambiguation pass before the set is finalised.** Every
  domain-specific noun that has a mainstream homonym is checked, and the
  prompt either anchored with the product category or the drift accepted
  knowingly. See the sub-section below.

#### Product detectors (a prompt covers a product only if it names it)

A prompt covers a product **only if its text names that product**. Loose
matching — any token of the product name appearing in the prompt —
credits generic prompts to products they never mention: "how to choose a
project management tool" is not a prompt about the brand's product
called "Project Hub", "best providers in [country]" is not a prompt
about a product whose name happens to contain that country, and a short
acronym product name matches inside longer acronyms and inside ordinary
words. The failure shape: loose matching credits dozens of generic
prompts to product cells they never name, and the "products already
tracked" baseline runs high before any authoring begins.

So build **one detector per product** — a distinctive pattern for the
product's name and its accepted variants, **word-bounded**, and
**case-sensitive for short acronyms** (a two- or three-letter acronym in
lower case is usually a word or a fragment of a longer name) — and use
the **same detector for all three jobs**: matching carried-over prompts
to product cells (§10), tagging prompts with their product (§9.4), and
counting the coverage baseline (§8.5.6). Three detectors that disagree
produce a grid, a tag set and a baseline that cannot be reconciled with
each other. Before any write, **assert that every prompt authored or
carried over for a product cell is detected as its own product, and as
no other** (§15.4 gate 14): a product-cell prompt its own detector does
not fire on is either mis-authored or mis-assigned, and either way the
cell is empty.

#### Disambiguation pass (mandatory before a set is finalised)

A prompt can be grammatical, natural, on-intent and still be read by the
engines as a question about a different industry. The failure is **invisible
in mention rates** — the brand simply doesn't appear, which looks like a
visibility problem — and visible **only in the cited sources**, where the
answer turns out to have been built from pages in an unrelated category.

Go through the set noun by noun and flag every term where the
brand's sense is the specialist one and another sense is the mainstream one.
The shapes that recur:

- **A compound noun whose first element is generic.** The specialist
  compound and a mainstream compound share that first element, and without
  context the engines resolve to the mainstream one.
- **A phrase that names a category in two industries.** The same two or
  three words are a product category in the brand's market and a different
  product category in a larger one; the larger one wins.
- **A bare category word that is also an everyday word**, where the
  everyday sense dominates the general-purpose training data.

Homonyms are language-specific, so the pass runs **per language**, on the
native phrasing, not on the English source prompts. A term that is
unambiguous in one target language is routinely ambiguous in another.

For each flagged term, one of two decisions, recorded:

1. **Anchor it** — add the product category or an unmistakable qualifier to
   the prompt. This costs a little naturalness and buys the right sense.
2. **Accept the drift knowingly** — sometimes the ambiguous phrasing is what
   real users type, and what the engines do with it is itself the finding.
   Accepting is legitimate; accepting by accident is not.

**The check is the cited sources of the first run, not the mention rate.**
After the set's first complete run, read the cited domains for the flagged
prompts (the sources/citations view, §13.10.1). Sources from the wrong
industry mean the prompt drifted, whatever the mention rate says. This costs
one read per new prompt set and catches a class of defect nothing else in the
pipeline sees — the general principle being that **the cited sources of a
prompt are a wording test the mention rate cannot perform**. Run it once per
new prompt set, and add the result to the §13 findings so the term is not
re-authored the same way next time.

#### Audience-exploration probes (the mirror of owned-territory)

Owned-territory probes measure the informational ground the brand *is*
cited for. The mirror case is a band of prompts covering audiences the
brand does **not** serve and has no content for. Their purpose is not to
measure whether the brand appears — it will not — but to read **which
third-party sites the engines cite** when those audiences ask. Those
cited domains are a ranked, evidence-based target list for outreach or
partnership work, generated by the same engines the visibility programme
is already paying to observe. A tracker that reads its sources data only
for the brand's own standing is leaving that list on the table.

Two properties are mandatory, and both are load-bearing:

1. **Every prompt in the band carries `signal:diagnostic`.** A dozen
   guaranteed zeros in an untagged set drags the headline discoverability
   number down and makes the whole strategy read as failing. Tagged, they
   cost nothing and the number stays honest.
2. **The container is capped and its members rotate.** Once a
   category's cited sources have been harvested and acted on, those
   prompts have done their job and are displaced by the next audience.
   Without a cap the band grows without bound, because there is always
   another audience.

**Cadence.** Prompts added now are readable only after the platform's
next complete run, so a discover-to-act cycle takes roughly 2–3× the
platform's run interval (§12.7) — a week or more where runs are weekly.
Batch band rotations to match that interval rather than trickling
prompts in; a rotation written mid-cycle is not readable any sooner.

**Read path and consumer.** The band is read through the platform's
sources or citations view, never the visibility views (§13.10.1), and
its output is consumed by a process *outside* the tracking tool. That
makes it the one part of the set whose findings do not feed the next
Strategy iteration — say so when handing over, or the band looks like an
analysis nobody actioned.

#### Trust / reviews probes (branded, for source diagnosis)

Include a **small block of branded review prompts per market** — "is [brand]
a reputable shop", "[brand] reviews", "what do customers say about [brand]" in
the market's native phrasing. Their purpose is **diagnosis, not measurement**.

Unbranded prompts cannot do this. Branded review prompts reveal exactly
**which third-party review pages and profiles the engines pull for the
brand** — which review platforms, which specific profiles, whether each is
claimed or unclaimed, current or long removed, and what rating it shows.
Typical findings from a single run: a profile on a platform nobody at the
brand knew was being cited, an unclaimed profile carrying a single bad
review, a stale profile for a platform the brand left years ago, and the
properly maintained profiles that turn out not to be cited at all.

That is actionable in a way share of voice is not — claim the profile,
correct it, retire it, or earn presence on the platform that is actually
being read — and it is the **cheapest diagnostic in the set**: a handful of
prompts, read once, producing a concrete list of owned or claimable assets.
**Route its findings to the structural side of any outreach or content
plan**, alongside the audience-exploration band's target list, not into the
visibility narrative.

**Reconcile with the branded-prompt rule, don't fight it.** §9.7 and §11.5
are right that branded prompts score near 100% by construction and inflate a
headline. These prompts are not an exception to that — they are governed by
it:

- Tag them with the branded brand-mention tag like any other branded prompt
  (§9.7), plus `signal:diagnostic` where the platform supports it, so the
  headline discoverability figure never absorbs them.
- **Exclude them from the headline visibility figure, or report them
  separately and label them.** Their own visibility number is meaningless by
  construction; the *sources* behind it are the output.
- Keep the block inside the branded allocation §9.1 already sets (the
  low branded count of §11.5), not on top of it. A few prompts per market is
  enough — the diagnostic saturates quickly, because the engines pull a
  small, stable set of review sources for a given brand.
- Read them once per market, then leave them running cheaply; re-read after
  any change to the brand's review-platform footprint.

#### Language-specific adaptation

For multilingual prompt sets:

- **Translate the intent, not the words.** "Best specialty coffee
  roasters" in English might become "Beste Spezialitätenkaffee-Röstereien"
  in German, but some prompts won't have a direct equivalent because the
  product or service doesn't exist in that market.
- **Add market-specific prompts.** If a regulation, product norm or
  category is particularly important in one market (a national
  insurance product, a cycling-infrastructure norm), include it even if
  it doesn't appear in the other language set.
- **Match local search behaviour.** Languages differ in query length and
  question form — German searchers tend to use longer, more specific
  queries; US searchers tend to be more concise. Frame prompts
  accordingly.
- **Use native phrasing.** Don't transliterate English prompt patterns
  into other languages. You are authoring an original set in each
  language; have the prompts sound natural in the target language.
- **Run the cross-market divergence check before reusing an allocation.**
  Translating the prompts is a language decision; reusing the
  *allocation* is a demand decision, and it needs one demand-side
  measurement per market first (§9.2).

#### Delegating to parallel authors

For sets beyond ~150 prompts, write a **brief** and delegate batches in
parallel. The brief carries: the container list and exact per-container
counts, the tag vocabulary with the one-and-only-one rules (§9.4), the
brand-mention definition with real example brands from the project's own
data (§9.7), the authoring rules above with the banned openers per
language, the real vocabulary files, and worked examples of good and bad
rows — authors copy the shape of the examples more faithfully than the
wording of the rules.

Per-batch validation can only check properties local to a batch.
Uniqueness, vocabulary consistency and cross-slice balance are global
properties and are unverifiable from inside any slice. So:

- Require every author to close with a **"decisions the brief did not
  cover"** section. This is how brief defects surface. When two
  independent authors flag the same ambiguity, the brief is the defect.
- Run a **merge-time validation pass** over the combined set (§15
  quality gates). This is not tidying; it is the only place the global
  invariants can be checked — counts per container, tag conformance,
  brand-mention consistency, placement, and cross-batch near-duplicates.
  Two authors given the same source anchor will independently write the
  same prompt, and neither self-check can see it. A high-similarity
  pair is a **decision to make, not an automatic defect**: a deliberate
  branded/unbranded twin ("what's the best entry-level road bike?"
  against "is *brand X*'s entry-level road bike any good?") scores high
  on token overlap and is exactly the comparison the set exists to
  make. Read every flagged pair; merge the accidental ones, and record
  the deliberate ones so the next run does not re-litigate them.

---

## 10. Prompt disposition framework (existing projects only)

When the project has existing prompts, every one of them is classified
into one of six buckets. The Action column is generic; the platform
companion §10 maps each action to the tool's write operations, and must
be read before any of them is executed.

| Bucket | Criteria | Action |
|---|---|---|
| **Keep as-is** | Strong commercial intent, non-zero visibility, aligned with a strategy category | No write required |
| **Keep with retagging** | Good prompt but needs updated tags or container | Retag / reassign container (check whether the tool's tag update is a full replacement or a merge — companion §10) |
| **Keep as gap-to-close** | Legitimate commercial prompt, currently 0% visibility, strategy flags as a performance gap to hunt | Retag with `signal:gap-to-close`; feed into content strategy recommendations |
| **Keep as diagnostic** | Zero visibility expected (structural gap, regulatory barrier, low-priority category), but worth measuring for trend | Retag with `signal:diagnostic`; filter out of headline reports |
| **Reframe** | Right intent, wrong phrasing (wrong language, wrong product framing). Where the tool treats prompt text as immutable, this is a paired delete + create and loses historical data. | Edit text where the tool allows it; paired delete + create where text is immutable. Only reframe when the improved framing is worth the data loss. |
| **Remove** | Educational (produces Wikipedia, not provider mentions), duplicative, or zero-signal without diagnostic value | Delete |

The **gap-to-close** bucket captures the common case of a legitimate
commercial prompt that currently scores zero — "where can I buy X in
Germany" for a brand that ought to appear there but doesn't. Keeping
it (vs deleting as noise) preserves the metric that tracks the gap
closing. This is different from `diagnostic`, which flags prompts we
expect to stay at zero.

**An existing prompt is not grounded by having been tracked.** Before a
prompt is placed in any Keep bucket, it passes the service-grounding
check of §9.9 / §15.4 gate 13 exactly as a new prompt would: where it
names a product, service, programme or standard the brand does not
offer (verified against the brand's own pages, not recalled), a
provider-selection shape is **Remove**, and an informational shape is
**Keep as diagnostic** at most. Inherited prompts carry the implicit
authority of already being in the project, and the authoring effort
naturally goes to the gap-fills that had to be invented — so the
carried-over share is the part of a merged set that goes unchecked
unless the disposition pass checks it explicitly.

**Carry-over into a product cell is by detector, not by overlap.** Where
the strategy has a product coverage grid (§9.1.0), an existing prompt
fills a product's cell only if that product's detector (§9.9) fires on
its text **and** its expected answer shape (§9.1.4) matches the cell's
instrument. A definition prompt does not fill a provider-selection cell
however many "which companies" clauses it carries, and a prompt that
merely shares a word with the product name fills no cell at all. An
existing prompt that matches no cell is still dispositioned on its own
merits in the table above; it just does not count as coverage.

**Cutting to a budget is a fill, not a ranking.** Where the existing set
is larger than the budget, the disposition pass fills each band of the
specified composition to its share and ranks within the band (§9.1.4);
a value ranking across the whole pool keeps the counts and silently
deletes the lowest-scoring instrument. Recompute the realised mix after
the pass (§15.4 gate 12).

The disposition table is part of the Strategy sign-off (§9.8) — concrete
and line-by-line when existing prompts are involved. Subsequent Analyse
loops (§13) will check the gap-to-close bucket for movement and may
reclassify prompts between buckets as evidence accumulates.

---
