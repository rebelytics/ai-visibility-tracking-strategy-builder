---
name: ai-visibility-tracking-strategy-builder
description: 'Build or refine an AI visibility tracking strategy — the prompt set, grouping structure, brand roster and reporting split that measure how a brand appears in ChatGPT, Gemini, Perplexity, AI Overviews and similar — on any AI visibility monitoring platform. Runs as an iterative loop (Intake → Strategy → Write → Analyse) with an optional stakeholder presentation once the strategy has stabilised. Load whenever the user mentions AI visibility, GEO (generative engine optimisation), AI brand monitoring, prompt tracking, "what prompts should we track", "how are we showing up in ChatGPT / Gemini / Perplexity", AI mention tracking, a prompt set for an AI monitoring tool, or a tracking strategy review. This is the platform-agnostic core of a skill family: load it together with the companion for the platform in use (Peec AI: `peec-ai-tracking-strategy-builder`; SISTRIX: `sistrix-tracking-strategy-builder`), or alone for any other tool.'
version: 1.2.0
license: CC-BY-4.0
origin: https://github.com/rebelytics/ai-visibility-tracking-strategy-builder
maintainer: Eoghan Henn / rebelytics (eoghan@rebelytics.com)
---

# AI Visibility Tracking Strategy Builder

**Created by Eoghan Henn / [rebelytics.com](https://www.rebelytics.com)**

An end-to-end workflow for taking a brand from "we should be tracking how
AI assistants talk about us" — or "our tracking project no longer fits our
strategy" — to a measured, well-structured tracking strategy that reflects
commercial reality, on whichever AI visibility platform the brand uses. The
skill runs as an iterative loop (Intake → Strategy → Write → Analyse) that
produces concrete configuration changes and findings each pass, with an
optional terminal phase for a stakeholder presentation once the strategy
has stabilised.

This is the **platform-agnostic core** of a skill family. Everything here
is true of building a tracking strategy on any platform; field names, API
mechanics, plan-tier quirks and import formats live in a **platform
companion** (§5). Load the core and the companion together.

> This skill is a **living document**. If you run it and discover a pattern
> that isn't captured, open an issue on the repo. See the contributing-back
> section at the end of this file.

## Licence

Released under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
licence. You are free to share and adapt this skill for any purpose,
provided you give appropriate credit to the original author.

## Feedback & Support

If you run this skill and find methodology gaps, gotchas, or patterns
worth contributing, open an issue on the
[GitHub repository](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder).
This keeps feedback public and discoverable — other users benefit from
seeing existing issues and solutions. For direct contact, reach the
skill's creator, Eoghan Henn, via [rebelytics.com](https://www.rebelytics.com).

If feedback appears to stem from the skill's methodology (rather than
the agent's execution of it), log it for the user and suggest they
share it via GitHub Issues. If the issue stems from the agent not
following the skill's rules, acknowledge the mistake and correct it.

---

## 1. What this skill is (and isn't)

**Is:** A layered, prescriptive workflow that takes a brand from platform
access to a tracking strategy that's live, documented, and explainable to
a stakeholder. Runs as an iterative loop (Intake → Strategy → Write →
Analyse) so the strategy gets sharper each pass. Covers both **new
projects** (no prompts yet) and **existing projects** (prompts already in
place that may need rationalising). The agent decides which path to take
by inspecting the project's current state, not by asking.

**Two classes of deliverable:**

- **Mandatory:** the configured tracking project itself — brand roster,
  grouping structure, tags and prompts, written directly through the
  platform's API where one exists (see §14.16 for platforms that only
  take an import file). Written as Phase A loops produce them.
- **Optional (Phase B, terminal):** a stakeholder-facing presentation of
  the strategy and its findings. The agent should proactively offer this
  after the first full Phase A loop completes (see §14.5), rather than
  waiting for the user to ask. Produced once at the end of the
  engagement; not committed to upfront — see §14.

Working artefacts (intake state, strategy sign-off artefact, findings from
each Analyse loop, verification log) are produced by the workflow but are
not deliverables in their own right. Their format is agent/user choice
(§3.7).

**Isn't:** A platform reference. Tool mechanics, schema quirks, import
formats and setup live in the platform companion (§5), and in the
platform's own MCP/API companion skill where one exists.

**Isn't:** A content strategy skill. A tracking-strategy build surfaces
content and distribution opportunities (community gaps, reference-site
defence, listicle editorial issues) but doesn't execute them. Those land
in the strategy sign-off artefact and any Phase B deliverable for the
content team.

