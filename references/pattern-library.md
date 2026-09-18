# Pattern library (§11)

Part of the **ai-visibility-tracking-strategy-builder** skill (CC BY 4.0 — Eoghan Henn / [rebelytics.com](https://rebelytics.com)). Section numbers are global across the skill family — the section map in `SKILL.md` says where each § lives; platform companions extend some sections with their own "Peec implementation" / "Sistrix implementation" parts.

**Load trigger:** Skim the contents list during every Strategy and every Analyse step; read any pattern whose symptom matches the project. Do not skip the skim — patterns fire on recognition. Where a pattern's fix names a platform mechanism, read the matching "§11.N — <platform> implementation" part in the platform companion before executing it.

**Contents:**

- 11.1 Multi-TLD footprint underspecification
- 11.2 Sister-brand misclassification
- 11.3 Tag taxonomy dimension duplication
- 11.4 Zero-visibility = gap-to-close, not dead weight
- 11.5 Branded / non-branded reporting split
- 11.6 Plan-tier model coverage gating (platform-specific — lives in the platform companion)
- 11.7 Regulatory-aware sentiment
- 11.8 Fanout exposure without platform presence
- 11.9 Dead-weight listicle
- 11.10 Structural-zero category
- 11.11 Per-engine retrieval personality profiling
- 11.12 Narrative ossification risk
- 11.13 ChatGPT parametric behaviour in regulated verticals
- 11.14 Roster candidates surfacing from gap reports
- 11.15 Sale / discount intent cluster (revenue-informed)
- 11.16 Sub-brand revenue defence (revenue-informed)
- 11.17 High SoV / low visibility divergence (narrow-but-deep presence)
- 11.18 Product-knowledge vs retailer-discovery intent mismatch
- 11.19 Category-ranking mirror (ranking-dominated verticals)
- 11.20 Different page types earn citations via different recipes
- 11.21 Educational opener produces an essay in which no brand is named
- 11.22 Regulatory refusal is not a miss
- 11.23 Engine-returned-empty vs brand-not-mentioned (denominator corruption)
- 11.24 Translated prompt set masks market-specific demand
- 11.25 Phrasing-variant bloat (and the deliberate-twin exception)
- 11.26 Competitor-blind prompt set
- 11.27 Invented vocabulary in prompts

---

## 11. Pattern library

Meta-patterns observed across strategy builds. Each is a recognisable
signature with a diagnosis and a recommended action. Extend as new
patterns emerge.

Vocabulary used throughout: **topic** is the prompt's single-valued
grouping field, **tag** the multi-valued one, **roster** the list of
tracked brands, and **the platform** the AI-visibility tracking tool in
use. Where a platform has a different name for one of these, the platform
companion maps it.

### 11.1 Multi-TLD footprint underspecification

**Symptom:** Own brand's domain list contains only the primary TLD, but
the brand operates multiple TLDs.

**Diagnosis:** The platform's domain / URL citation report classifies
non-listed own TLDs as third-party (corporate) domains, not as own
domains. Cross-TLD mentions silently misread as competitive.

**Action:** During Intake (§8), enumerate all owned TLDs from the
brand-context material or a direct user ask. Populate the domain list
fully at project setup, persist in the intake state. For existing
projects, surface as a required brand-record update in the Write
sub-phase (§12). Batch all changes to the brand record (name, aliases,
detection pattern, domains) into a single write — on platforms that
recalculate metrics after a brand-record change, each separate write
costs a recalculation (see the platform companion, §11.1).

### 11.2 Sister-brand misclassification

**Symptom:** Brands owned by the same parent group tracked as
competitors without any "sister" distinction. Share-of-voice and gap
reports show sister brands as taking share.

**Diagnosis:** The platform's roster has no sister-brand flag. All
non-own brands sit in the same "tracked" bucket. AI responses don't
understand corporate ownership — they optimise for brand-name match
against the query.

**Action:** Two options:
1. **Prefix the sister brand's display name with `[Sister]`** in the
   roster so reports self-document. **Critical:** the alias list must be
   populated in the same update with the original brand name, or brand
   detection breaks silently (see the "Critical detail" below).
2. **Maintain a separate sister-brand list** in the intake state and
   post-filter reports.

Either way, the intake state records which competitors are sisters.
Surface in the Strategy sign-off: sister-brand visibility is not a
competitive loss at group level; group-level strategy discussions should
precede any "divide territory" recommendations.

**Critical detail on option 1 — aliases must be set simultaneously.**
On any platform that uses the brand's display name for mention
detection, prefixing the name with `[Sister]` without also populating
the alias list to preserve the original brand name causes **detection
to break silently**: the prefixed name no longer matches mentions in AI
responses, and the brand's visibility metrics drop to near-zero. The
prefix must be a pure cosmetic label, not a detection-changing edit.

Correct write sequence for option 1:

1. Read the current brand record (capture current name, aliases and any
   detection pattern).
2. Update name to `[Sister] <original_name>` and aliases to
   `[<original_name>, ...existing_aliases]` **in one write**.
3. Verify: re-run the brand's visibility report over the same time
   window you had before. Mention counts should be within ±5% (noise
   window). If they drop materially, the alias didn't take — revert the
   name change and investigate.

Never run step 2 without step 3, and never run the name update without
the alias update in the same write (update semantics are not guaranteed
to be atomic across separate calls). The verification (step 3) is the
only reliable signal that the cosmetic change didn't break detection.
Read §11.2 in the platform companion for the exact calls before
executing.

### 11.3 Tag taxonomy dimension duplication

**Symptom:** Multiple tags measure the same dimension (e.g.
`transactional` + `funnel:decision`, or `informational` +
`funnel:awareness`). Reports filtered by one give different counts
than reports filtered by the other.

**Diagnosis:** Taxonomy grew by accretion. Older flat-tag scheme was
never retired when the newer structured scheme was added. The two
schemes measure overlapping but non-identical prompt sets.

**Action:** Run the taxonomy hygiene check (§9.4). For each duplicated
dimension, propose a single tag to retain, retag affected prompts, and
delete the retired one. Apply **before** reports are built on the new
taxonomy.

### 11.4 Zero-visibility = gap-to-close, not dead weight

**Symptom:** 25–50% of prompts show 0% visibility after 7–30 days.

**Diagnosis:** Not all zero-visibility prompts are equal. Some are
educational (prompt produces Wikipedia, not retailer mentions — §10
"Remove"; see also §11.21). Some are structural (category that the
model doesn't understand the brand operates in — §10 "Keep as
diagnostic"). But a substantial chunk are legitimate commercial prompts
where the brand **ought** to appear but doesn't yet. Those are
gap-to-close.

**Action:** Strategy (§9) classifies each zero-visibility prompt into
the right bucket. The gap-to-close bucket feeds the content strategy
findings section — each gap becomes an editorial opportunity.
Don't delete gap-to-close prompts; they're the metric that tracks the
content strategy working. Subsequent Analyse loops watch this cohort
for movement.

### 11.5 Branded / non-branded reporting split

**Symptom:** Headline visibility metric looks reasonable (~15–20%) but
drops sharply when branded prompts are filtered out (<5%). In another
comparable set the observed gap was roughly 90% branded against under
20% unbranded — a blended figure is meaningless.

**Diagnosis:** Branded prompts score near 100% by construction. Mixing
them into the overall visibility number inflates the headline and
obscures the "unprompted discovery" signal — which is the real metric
for a commercial strategy.

**Action:** Strategy recommendation §9.7 — report branded and
non-branded as separate KPIs with the strict-with-disclosure rule
(§3.1, §9.7). Tag every prompt with exactly one brand-mention tag
(`branded` / `other-brand` / `non-branded`) and don't duplicate that
signal into the intent or funnel axes. Keep branded prompt count low
(5–10) and concentrated in one topic to avoid spray-bias. The handover
or deliverable must carry the instruction "never blend branded into a
headline number" explicitly — it is invisible in the data and expensive
to get wrong.

**Intermediary variant.** For a retailer, marketplace or distributor,
the same symptom has a second cause: prompts naming an assortment or
competitor brand behave like neither cohort, and under a two-value
scheme they get labelled inconsistently, so the split itself becomes
unreliable. Check the middle cohort exists before trusting the
diagnosis — see §4.10 and §9.7.

### 11.6 Plan-tier model coverage gating

Platform-specific: whether and how a plan tier caps the engines a
project can track is a property of the platform, not of the
methodology. Read §11.6 in the platform companion when the active-engine
count looks smaller than the plan's marketing claims. The generic rule
that survives: on a gated plan, don't spend strategy cycles on "which
engines should we track" — redirect effort to prompt quality, brand
detection (aliases / patterns) and measurement hygiene, and surface the
gating in the Strategy sign-off (§9.6) so stakeholders can factor it
into plan-upgrade decisions.

### 11.7 Regulatory-aware sentiment

**Symptom:** Small cluster of prompts shows sentiment well below the
platform's neutral midpoint (on a 0–100 scale, 15–30 against a neutral
50). Inspection shows AI models mention the brand with cautionary
framing ("be aware of legal status", "not available for legal purchase
in…", etc.).

**Diagnosis:** Brand operates in a regulated or grey-area vertical
(pharma, gambling, alcohol, adult, certain financial products). AI
models correctly add legal-caution framing, which the platform's
sentiment scoring records as negative sentiment. This is not a
reputation problem.

**Action:** Add a `regulatory:restricted` (or similar) tag on day 0.
Filter this tag out of headline sentiment reports. In the Strategy
sign-off, note that for this brand "sentiment" has two distinct
cohorts: a commercial-reputation cohort where the metric is
actionable, and a regulatory-framing cohort where low sentiment is
expected and correct model behaviour. The same tag does double duty for
refusal handling — see §11.22.

### 11.8 Fanout exposure without platform presence

**Symptom:** The query-fanout report (on a tool that exposes query
fanout) shows frequent `site:reddit.com`, `site:amazon.*`, or
`site:youtube.com` fanout queries, but the brand has zero presence on
those platforms.

**Diagnosis:** AI models believe the answer to the question lives on
those platforms. The brand is structurally absent from the retrieval
surface the model expects.

**Action:** This is NOT a tracking-tool operation. Flag in the Strategy
sign-off's content strategy findings section. Either invest in
platform presence (curated Reddit profile, Amazon seller presence,
YouTube channel) or accept the category isn't winnable via AI
visibility without that investment.

### 11.9 Dead-weight listicle

**Symptom:** Own-brand URL has high retrieval rate but zero citation
rate. Usually a blog listicle.

**Diagnosis:** Listicle is "about competitors" rather than "about
us" — the model fetches it for context about named competitors but
doesn't credit the host brand.

**How to detect (report recipe):** Requires a platform that reports
retrievals and citations separately per URL. Pull the platform's URL
citation report filtered to the own brand's domain list (filter on the
domain values themselves, not on an own/third-party classification —
classification is not reliably filterable on every platform). Sort by
retrievals. Then calculate `citation_rate = citations / retrievals`
client-side and flag URLs where retrievals are high and
citation_rate ≈ 0. Read §11.9 in the platform companion for the exact
report call, field names and sort column.

**Action:** Editorial rewrite recommendation (not a tracking-tool
operation). Add own-brand centred sections; tilt editorial voice to
position the brand as an answer, not a tour guide. Surface in content
strategy findings.

### 11.10 Structural-zero category

**Symptom:** A category has 0% visibility across all prompts and all
models, but the brand genuinely sells products in that category.

**Diagnosis:** Either the brand's positioning isn't understood by the
model (general retailer trying to show up in a vertical retailer's
space) or the category's content/authority on the brand's site is too
thin.

**Action:** Keep 2 diagnostic prompts in the category — don't delete
them, so the gap stays visible. Flag for content audit. Don't expand
the slot allocation until the content gap is closed.

### 11.11 Per-engine retrieval personality profiling

**Symptom:** Aggregate visibility masks very different per-engine
behaviours. ChatGPT retrieves heavily from UGC; AI Overview leans on
editorial domains; Perplexity favours documentation/primary sources.
Headline metrics average these into meaningless numbers.

**Diagnosis:** Each engine has a distinct "retrieval personality" —
preferences for source types, citation behaviours, and query
reformulation patterns. Treating the engine layer as homogeneous hides
structural differences.

**Action:** In the Analyse sub-phase (§13), run per-engine breakdowns
on at least visibility, SoV, and source-domain classification. In the
Strategy sign-off, note engine-specific recommendations where the
difference is actionable (e.g. "win AI Overview by increasing editorial
domain coverage; win ChatGPT by addressing Reddit absence").

### 11.12 Narrative ossification risk

**Symptom:** Phase B deliverable was committed to early (at intake or
after loop 1). By loop 3, Phase A findings have evolved, but the
stakeholder narrative is locked — editing it means "breaking the
story". Findings get softened to fit the deck.

**Diagnosis:** Committing to a stakeholder narrative before the
underlying Phase A data has stabilised creates a reverse-causality
pressure: findings get shaped by the story instead of the other way
round. The skill's integrity decays.

**Action:** Strictly enforce §14.1 — Phase B runs *only* at the end of
Phase A, as a terminal pass. If a stakeholder presentation is
unavoidable mid-engagement, produce it as a point-in-time snapshot and
label it so; don't treat it as the canonical narrative for the rest of
the build.

### 11.13 ChatGPT parametric behaviour in regulated verticals

**Symptom:** In regulated verticals (pharma, gambling, specific
jurisdictions for legal/financial services), ChatGPT shows reasonable
visibility for the own brand but the query-fanout report is empty and
the chat's source list is empty or near-empty. Other engines (AI
Overview, Copilot) behave normally.

**Diagnosis:** ChatGPT answers regulated-vertical queries almost
entirely from parametric memory — no retrieval at generation time. The
own brand's visibility is a function of the model's priors, which
update on training-cycle timescales (months to a year), not on content
published this quarter.

**Action:**

- Document the split in the strategy deliverable: per-engine note
  specifying ChatGPT = parametric, AI Overview / Copilot = retrieval.
- Shift content-strategy focus toward the retrieval-based engines where
  published content can move the needle in observable timeframes.
- Set long-horizon measurement expectations for ChatGPT visibility in
  these verticals. Quarter-over-quarter stability is the baseline, not
  the exception; a movement there is a meaningful signal.
- Revisit the pattern when the platform exposes training-cycle metadata
  or when the vertical's regulatory posture shifts.

**The broader pattern — high-salience parametric fallback.** Regulated
verticals are the sharpest case of this behaviour but not the only one.
Across multiple cross-vertical strategy builds spanning regulated,
editorial-ranked, and commerce verticals, the pattern appeared in
three non-regulated or weakly-regulated contexts: accounting-software
vendors on widely-discussed accounting and tax-compliance standards
(own-brand queries on well-known standards), branded queries in
consumer e-commerce on strongly-recognised brand names, and
category-shop queries in a vertical with genuine regulatory
ambiguity. In some sampled cohorts, effectively all branded ChatGPT
chats on strongly-recognised brands returned an empty source list — a
pointer to how complete the parametric collapse can be on
high-salience brand queries. The common thread is *queries with
strong parametric priors* — well-known brands, well-known standards
or categories, commercial queries where the model can answer from
training data alone. ChatGPT (and to a varying degree Grok) will skip
retrieval on these; retrieval-first engines (Perplexity, AI Overview,
Copilot) will not.

Keep the section named around regulated verticals because that is the
most acute case and the one that needs the sharpest strategic response.
But when diagnosing ChatGPT's "empty sources + meaningful visibility"
combo on a new project, don't rule the pattern out just because the
vertical isn't regulated. Ask instead whether the *queries* carry high
parametric salience — branded queries almost always do, and commercial
categories well-represented in the pre-training corpus often do.

See §13.10 (parametric-bias detection) for the diagnostic procedure and
§13.11 for when this rises from pattern to strategic pattern. For the
per-engine architectural reasons, see §11.13 in the platform companion.

**Sampling discipline caveat.** Before labelling a large share of a
project's chats as parametric, sample a handful of chat payloads to
confirm the response body is substantive — an empty source list has
multiple causes (see §11.23 and the platform companion), and confusing
engine-no-answer or empty-placeholder responses for parametric
retrieval will inflate the apparent share of parametric chats.

### 11.14 Roster candidates surfacing from gap reports

**Symptom:** URL / domain gap reports (gap of 2 or more tracked
competitors) consistently surface the same external brands or domains
co-appearing with tracked competitors, but those brands / domains
aren't in the tracked roster.

**Diagnosis:** The roster was built from intuition or from the
platform's auto-suggestion, which skews toward information sites. Real
commercial peers are visible in the gap data but haven't been added to
the roster.

**Action:** After each Analyse loop, cross-reference the brands
mentioned in the top-N gap URLs / domains against the roster. Any
frequently-appearing brand, or third-party corporate domain not
associated with a tracked brand, is a roster candidate for the next
§9.3 Brand roster review. See §13.13 for the full procedure and §11.14
in the platform companion for the field names.

### 11.15 Sale / discount intent cluster (revenue-informed)

**Precondition:** Web analytics (GA4 or equivalent) with landing-page
revenue is available. Without it, this pattern cannot be applied — skip
it rather than guess at intent split. See §8.3.3a item 3 for the full
revenue-data handling rules (navigational exclusion, don't-shrink-on-
revenue-alone, transient/price-driven cluster caveats).

**Symptom:** Landing-page revenue analysis shows 10-25 % (or more) of
commerce revenue concentrating on sale / clearance / outlet / discount
URLs. No prompts in the tracked set address that intent explicitly —
the existing Category and Product topics cover steady-state discovery
but not discount-driven buying.

**Diagnosis:** A distinct intent cluster (price-sensitive buyers) is
generating meaningful revenue, and AI assistants do surface sale /
discount-oriented answers when users ask for them. Not tracking those
queries leaves a silent blind spot in the strategy.

**Action:** Add 2-4 dedicated prompts that mirror the discount-buying
intent (e.g. "Where can I find [category] on sale?", "Best deals on
[brand] [product type] this month"). Tag them with a shared
`intent:price` tag so performance can be sliced as one cluster.
Consider grouping them under a dedicated topic ("Deals & Sales") if
the cluster is big enough to warrant first-class reporting.

**Transience caveat:** Revenue on sale URLs can swing between seasons
or around campaigns. Before allocating topic-level capacity, cross-
check the same cluster against steady-state search-demand signals
(GSC, Ahrefs, Semrush, or equivalent). If the revenue is
campaign-transient and
search demand is low, keep the cluster small (2 prompts, no dedicated
topic). See §8.3.3a item 3 on transient / price-driven revenue
clusters and §11.12 narrative-ossification risk.

### 11.16 Sub-brand revenue defence (revenue-informed)

**Precondition:** Web analytics with landing-page revenue available
(same rule as §11.15). Additionally: the brand operates one or more
own-brand / house-brand sub-brands that have their own landing-page
subfolder or URL pattern.

**Symptom:** Landing-page revenue analysis shows an own-brand /
house-brand sub-brand subfolder (e.g. `/our-brand/*`,
`/brand-x-exclusive/*`) ranking inside the top 3 revenue pages — often
the single most lucrative subfolder after the homepage — but the
tracked prompt set treats that sub-brand as a product line rather than
a brand entity, or doesn't track defensive sub-brand discovery
queries at all.

**Diagnosis:** The sub-brand is doing commercial heavy lifting that
the strategy isn't defending. Competitor AI answers that steer users
toward alternatives at the sub-brand's price tier can erode this
revenue without showing up in any tracked prompt.

**Action:**

1. Add the sub-brand as a first-class entry in the roster (own-brand
   alias or separate brand entity depending on domain overlap — see
   the brand-domain rules in the platform companion, §11.16).
2. Expand the brand and competitive topic allocation to include
   2-4 dedicated sub-brand prompts: direct discovery
   ("What is [sub-brand]?"), comparative
   ("[sub-brand] vs [nearest competitor]"), and use-case-anchored
   ("Best [sub-brand] for [primary job-to-be-done]").
3. Tag with an existing brand / competitive tag plus — if the
   sub-brand sits at a distinct price tier — an `intent:price` tag
   so its performance can be cross-analysed with §11.15's sale
   cluster.

**Don't shrink elsewhere to fund this.** Per §8.3.3a item 3: revenue
evidence justifies adding, not cutting. If the prompt budget is
tight, flag the trade-off for user decision rather than quietly
reallocating.

### 11.17 High SoV / low visibility divergence (narrow-but-deep presence)

**Symptom:** A brand with materially higher SoV than visibility — e.g.
9% visibility but 16% SoV, with a citation rate above 2.0 on the own
domain. Visibility is the share of chats that mention the brand at
all; SoV is the brand's share of all mention events across the cohort.
When SoV runs well ahead of visibility, the brand is mentioned many
times per chat it appears in, but appears in fewer chats overall.

**Diagnosis:** The content the model does retrieve for this brand is
dense and citable (long-form, listicle-friendly, authority-signal-
bearing) — hence the high mentions-per-chat. But the brand's
*discoverability surface* — the number of queries and source pages
the model reaches for — is too narrow for the category.

**Distinguish from other shapes:**

- *Low visibility + low SoV* → brand not known at all. Action: roster,
  awareness content, foundational listicle placements.
- *High visibility + high SoV* → market leader with matching reach and
  depth. Action: defend, don't over-invest.
- *High visibility + low SoV* → brand is named often but shallowly (1
  mention per chat). Action: improve the detail the model can surface
  (structured data, detailed product/service pages).
- *High SoV + low visibility* (this pattern) → deep content, narrow
  reach. Action: **widen reach** — more third-party mentions in
  category listicles, more Wikipedia/industry-reference presence, more
  pages that answer adjacent queries. Don't pour more depth into the
  existing hot URLs; the model is already citing them hard.

**Reporting implication:** When this pattern appears, the Phase B
narrative should resist "we're #N in SoV" as a standalone claim — pair
with visibility rank to avoid misleading a stakeholder into thinking
the brand has broad presence. See §14.2.

### 11.18 Product-knowledge vs retailer-discovery intent mismatch

**Precondition:** E-commerce project where the tracked brand is a
retailer / reseller (not a manufacturer of the products).

**Symptom:** A high-allocation category topic scores 0% or near-0%
visibility despite the brand carrying the category strongly in its
assortment. Chat inspection shows the model answers the prompts with
manufacturer brand recommendations, product test results from
consumer-review publications (e.g. Which?, Consumer Reports,
Stiftung Warentest), or editorial "best X" lists rather than
retailer mentions. Example: a query like "best [product category]
this year" returns manufacturer brand comparisons, not retailer
URLs.

**Diagnosis:** The prompts are phrased as *product-knowledge* queries
("which X is best", "X vs Y", "most reliable X") rather than
*retailer-discovery* queries ("where can I buy X online", "best online
shop for X", "where to order X with fast delivery"). AI engines
activate fundamentally different answer structures for the two intent
classes in e-commerce categories: product-knowledge queries retrieve
editorial and manufacturer content; retailer-discovery queries
retrieve shop-level content and listicles of retailers. A retailer
site can rank strongly in traditional search on the product-knowledge
phrasing and still score 0% in the tracking tool.

**Distinguish from §11.10 (structural-zero category):** Structural
zeros are categories the AI simply doesn't name *any* retailer for —
the fix is to keep 2 diagnostics and accept the ceiling. This pattern
is different: retailers *are* named in the space, just not on the
prompts this strategy wrote. The fix is on the prompt side, not the
allocation side.

**Action:**

1. Reframe the bulk of the topic's prompts toward shop-level intent:
   "Wo kaufe ich [category] online?", "Best online shop for
   [category]", "Where to order [category]", "[category] with next-day
   delivery", "[retailer] alternatives for [category]".
2. Keep 2-3 product-knowledge prompts as diagnostics — they still
   reveal whether the retailer is named in editorial comparisons.
3. Tag the shop-level cluster so performance can be sliced separately
   from the product-knowledge diagnostics.
4. Cross-reference §11.8 (fanout exposure without platform presence):
   a retailer being invisible on product-knowledge queries but
   fanning out to shop-level queries is a partial discoverability
   win.

**Reporting implication:** Phase B should frame the split as *"we
measure where people who want to buy look, not where people who want
to research look"* — keeps the prompt choice defensible.

### 11.19 Category-ranking mirror (ranking-dominated verticals)

**Precondition:** The vertical has a small number of authoritative
third-party category rankings that dominate what AI engines surface
for "who's good at X" questions — see the list in §13.2
(*Category-ranking-dominated verticals*).

**Symptom:** A topic's visibility decomposes into a per-prompt split
that mirrors the brand's third-party ranking position in each
sub-category. Illustrative example — a professional-advisory vertical
(an insurance brokerage, say) with a dominant third-party ranking
body (call it "Contoso Advisory Index"): three topics in the tracked
set each show a middling average (roughly a quarter, two-fifths, and
just under half visibility) but decompose per-prompt into dramatic
tier-gated splits. The quarter-avg topic breaks into ~70% on a
sub-area where the firm holds a Tier 1 ranking and ~0% on a sub-area
with no Tier. The two-fifths-avg topic splits on the same pattern:
~90% on a Tier 1 sub-area, ~0% on an unranked sub-area. The
just-under-half topic shows ~75% on a Tier 2 sub-area and ~10% on an
unranked sub-area. Each topic average looks like a middling position
but actually describes a Tier-1-or-zero pattern per sub-area.

**Diagnosis:** In ranking-dominated verticals the AI's mental model
of "who's good at X" collapses toward the top tiers of the relevant
third-party ranking for sub-area X. Brand visibility is a near-
deterministic function of ranking position per sub-area, not a
smooth property of the practice as a whole. Topic-level metrics
mask this completely — a 40% topic average could mean "consistently
mid-tier across the practice" or "top-tier in 40% of sub-areas, absent
in the rest", which are materially different strategic positions.

**Action:**

1. Run a per-prompt visibility breakdown on every INVEST /
   borderline topic in Analyse — promoted to core in §13.2 for these
   verticals (the platform companion, §11.19, gives the report call).
2. In findings, report the split alongside the average and identify
   which sub-areas are ranking-backed vs ranking-gap.
3. In Phase B, lead with the topic average and let the per-prompt
   split do the reveal (§14.2 — do not lead with the flattering niche
   stat).
4. Strategy work targets ranking-gap sub-areas as distinct initiatives
   — PR placements, submission to next cycle of the relevant ranking,
   content that signals category authority to the ranking reviewers.
   Pouring generic content into the topic as a whole will not move
   the sub-area that's invisible; the pattern is sub-area-specific.

**Confirming diagnostic — platform-mention mining (§13.10).** The
decomposition above infers ranking-dominance from outcome metrics;
fanout query text can prove it one level earlier in the causal chain
(on a tool that exposes query fanout). Grep the fanout queries for the
vertical's candidate ranking bodies by name — a high named-source share
(e.g. ~20%+ of all fanout queries naming the same one or two
directories, with tier vocabulary and year qualifiers) confirms the
engine literally searches the ranking bodies before answering, and
identifies exactly which bodies gate visibility. That narrows step 4's
submission/PR targets to the named bodies rather than the long tail of
directories. See §13.10 for the procedure.

**Reporting implication:** Phase B attribution should disclose that
a single-firm (or single-brand) project in a ranking-dominated
vertical is inherently biased toward the own brand's focus sub-areas
(§14.14). The #1 position this project reports describes "most
coverage within our chosen sub-areas"; a firm measured against its
own sub-areas would show a different picture.

### 11.20 Different page types earn citations via different recipes

**Symptom:** A "what makes a high-citing page" pattern surfaced from
analysis on one page genre (e.g. expertise / service-line pages of a
professional-services firm) gets applied as a generic improvement
recipe across the entire site, including page genres where the recipe
doesn't fit. The most common failure shape is to derive a recipe from
a high-citing **expertise page** and then evaluate every page through
that same recipe — at which point a high-citing **insights hub** page
looks like it's "missing" the recipe ingredients even though it's
outperforming the expertise pages on citation rate.

**Diagnosis:** AI engines treat different page genres as different
classes of evidence. The features that make an expertise page citable
are not the features that make a hub page citable, and not the
features that make a comparison-style listicle citable. Each genre
has its own citation recipe; conflating them produces wrong actions.

Three observed recipes (illustrative — not exhaustive):

- **Expertise / service-line pages.** Specific quantitative claims
  with named sources: engagement or case counts with attribution,
  named awards with years, named industry-ranking tiers, attributed
  client / partner quotes, service-specific named expert counts. The
  mechanism is "the page contains hard evidence the engine can lift
  verbatim."
- **Insights hub pages.** Strong positioning at the top, structured
  sub-topic framing (named pillars, value-chain breakdown, taxonomy
  diagram), and large content-cluster depth (50+ regularly-updated
  publications, organised by named sub-topic). The mechanism is
  "the page reads as the canonical entry point to a topic the brand
  owns at depth."
- **Comparison / listicle / "best of" pages** (typically
  third-party). Multi-brand coverage with consistent attribute
  structure across entries (price, feature, rating, year, named
  reviewer). The mechanism is "the page reads as a structured
  reference table the engine can sample from."

**Action:**

1. **Classify the page first, then apply the recipe.** Before
   attributing a page's high or low citation rate to any specific
   content element, classify the page genre. Use the recipe for
   that genre as the comparison baseline, not the recipe from a
   different genre.
2. **Don't recommend recipe ingredients from one genre on a page of
   a different genre.** "Add specific engagement counts to the
   insights hub" is the wrong recommendation; the hub doesn't fail by
   lacking engagement counts, and adding them won't move citation
   rate. The right recommendation is "deepen the content cluster" or
   "tighten the pillar framing", per the hub recipe.
3. **In Phase B side-by-side comparisons across page genres, frame
   the contrast as different recipes, not different scores.** A
   slide that compares an expertise page (citation rate around 1×)
   and a hub page (around 1.8×) should explain *why each is
   citable* (different mechanism) rather than treating one as the
   baseline and the other as the gap.

**Anti-pattern.** Surfacing a content-element pattern from one
high-citing expertise page (e.g. "this service-line page has named
ranking tiers and attributed quotes; that's the recipe") and then
listing the same elements as "missing" on a high-citing hub page on
a comparison slide. The hub page isn't missing them — it's earning
citations through a different mechanism. The comparison slide reads
as a critique of a page that is in fact outperforming the page being
held up as the recipe source.

**Reporting implication:** When a deck includes a side-by-side
comparison of two pages with different citation rates, classify both
pages by genre before attributing the rate difference to specific
content elements. If the genres differ, the rate difference may not
be a content-recipe gap at all — it may be a different recipe
working at a different intensity, which is a different strategic
implication.

### 11.21 Educational opener produces an essay in which no brand is named

**Symptom:** A cluster of prompts opening with "What is …", "How does
… work", "Explain …", "Difference between … and …" (or their
equivalents in the market language — "Was ist", "Wie funktioniert",
"Qu'est-ce que", "Analysiere") sits at 0% visibility for every brand
in the roster. Chat inspection shows essays, encyclopaedia-style
answers and Wikipedia citations; no retailer, vendor or provider is
named at all.

**Diagnosis:** The prompt tests AI knowledge, not brand visibility in a
commercial context. "What is accident insurance" shows Wikipedia, not
insurance brokers; "How does a bicycle groupset work" shows an
explainer, not bike shops. The engine has no reason to name a
commercial actor, so the prompt cannot register a mention for anyone
and burns a slot. The failure is almost always an authoring-time
failure: the commercial-intent filter (§4.1 — "does this prompt
measure a question a real customer would ask on the way to a
purchasing decision?") was run after authoring rather than during. In one prior engagement several prompts
were created and deleted inside 48 hours for exactly this reason.

**Action:**

1. **Apply the intent filter at authoring time**, not at the first
   Analyse loop. Ban the educational openers in the authoring brief;
   validate for them before any write.
2. On an existing set, classify each such prompt under §10 "Remove"
   — unless it is a deliberate owned-territory probe (next point).
   Don't confuse this with §11.4 gap-to-close (commercial prompt, brand
   ought to appear) or §11.10 structural zero (category the model
   doesn't associate with the brand).
3. **The deliberate exception: owned-territory probes.** Around 15% of
   the set may probe the informational ground the brand is already
   cited for, tagged `intent:informational` plus a `source:` tag.
   Without them a commercial-only set reads as a flat near-zero line
   and the project cannot answer whether owned authority converts.
   Without the tag they inflate the headline. Both halves matter —
   the probes are allowed only when tagged so they can be excluded
   from commercial KPIs.

### 11.22 Regulatory refusal is not a miss

**Symptom:** Regulated categories (pharma, gambling, alcohol, adult,
regulated finance, weapons and similar) read as systematically worse
than the rest of the set — near-zero visibility for *every* brand in
the roster, not just the own brand. Chat inspection shows responses
that look populated but read as "I can't help with that", "not able to
provide", "recommend consulting a professional", with short bodies and
no topical content.

**Diagnosis:** A content-policy refusal is a different outcome from a
brand not being mentioned. Aggregate metrics count both as
"no mention", so the regulated cohort's denominator fills with chats
in which no brand could ever have appeared. The absence is structural,
not evidence-based: a refusal means the engine will never mention the
brand regardless of what the brand publishes, whereas a genuine miss
means a competitor got the mention instead. Some engines refuse far
more than others on the same prompt, so the effect is also
engine-skewed.

**Action:**

1. Tag the affected prompts `regulatory:restricted` (the same tag as
   §11.7) on day 0, so refusals can be separated in every report.
2. In regulated verticals, sample at least 8 chats per engine on
   regulated-category prompts to estimate the refusal rate before
   relying on that engine's data for strategic conclusions.
3. Filter refusals out of visibility / SoV denominators. They are
   neither parametric (§11.13) nor retrieval — they are a third state
   with a different strategic meaning.
4. The handover or Phase B deliverable must state explicitly that
   `regulatory:restricted` marks prompts where a refusal is not a miss.
   The instruction is invisible in the data and expensive to get
   wrong: if the two outcomes land in one bucket, the regulated
   categories read as systematically worse than they are.

### 11.23 Engine-returned-empty vs brand-not-mentioned (denominator corruption)

**Symptom:** A prompt or engine cohort shows unexplained low
visibility, or a sudden drop on one engine only, with no matching
movement on sister prompts. Chat inspection shows empty or placeholder
response bodies ("No response." or equivalent) rather than a
substantive answer that omits the brand.

**Diagnosis:** "Engine returned empty" and "brand not mentioned" are
different states. The engine didn't fail to find the brand — it failed
to answer. Most platforms' aggregate fields treat the two identically,
so empty responses silently inflate the denominator and depress every
brand's visibility at once. The state is detectable only by reading the
chat payload. Three look-alikes must be kept apart:

- *empty body* — engine failed to answer (this pattern);
- *populated body, empty source list* — engine answered from parametric
  memory (§11.13);
- *populated body that is a refusal* — content-policy decline (§11.22).

An engine-wide outage looks like this pattern across many prompts on
the same engine and day; sister prompts from the same project, engine
and day answering normally rule the outage out.

**Action:**

1. At Intake, ask whether the platform can distinguish "engine
   returned empty" from "brand not mentioned" (see the platform
   companion, §11.23). If it cannot, build the spot-check into every
   Analyse loop: for low-visibility cohorts, sample chat payloads and
   classify each into the three states above before drawing
   conclusions.
2. Exclude empty-response chats from the denominator when reporting
   the cohort, and say so in the deliverable.
3. Where a single engine produces empties disproportionately, report
   that engine's visibility with the caveat rather than averaging it
   into the headline (§11.11).

### 11.24 Translated prompt set masks market-specific demand

**Symptom:** A second market's prompt set is a translation of the
first market's set — same allocation, same phrasing, same product
vocabulary. The second market's visibility line is flat or reproduces
the first market's pattern exactly, and nothing in it answers a
question the client has about that market.

**Diagnosis:** Copy-pasting translated prompts into another language
misses market-specific demand: category names, price anchors, seasonal
peaks, the brands people compare against, and the intents that carry
revenue all differ per market. A translated set measures how the brand
shows up for the *first* market's questions asked in a second language
— which nobody asks.

**Action:**

1. Author an original set per market in native phrasing, from that
   market's own data sources (§8), not by translation.
2. Run the cross-market divergence check before reusing an
   allocation: if revenue or demand distribution across categories
   differs materially between markets, derive independent allocations
   and record that the check fired.
3. Keep the tag vocabulary and topic structure shared across markets
   so cross-market reports remain comparable — it is the *prompts*
   that must be native, not the taxonomy.

### 11.25 Phrasing-variant bloat (and the deliberate-twin exception)

**Symptom:** Several prompts differ only in wording — "accounting
software cost", "how much does accounting software cost", "accounting
software price" — and a near-duplicate sweep across the merged set
flags them. Breadth is lower than the slot count suggests.

**Diagnosis:** Variants at the prompt-set layer buy nothing: the
platform re-runs prompts on a schedule, so non-determinism is handled
at the measurement layer. Three phrasings of one intent are one prompt,
not three (the wildcard principle — §4.1 quality over quantity), and
each duplicate costs a
slot that could carry a distinct intent. When authoring is delegated to
parallel authors the problem compounds: two authors given the same
source anchor independently write the same prompt, and no per-batch
self-check can see it.

**Action:**

1. Run a token-similarity near-duplicate sweep across the **whole**
   merged set, not within batches — cross-batch duplication is a global
   property and is unverifiable from inside any slice.
2. Treat a high-similarity pair as a **decision to make, not an
   automatic defect**. A deliberate branded / unbranded twin ("what's
   the best beginner road bike?" against "is *brand X*'s beginner road
   bike any good?") scores high on token overlap and is exactly the
   comparison the set exists to make. Read every flagged pair; merge
   the accidental ones, and record the deliberate ones so the next
   run does not re-litigate them.
3. Reallocate the freed slots to distinct intents under the approved
   allocation (§9).

### 11.26 Competitor-blind prompt set

**Symptom:** The set is almost entirely unbranded category queries.
Reports can say whether the brand appears, but not against whom it
loses; share-of-voice and gap reports carry no head-to-head signal, and
the Phase B deliverable has no competitive narrative.

**Diagnosis:** The competitive dimension was forgotten at authoring.
Unbranded category prompts measure presence; they do not measure
comparative positioning, and they never surface the alternatives the
engine steers users toward.

**Action:** Include head-to-head comparisons ("[own brand] vs
[competitor]"), best-of lists ("best [category] providers"), and
alternatives queries ("[competitor] alternatives") in the allocation,
each tagged under the brand-mention split (§4.10, §9.7) — `branded`
where the own brand is named, `other-brand` where only a competitor is
named, `non-branded` for best-of lists — so none of them blends into
the wrong KPI. Size the cluster from the
roster (§9.3): every tracked competitor should be reachable by at least
one comparative prompt.

### 11.27 Invented vocabulary in prompts

**Symptom:** Prompts name products, models, ranges or brands that the
client does not stock or that do not exist ("best [brand] carbon
gravel frame" for a brand that sells no gravel bikes). Visibility on
those prompts is zero for structural reasons, and the client questions
the set's credibility on first review.

**Diagnosis:** The prompts were authored from assumption rather than
from data. Product, range and brand names must come from the client's
own data (catalogue, analytics, search-console queries, sitemap — §8).
Never invent them, and never assert what the client stocks beyond
what the data shows.

**Action:** Build a vocabulary list from the intake sources before
authoring and hand it to every author with the brief. At validation,
check every named entity in the set against that list; anything not on
it is a defect to correct, not a caveat. Where the vocabulary is
genuinely uncertain, use the AskUserQuestion tool to confirm with the
user rather than guessing.

---