**Isn't:** An analysis-of-results skill beyond what each loop's Analyse
step needs to feed the next Strategy iteration. Ongoing reporting is a
separate concern.

---

## 2. When this skill fires

Trigger when the user:

- Wants to set up tracking for a brand on a newly connected or newly
  licensed AI visibility platform.
- Has an existing project where the brand list, grouping structure, tags
  or prompts need rationalising.
- Says "what should we track", "build our AI visibility strategy", "what
  prompts should we monitor", "fix our tracking setup", "our project's
  structure needs review", or equivalents — on any platform.
- Shops around and an agency pitches "we'd do it differently" — the
  output of this skill produces a defensible set of decisions to
  respond with.
- Asks for a tracking strategy review ahead of a renewal or budget
  conversation.
- Wants a stakeholder presentation for an already-stable strategy
  (Phase B only — the Phase A loops have already produced the strategy in
  an earlier engagement).
- Is about to reuse one market's prompt allocation in another market
  (§9.2 governs; see the cross-market divergence check).

The skill works with any project state: zero prompts, 50 prompts still
finding shape, or several hundred prompts that have grown organically.
The workflow routes automatically based on what it finds.

---

## 3. Cross-cutting principles

These principles apply across every phase and loop of this skill.
Re-read them at the start of each loop before planning work. They're the
rules of the game — phase-specific rules (§§4, 8–15) defer to these when
they conflict.

### 3.1 Instrument separation (branded vs non-branded)

Branded prompts and non-branded prompts measure different things. They're
not two columns of one KPI — they're two instruments with different
purposes. Never aggregate them into a single visibility score, never claim
"the brand leads on branded prompts" as a finding (tautological), and
always report them separately in analysis and strategy. If a combined
metric is requested, produce it only with explicit disclosure that it's an
anti-pattern.

**What each instrument actually measures** (name this in stakeholder
outputs whenever the split appears):

- **Non-branded prompts = commercial visibility scorecard.** These
  measure whether the AI surface names the brand when asked commercial
  questions that don't contain the brand's name. This is the genuine
  discoverability signal and the only valid basis for competitive
  comparison.
- **Branded prompts = reputation / representation instrument.** These
  measure how the AI describes the brand when asked about it by name.
  Visibility on branded prompts is near-tautological (the brand name is
  in the prompt, so the brand nearly always appears in the response);
  sentiment and source authority on branded prompts carry real
  information.

Three hard rules that follow from the split:

1. **Headline metrics split side-by-side.** Never report a blended
   visibility / share-of-voice figure as the primary number. Blended
   figures are dominated by branded prompts — the brand looks stronger
   than it is, and the non-branded competitive picture disappears.
2. **Competitive comparisons exclude branded prompts.** Share of voice and
   position rankings only make sense on non-branded; branded prompts
   systematically favour whichever brand's name is in the prompt.
3. **Sentiment belongs to branded.** Non-branded sentiment is mostly
   noise — most non-branded responses don't name the brand at all.
   Sentiment as a headline metric comes from the branded cohort.

For an intermediary (retailer, marketplace, distributor, agency) the split
is **three cohorts, not two** — §4.10 and §9.7 carry the third case.

Few platforms have a native branded/non-branded concept. The standard
implementation is a **brand-mention tag** set at prompt creation (§9.7);
the companion says what the platform offers.

**Phase B additional rule — the branded visibility number does not
appear.** In analysis contexts (§13), the split-side-by-side rule above
is sufficient because the audience is reading the methodology carefully.
In stakeholder contexts (§14), attention filters captions and leaves
only the numbers behind — a branded visibility figure in the nineties next
to a non-branded figure in the teens, even with a caption reading "branded
measures reputation, not discovery", anchors the stakeholder on the big
number as a success signal. Split-screen framing is not a sufficient guard
against anchoring in a Phase B deliverable.

The Phase B rule is stricter than the Phase A rule:

- The branded visibility figure **must not appear** in any Phase B
  slide — not as a headline, not as a comparison, not in a caption, not
  as a sanity check, not on a methodology slide.
- The non-branded figure appears on its own, named clearly as the
  discoverability score (or equivalent stakeholder-register label, see
  §3.5).
- The branded cohort is acknowledged as "measured separately, reported
  on sentiment and source authority in the branded appendix" (or an
  equivalent one-liner); it is not presented with a percentage.

**An unfiltered brand report silently inflates the own brand against
competitors.** A brand report with no cohort filter returns visibility
computed across **all** prompts in scope — branded and non-branded
combined. The blended figure is mathematically valid for any single brand
individually, but as a **competitive comparison** it is structurally
inflated for the own brand: on branded prompts the own brand scores near
100% by construction while every tracked competitor is measured on the
*same* prompts and scores near 0% (the prompt isn't about them). The
blended roster comparison is asymmetric by construction.

**Hard rule — competitive comparisons.** Any roster comparison (Phase B or
Phase A) filters to non-branded only. Never report an unfiltered blend as
a competitive headline.

**Worked example (composition shape, not just numbers).** An initial deck
reported the own brand at "#1 in category visibility" on an unfiltered
blend across roughly 70 prompts (a small branded slice plus a much larger
non-branded slice). Recomputed on non-branded only, the own brand dropped
several points and was essentially tied with the next-ranked rival. A
different headline. The blend was the own brand's branded ~95% pulling
its figure up, while every competitor's blend was held flat by their ~0%
on the same branded prompts. Competitors had no equivalent inflation
pathway.

This is the same family of error as the §14.2 "summing rates across
brands" hard rule — applied to the **instrument axis** instead of the
brand axis. Both rules generalise: aggregating across two distinct
measurement instruments doesn't just produce uninterpretable numbers;
when one instrument has structural asymmetries between the own brand and
competitors (as branded prompts do), the aggregate silently inflates the
own brand.

### 3.2 Provenance

Every claim in findings must be traceable to a platform read (which
report, which filter, which date window, which cohort). If a claim can't
be traced, it doesn't appear in findings. This is the discipline that
keeps Analyse honest.

### 3.3 Caveats are symptoms, not cover

If a finding requires a caveat to be defensible ("this is strong, but note
that the cohort was only 3 prompts"), the finding is weak — the caveat is
a symptom that the evidence is thin. Either strengthen the evidence,
reframe the finding, or drop it. Caveats shouldn't be used as a rhetorical
escape hatch.

### 3.4 Calendar time is a resource

Measurement windows, cohort age, and signal maturity are real constraints,
not formalities. "We wrote 25 deletes yesterday, let's analyse tomorrow"
is wrong because the cohort hasn't stabilised. Plan loops around the
signal, not the work rhythm. Communicate pacing expectations to the user
at intake (§8).

**Corollary — don't bake in cadences the skill hasn't itself validated.**
Specific review rhythms (30-day, 90-day, monthly) should be described as
user-configurable defaults with the rationale exposed, not hard-coded as
skill prescriptions. If the skill's validation timeframe hasn't covered
multiple cycles at the prescribed cadence, treat it as a hypothesis the
user can adjust, not a finding. Phrase cadence language accordingly
("Users typically review monthly; confirm what works for your team")
rather than as a rule ("Reviews happen monthly").

### 3.5 Audience separation

The agent's internal reasoning, the user-facing sign-off, and the Phase B
stakeholder deliverable are three different audiences with three different
registers. Don't leak internal methodology language into stakeholder
decks; don't leak stakeholder simplification into agent reasoning.

### 3.5.1 Structured-question register rules

> **Tool note.** "AskUserQuestion" is the structured multi-choice user
> prompt used by Claude. Other agents expose equivalent primitives under
> different names. The rules below apply to any structured multi-choice
> user prompt, whatever the agent calls it.

The audience-separation principle (§3.5) applies to every user-facing
surface, including AskUserQuestion payloads. Skill-internal labels exist
for agent orientation; they must never appear as user-facing option
labels or question text.

1. **Option labels must be outcome-focused, not process-focused.** Prefer
   "I design the strategy, get your OK, then create everything in the
   tool" over "Phase A loop 1 — strategy + writes + verify".
2. **Never use skill-internal jargon in option labels or questions.**
   Forbidden terms as user-facing labels: "Phase A / Phase B",
   "Ring 1/2/3 intake", "strategy sign-off artefact", "disposition
   framework", "prompt disposition", "loop 1", "rationalise",
   "Branch A/B", "quality gate".
3. **Option descriptions should describe what the user will experience**,
   not what the skill's phases do. Good: "You end with a live,
   configured project collecting data from tomorrow." Bad: "Agent
   executes Write sub-phase after sign-off."
4. **When in doubt, assume the user has never seen the skill.** This
   mirrors §3.5 for stakeholder decks but applies during the work, not
   after. The skill runs with the user inside it — they don't benefit
   from the skill-internal vocabulary the agent uses to navigate the
   workflow.

### 3.6 Label travel

Tags, container names, and strategy labels travel across deliverables and
sessions. A tag called `gap-to-close` in the tool needs to mean the same
thing in the strategy sign-off, in findings, and in a Phase B deck. Rename
with care, rename everywhere at once, and document what each label means
in the persisted intake state.

### 3.7 What, not how

This skill specifies what must happen, not how it's presented. Anything
format-dependent (file names, sign-off medium, findings structure, state
persistence mechanism) is agent/user discretion. The skill prescribes
outcomes and gates; users choose their own formats.

### 3.8–3.10 Intake discipline

Intake shortcuts are the strongest failure mode this skill has seen; the
three named skip shapes, the recovery rule (a user-ask, never a
substitution) and the meaning of the intake "rings" are §3.8–3.10 and
live with the intake playbook — **read `references/phase-a-intake.md` in
full at the start of every Intake step.**

---

## 4. Core principles

### 4.1 Quality over quantity

Fewer well-chosen prompts always beat many marginal ones. Every prompt
that doesn't earn its slot costs two things: platform credits or budget,
and analytical noise that obscures signal from the prompts that matter.

The test each prompt must pass: *"Does this prompt measure a question a
real customer would ask on the way to a purchasing decision?"* If the
answer is "only loosely" or "for completeness", cut it. Resist the
instinct to fill whatever ceiling the plan or the user names; propose the
defensible number and document an optional tranche (§9.1).

### 4.2 Every prompt earns its slot

Slots are allocated based on data, not intuition. Demand signals
(landing-page revenue, search-console click share, CPC × volume,
AI-fanout patterns, observed AI citations, customer-voice logs) determine
how many prompts a category deserves. Categories without external demand
signals don't get slots just because the brand offers the product — they
may be a content problem, not an AI visibility problem.

### 4.3 Automated sources first, user asks last

The agent must check what it can already access before asking the user
for anything. The platform's own API or MCP, connected data MCPs
(analytics, search console, SEO tools, commerce platforms, crawl tools),
other loaded skills (brand dossiers, business context), and earlier
conversation context all take precedence. The user is asked for manual
input only as a batched fallback when no automated path exists. When
asking, ask once, ask for the maximum useful batch, and never trickle
questions across the session.

### 4.4 Data persistence

Any data the user provides manually — domain lists, market priorities,
taxonomies, customer-voice samples, regulatory notes — is saved to the
persistence store so the user never has to provide it twice. On
subsequent runs, the agent reads the saved data first, surfaces it to
the user, and asks only whether it needs refreshing. See §7 for the
persistence mechanism (and note that the mechanism itself is agent/user
choice per §3.7).

### 4.5 Prescriptive strategy, explicit overrides

The Strategy phase outputs a concrete recommendation the user accepts or
rejects — not a menu of options with trade-offs. Each recommendation is
paired with an explicit **"Override this if…"** block that lists the
common departures. The user reads the recommendation, accepts, or calls
out an override. No "which would you like" questions during the strategy
phase.

### 4.6 Brand list reflects reality

Platform-suggested competitor lists are usually wrong — they skew toward
information sites (forums, wikis, magazines) rather than actual
commercial rivals. The real competitors are domains that **actually get
cited** when AI models answer prompts in the brand's space. On day 0,
derive the competitor list from the brand's own commercial knowledge
plus any available SERP-competitor or citation data. On existing
projects, derive it from the platform's domain and URL citation reports.

**Three categories, not two.** The brand roster has three shapes, not
the binary "competitor vs marketplace noise":

1. **Commercial competitor** — a distinct business the own brand is
   fighting for the same customer's wallet. Add to the roster as a
   competitor; it will drive share-of-voice, gap reports, and
   competitive narrative.
2. **Assortment brand** — a brand stocked *by the own retailer* (it
   appears as a product line or brand page on the own site). Retailing
   the brand does not make it a competitor; conflating the two inflates
   competitor counts and corrupts gap analysis. Assortment brands can
   still matter for visibility tracking (a user searching for the brand
   may land on the retailer) but should be **tagged as assortment** so
   the Strategy-phase output surfaces them distinctly.
3. **Marketplace / generic noise** — large marketplaces, shopping
   engines, generic directory pages. Not a competitor; not stocked; just
   co-retrieval noise.

§9.3 codifies the classification step to run before adding any brand
to the roster, and how assortment brands map to the grouping structure.

### 4.7 Tags serve analysis, not categorisation

A tag taxonomy should be 2–3 dimensional (intent × funnel × category is
a common shape) and total 15–25 tags. More than that and consistency
breaks down. Every prompt should carry at least one tag from each
dimension. Avoid tag-dimension duplication (a `transactional` tag and a
`funnel:decision` tag are the same signal — pick one).

### 4.8 Containers mirror business structure — cardinality decides the rest

Every platform offers some **single-valued grouping field** (a brand, a
topic, a cluster — the companion names it) and usually a **multi-valued
tag field**. The single-valued container is the coarse grouping used for
dashboards and reporting. It should map to the brand's internal structure
so stakeholders can find their area. Don't duplicate categorisation
between containers and tags — let containers carry business structure and
tags carry cross-cutting dimensions.

**Cardinality is what settles the container-versus-tag question.** A
single-valued field can only ever hold the one dimension that genuinely
*partitions* the set — so the container must carry the dimension the
budget is allocated against and that stakeholders own internally,
normally the commercial category. Every dimension that *overlaps*
categories (funnel stage, intent, seasonality, regulatory sensitivity,
diagnostic status, brand-mention type, assortment brand) has to live in
the multi-valued field or be lost, because multi-membership is
expressible nowhere else. The question is never "containers or tags" —
it is which dimension goes in which field, and the answer follows from
how many values the field holds. Where a nested sub-level exists, it must
subdivide its parent, never act as a second independent axis: two
orthogonal axes nested in one field cannot be filtered apart afterwards.
§9.4 works this through for the three field shapes platforms actually
expose.

5–8 containers covers most single-market e-commerce projects; more than
10 usually signals either multiple markets mashed together or containers
acting as tags. **Containers are categories, not brand names** — a
competitor's name belongs on the brand roster, never as a container.

### 4.9 Engine coverage matches the audience

Every tracked engine multiplies chat count and cost. Match engines to
where the audience actually asks — and don't default to "all engines".
Some platforms gate the engine set by plan tier; there the question flips
from "which engines" to *"am I getting maximum signal from the engines I
do have?"* — a prompt-quality and brand-detection-hygiene question. The
companion says how to detect the plan's engine set (§9.6).

### 4.10 Branded, other-brand and non-branded prompts are different KPIs

This section applies the instrument-separation principle (§3.1) to KPI
reporting specifically — see §3.1 for the underlying rule.

Rolling branded-prompt visibility into overall visibility inflates the
headline number. A project with 10 branded prompts that score near 100%
and 90 non-branded prompts at 10% looks like it has ~20% visibility when
the real "unprompted discovery" visibility is 10%. Branded and non-branded
metrics must be reported separately. Keep branded prompts small in count
(5–10) and consistently tagged so filters work.

**For an intermediary the split is three cohorts, not two.** Before
adopting any brand-mention taxonomy, ask what fraction of the tracked
entity's value comes from entities it does not own. For a single-brand
business the answer is "none" and the binary holds. For a retailer,
marketplace, distributor or agency the answer is "most of it" — an
intermediary's whole business is other people's brands — and the case the
binary loses is the *main* case:

1. **Own brand named** — near-guaranteed mention; the reputation
   instrument.
2. **Another brand named, own brand not** — a rival, or an assortment
   brand the retailer stocks (§4.6). The own brand is *not* guaranteed a
   mention here; it has to be surfaced as a place to buy that brand. A
   hard signal, and for an intermediary frequently the most actionable
   one.
3. **No brand named** — the pure discoverability instrument.

Tag on **who is named in the prompt text**. Whether the named brand
competes or supplies does not change the tag: the same company is often
both, and only "who is named" has a stable answer. Leaving the middle case
undefined guarantees inconsistent labelling — handed a two-value scheme,
parallel authors tag the identical construction both ways, each
defensibly. §9.7 carries the decision and the reporting arithmetic lives
in §13.

### 4.11 Sign-off is the audit trail; verification is the closure

Where the platform has a write API, the skill writes directly to the
project rather than producing an intermediate operations list. The
strategy sign-off artefact — produced before writes begin — is the audit
trail. User sign-off happens before writes begin; verification happens
after, by re-reading the platform state and reconciling it against the
plan (§12). Where the platform only takes an import file, the validated
file is the write and the post-import re-read is the verification
(§14.16).

### 4.12 Fresh prompts need time

Prompts start collecting data within roughly a day on most platforms. The
default iteration pace is daily — the next Analyse loop can run ~24 hours
after writes. For trend-level analyses (share-of-voice shifts, sentiment
drift), 7–14 days produces more stable signal. Don't run Analyse in under
24 hours — the data won't be there yet. See §12.7 for the full
measurement-window guidance and §3.4 on why calendar time is a
first-class resource.

### 4.13 Wildcard over granular

Each prompt should represent a **cluster of related queries**, not a
single exact phrase. AI conversations are personalised — the same person
might ask "best trail running shoes for beginners", "which running shoes
should a beginner buy for trails" or "I'm starting trail running, what
shoes do I need?" These all map to the same intent. Track the
representative wildcard prompt; don't burn prompt slots on variations of
the same question.

**The non-determinism counterargument, and why it doesn't break this.**
Public advice sometimes recommends running dozens of phrasing variations
per priority query because individual AI responses are non-deterministic.
That addresses a different layer. Prompt-set composition (what the
wildcard principle governs) is how a finite budget is spread across the
intents the business cares about; measurement reliability (what the
non-determinism argument addresses) is how confidently any single
prompt's score reflects reality, given stochastic outputs. Mainstream
platforms handle non-determinism **temporally** — they re-run each prompt
on a schedule and aggregate across runs, so a prompt's score is already a
distribution over many samples. Enumerating phrasing variations at the
prompt-set level is largely redundant with what the tool already does,
and it buys depth at the cost of breadth. The one genuine exception is
surgical precision on a very small number of strategically critical
queries — a *supplementary* exercise, never the default framing. If a
stakeholder pushes back with the non-determinism argument, the reply is:
the concern is real, it's handled at the measurement layer, and the
prompt set is optimised for breadth because that's where the business
value is.

### 4.14 Commercial intent filter

Every prompt should be close to a purchasing decision. The test: "If
someone asks an AI model this question and gets an answer that includes
our brand, would that plausibly lead to a sale or enquiry?" Include
"best [product] for [need]", "how do I choose [product]", "[brand] vs
[competitor]", "what does [service] cost". Exclude "what is [concept]",
"history of [topic]", "[acronym] meaning" — unless the business model is
inherently educational, in which case training-intent queries qualify.
The deliberate exception is a small, tagged band of **owned-territory
probes** on informational ground the brand is already cited for (§9.9).
A second, equally deliberate exception is a small **trust / reviews block**
of branded prompts per market (§9.9), included for source diagnosis rather
than measurement — it reveals which third-party review pages and profiles
the engines pull for the brand — and excluded from or reported separately in
the headline visibility figure like any other branded prompt.

### 4.15 Conversational framing

Prompts should sound like how a person talks to an AI assistant, not like
a search-engine keyword. **Good:** "How do I get my bike insured for
racing?" **Bad:** "bike insurance racing".

### 4.16 Market-specific adaptation

The same business may need different prompts per market. Build each
language/market as an independent prompt set: share the container
structure, let the individual prompts diverge on local demand, and
**never inherit an allocation from a sibling market on structural
grounds** — run the cross-market divergence check in §9.2 first.

---

## 5. Relationship to other skills

| Skill | Role |
|---|---|
| **Platform companion** | Required alongside this skill whenever the platform has one. Holds the platform's field names, API/MCP mechanics, plan-tier quirks, import format and platform-only patterns, as "§N — <platform> implementation" parts keyed to this skill's section numbers. Published companions: [`peec-ai-tracking-strategy-builder`](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) (Peec AI) and [`sistrix-tracking-strategy-builder`](https://github.com/rebelytics/sistrix-tracking-strategy-builder) (SISTRIX AI visibility / custom prompt tracking). For any other platform, run this skill alone and treat its import or API contract as the companion's job. |
| Platform MCP/API companion (varies) | Where the platform's tool surface has its own skill (e.g. [`peec-ai-mcp`](https://github.com/rebelytics/peec-ai-mcp), [`sistrix-mcp`](https://github.com/rebelytics/sistrix-mcp)), the platform companion names it. This skill consumes its reads; it doesn't restate tool mechanics. |
| External-data skills (varies) | Any skill the user has for pulling search-console data, SEO-tool data, crawl data, analytics data or AI-citation data. This skill consumes their output; doesn't reinvent them. |
| Brand-context skills (varies) | Any skill the user has loaded that holds accumulated knowledge about the brand being tracked (brand dossier, project-context skill, or similar — however it's named in the agent's environment). Contains prior-captured context (markets, TLDs, revenue profile, regulatory notes) that bypasses intake questions. Always check. |

**How the split works in practice.** Section numbers are global across the
family. When a section here says "the companion gives the platform's
mechanics", the companion holds a part with the same number ("§9.3 — Peec
implementation"). Read the core section first, then the companion part.
Companions never restate a core rule; if a companion appears to contradict
this skill, this skill wins for method and the companion wins for facts
about the platform.

---

## 6. Workflow overview

The workflow runs as **Phase A** (iterative) plus an optional **Phase B**
(terminal). Phase A is where all the configuration work happens; Phase B
is an opt-in stakeholder deliverable at the end.

### Phase A — iterative loop

Each loop runs four sub-phases in sequence:

1. **Intake (§8).** Gather everything the strategy needs. Three
   concentric rings on the first loop, run as parallel paths (§3.10):
   automated tools (Ring 1), a baseline path as the floor (Ring 2),
   and a batched user-provided data ask (Ring 3). Outputs a populated
   intake state, persisted per §7.
2. **Strategy (§9).** Convert intake into a prescriptive recommendation
   with explicit override callouts. User signs off (format agent/user
   choice). Outputs the strategy sign-off artefact.
3. **Write (§12).** Execute the signed-off strategy as direct writes to
   the project via the platform's API — or as a validated import file
   where that is the platform's contract. Outputs a configured project
   and a verification log.
4. **Analyse (§13).** Read what the platform's data actually says after
   the writes have settled. Produce findings (format agent/user choice)
   that feed the next Strategy iteration.

**Loop-awareness.** The **first loop** runs the full three-ring intake
(§8). **Subsequent loops** typically run a platform-only intake refresh —
re-reading current project state — unless findings or the user surface a
gap that needs external data, in which case Ring 2 or Ring 3 is re-entered
for that specific gap. Strategy, Write, and Analyse run every loop, with
scope narrowed to what changed.

**Termination.** Phase A ends when findings no longer produce material
action for the next Strategy iteration — the strategy has stabilised.
That's also when Phase B becomes relevant.

### Phase B — optional, terminal

Once Phase A has stabilised, the agent proactively offers a
stakeholder-facing presentation of the strategy and its findings (see
§14.5 for the timing rules). Phase B is a single pass from existing
Phase A artefacts — it doesn't re-do any Phase A work. See §14 for the
full rules, including why Phase B is intentionally terminal rather than
mid-engagement.

### Routing by project state

Phase A's Write sub-phase routes on project state:

- **New project** (zero prompts at first loop) → first Write is pure
  creates.
- **Existing project** → first Write uses the prompt disposition
  framework (§10) — six buckets covering what to keep, retag, reframe,
  or remove.

Subsequent loops always run in existing-project mode; the disposition
framework is reapplied to the prompts that have been in place long enough
to have meaningful data.

### Pacing disclosure at intake

At the start of the first Intake loop, the agent surfaces the iterative
model and the iteration cadence to the user:

- The default pace is daily iterations — most platforms process new
  prompts within about 24 hours (the companion states the platform's own
  figure), so the next Analyse loop can run the following day (§12.7).
- For trend-level analyses (share-of-voice shifts, sentiment drift), a
  7–14 day window produces more stable signal and can be used when the
  question requires it.
- The number of loops is driven by findings, not by a preset timeline.
- Once the strategy has stabilised across a few iterations, the agent
  can produce a polished stakeholder-facing presentation of the
  strategy and its findings (Phase B, §14). That comes later — first
  the tracking needs to be right. Phase B is not committed to at
  intake, but the user should know the capability exists.

This framing sets expectations before the user has anchored on a linear
"do it once and we're done" model.

---

## 6a. Section map — where to read what

This skill uses progressive disclosure: this file holds the mental model
and the rules that apply on every invocation; the phase playbooks live in
`references/` and are loaded when their phase runs. Section numbers are
global across the family — a cross-reference like "§13.6" resolves via
this map, and the platform companion's map says where its
"§N — implementation" parts live. Every load trigger below is mandatory,
not optional: running a phase without reading its file first is the same
failure shape as skipping an intake ring (§3.8).

| File | Sections | Load trigger |
|---|---|---|
| `references/data-persistence.md` | §7 | When initialising or resuming the project workspace, and before writing any loop artefact |
| `references/phase-a-intake.md` | §3.8–3.10, §8 (incl. §8.5 data-source handling) | In full, at the start of every Intake step, before asking the user for anything |
| `references/phase-a-strategy.md` | §9–§10 (incl. §9.9 prompt authoring, the disambiguation pass and the trust / reviews block) | Before drafting or revising any strategy recommendation, before authoring or delegating prompts, before finalising any prompt set, and before sign-off |
| `references/allocate.py` | §9.1.2 | Run (do not re-derive) whenever the damped revenue-share method leads the allocation |
| `references/pattern-library.md` | §11 | Skim its contents list during every Strategy and every Analyse step; read any pattern whose symptom matches |
| `references/write-and-analyse-principles.md` | §12–§13 (principles, incl. §12.7 measurement windows and run frequency, §13.5 per-answer share) | Before the first Write of a loop and at the start of every Analyse step, and before quoting any visibility figure or making any run-frequency decision — then load the companion's §12/§13 for the platform mechanics |
| `references/phase-b-deliverable.md` | §14 (incl. §14.16 configuration deliverable) | When Phase B is triggered or offered — plus the §14.5 timing check-in at every loop close; §14.16 whenever the platform takes an import file rather than API writes |
| `references/quality-gates.md` | §15 (incl. §15.4 merged-set validation gates) | At every phase transition; the relevant gate must pass before Write, Analyse, or Phase B begins, and §15.4 before any prompt set is written or delivered |

Then the companion's section map for the platform parts of §7–§15.

---

## 16. Output deliverables

### 16.1 Mandatory deliverable

**The configured tracking project itself.** Brand roster, containers,
tags and prompts are live on the platform as the result of the Phase A
Write sub-phase — written through the API, or delivered as the validated
import files of §14.16 where that is the platform's contract. No
intermediate operations list or execution log — the write is the
execution, and verification (§12.5) is the closure.

Each Phase A loop adds to or refines the configured project. The
"deliverable" grows with the loops; there is no single point at which
it's "done" until the user decides Phase A has stabilised.

### 16.2 Optional deliverable

**Phase B stakeholder presentation.** Produced once, at the end of the
engagement, if the user requests it (§14). Format is whatever suits the
audience — a deck, a narrative document, a one-page summary, or
something else. The *that* is optional; the *what* is covered by §14.

### 16.3 Working artefacts

Working artefacts are produced by the workflow but are not deliverables
in the client-facing sense. Their format and storage mechanism are
agent/user choice (§3.7). The skill requires they exist; it does not
require a specific file layout.

- **Intake state.** Whatever format persists the brand config, markets,
  competitors, regulatory context, and data-source inventory (§7.2 is
  one example schema).
- **Strategy sign-off artefact.** The per-loop confirmation of accepted
  recommendations — a markdown document, a structured chat message, an
  interactive list, or a handoff doc (§9.8).
- **Findings.** The per-loop output of Analyse (§13.6). Markdown file,
  chat message, updates to the intake state — whichever fits.
- **Verification log.** The Write-time reconciliation output (§12.6).
- **User-provided data.** Any CSVs, exports, or documents the user
  supplied during Ring 3. Kept so future loops don't re-ask.

In environments without persistent storage, the working artefacts live
inside handoff docs at session end and are re-seeded at session start.
The persistence mechanism is the user's choice; the persistence itself
is a requirement.

---

## 17. Contributing back

This skill improves when users feed patterns back. Two paths:

1. **If you already have a skill-improvement mechanism** (like an
   observer layer that captures patterns across skills), let it do
   its job on your local copy — and when it surfaces something that
   isn't user-specific, open a GitHub issue at
   [github.com/rebelytics/ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder)
   so the open-source version captures it too. Platform-specific
   findings go to the companion's repository instead.

   If you don't have one and want to add one,
   [`one-skill-to-rule-them-all`](https://github.com/rebelytics/one-skill-to-rule-them-all)
   is an open-source observer layer (same author, CC BY 4.0) that
   logs friction and pattern candidates across all your skills as you
   work. Using it with this skill produces the highest-quality
   feedback stream back to the repo.

2. **If you'd rather not install anything**, open an issue directly
   when something lands that would help the next person — a new
   pattern, a gotcha, a workflow refinement, a case where the skill
   steered the wrong way.

Don't fork in-session. Agent-time edits to the skill drift away from
upstream, lose the benefit of other users' patterns, and mean future
sessions load a stale local copy. Feedback → issues → considered
patches → version bump is the path.

---

## 18. Licence & attribution

**Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Reuse, adapt, redistribute — just keep attribution.

**Attribution:**

> AI Visibility Tracking Strategy Builder, maintained by Eoghan Henn
> (www.rebelytics.com),
> github.com/rebelytics/ai-visibility-tracking-strategy-builder.

**Not affiliated with any AI visibility platform.** No platform vendor has
reviewed or endorsed this skill. Recommendations here are based on
observed behaviour across several platforms and may become stale as they
iterate; platform facts live in the companions and carry their own
verification instructions.

Contributions welcome via GitHub. See `CONTRIBUTING.md` in the repo
root.
