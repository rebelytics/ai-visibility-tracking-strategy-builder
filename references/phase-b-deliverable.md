# Phase B — Stakeholder deliverable (§14)

Part of the **ai-visibility-tracking-strategy-builder** skill (CC BY 4.0 — Eoghan Henn / [rebelytics.com](https://rebelytics.com)). Section numbers are global across the skill family — the section map in `SKILL.md` says where each § lives; platform companions extend some sections with their own "Peec implementation" / "Sistrix implementation" parts.

**Load trigger:** Read when Phase B is triggered, offered, or being timed. Two exceptions fire outside Phase B: run the §14.5 proactive timing check-in at each loop close, whether or not Phase B is underway; and read §14.16 before the Write phase on any platform that has no write API (the configuration deliverable replaces the write step there).

**Contents:**

- 14.1 Opt-in timing
- 14.2 Anti-patterns (two-tier severity)
- 14.3 Positive rules
- 14.4 Post-delivery feedback
- 14.5 Proactive timing check-in (each loop)
- 14.6 Pre-build data-surface enumeration (before any slide is drafted)
- 14.7 Composition gate — before any slide is rendered
- 14.8 Cover-slide composition — combine two angles when both hold
- 14.9 Stakeholder-deck attribution — procedural, not personal
- 14.10 Topic-priority claims — external backing required
- 14.11 Topic-to-shop-category mapping (ecommerce recipe)
- 14.12 Reviewing the tracking platform's own recommendations — surface where the strategy improved on the tool
- 14.13 Closing-slide — strategy commitments, not tool dependence
- 14.14 Single-firm focus-area bias disclosure
- 14.15 Phase B data-to-deck handoff format (for subagent delegation)
- 14.16 Configuration deliverable for platforms without a write API

**Platform companion pointer:** the rules in this file are platform-agnostic. Before enumerating data surfaces (§14.6), computing a combined-brand figure (§14.2, §14.3), or writing provenance lines in a handoff (§14.15), read §14 in the platform companion — it maps the generic surface names used here (brand report, domain/URL citation report, per-engine breakdown, chat-level reading, the platform's own recommendations) to the platform's actual reports, tools and filters.

---

## 14. Phase B — Stakeholder deliverable

Goal: produce a stakeholder-facing presentation of the tracking strategy
and its findings. Phase B is **optional** and **terminal** — it runs
once Phase A has stabilised, at the user's request, not before.
Pre-committing to Phase B at intake risks ossifying the narrative
(§11.12).

### 14.1 Opt-in timing

- At **intake** (§8), acknowledge Phase B exists as an option at the
  end of the engagement. Don't ask for a commitment.
- At **end of Phase A** (once strategy has stabilised across one or
  more Analyse loops), offer Phase B as a discrete next step: "Strategy
  is done — do you want a stakeholder presentation?"
- If the user says yes, Phase B runs as a single pass from existing
  Phase A artefacts.

"Stabilised" is a soft term; the concrete signal is §13.6 — findings
no longer produce material action for the next Strategy iteration.

### 14.2 Anti-patterns (two-tier severity)

*Never (hard rules):*
- Tautological findings (§13.3).
- Aggregating branded and non-branded into a single metric without
  explicit "this is an anti-pattern" disclosure (§3.1).
- **Summing visibility, SoV, or any chat-share metric across
  brands.** A single chat can mention multiple brands simultaneously,
  so these metrics overlap and cannot be summed. "Own brand 35% +
  sister brand 31% = group 66%" is mathematically wrong — the
  answer is *somewhere between 35% and 66%*, and the only way to
  compute the actual group figure is to re-query the underlying
  chat set with both brands filtered into one call (a combined-brand
  filter on the platform's brand report — see the platform companion
  for the exact call) or to union the chat ID sets directly. The
  same rule applies to mention rates, retrieval share, citation
  share, and any rate metric whose denominator is "chats in scope".
  Sentiment and position are per-mention aggregates and don't have
  this overlap problem; the ratio metrics do (the platform companion
  lists which of the platform's metrics are ratio metrics). The
  failure mode is attractive because the sum stays below 100%, so
  it doesn't trip any obvious plausibility check — the rule has to
  be a hard "never".

  *Worked anti-example (composition shape, not just language).*
  Building a competitive bar chart for a brand family. Pulled own
  brand around 20% and sister brand around 22% from the platform's
  brand report. Computed the sum in head, drew a third bar labelled
  "Group: ~42%". The chart composition itself is the failure shape —
  any "combined" / "group" / "family" bar drawn by arithmetic
  addition triggers this rule. The rule fires on the *bar*, not just
  on the language. Correct shape: list each brand as its own row, no
  combined bar. If the stakeholder needs a group figure, run a
  single combined-brand query on the platform (or a manual chat-ID
  union) and label the result as a single combined-brand query, not
  as a sum.
- **Trend or time-series visualisation across a window in which the
  tracked prompt set changed.** Day-over-day line charts of
  visibility, SoV, position, sentiment, retrieval share, etc. assume
  a stable prompt cohort: the metric's denominator (chats in scope)
  is governed by the tracked prompt set, and any prompt creation,
  prompt-text edit, or prompt deletion inside the window changes
  that denominator mid-flight. The chart then visualises a
  measurement-shift artefact, not a real movement. Same logic as
  the rate-summing rule applied to the time axis — rates with a
  changing denominator across time can't be plotted as a continuous
  trend. Either truncate the chart to the longest sub-window where
  the prompt set was stable, or drop the trend visualisation and
  use snapshot metrics only. See §13.6 (prompt-set-stability check)
  and §13.7 (stable-cohort gate). Cross-loop deltas inherit the
  same constraint.
- **Contrasting AI search with Google when any Google-family engine
  is on the tracked roster.** AI Mode, AI Overview, and Gemini are
  part of what's being measured. Any "AI search, not Google"
  framing (in German: "KI-Assistenten, nicht Google"; in English:
  "AI assistants, not Google") is factually wrong when two of the
  three engines on the deck ARE Google. Use "classical search",
  "traditional search", "klassische Suchmaschinen", "legacy SERP"
  instead — the contrast is AI-era search experiences vs the blue-
  links SERP, not AI vs "the company Google". Before drafting any
  explainer slide that contrasts AI search with something else,
  read the engine roster (see §14.3) and pick contrast language
  consistent with what is actually measured. The rule
  generalises: any binary framing "X, not Y" — Y cannot be a name
  that appears inside X's measurement scope.
- **Lead with the flattering niche stat when a topic has a dramatic
  per-prompt split.** When a topic's per-prompt breakdown reveals a
  large spread (e.g. above 90% on a niche sub-prompt, near 0% on a
  broad sub-prompt, averaging around 40%), the slide's lead number
  must be the topic-level figure — the 40% — and the split must be
  revealed in supporting cards or body. Leading with the 90%+
  figure buries the harder story, breaks parallelism with sibling
  "beneath the average" slides in the same deck, and invites
  challenge when the stakeholder cross-checks the topic-level
  number elsewhere. The niche figure still appears — as the reveal,
  not the lead. Exception: single-prompt topics where there is no
  split to reveal (e.g. a standalone "Insurance 76%" headline). See
  §14.10 on topic-priority claims and §11.19 on the
  category-ranking mirror pattern that produces this shape.
- **Showing the branded visibility number in any form** — headline,
  comparison slide, caption, methodology slide, sanity check. Phase
  B reports only the non-branded figure, named clearly as the
  discoverability score; the branded cohort is acknowledged as
  "measured separately, reported on sentiment and source authority
  in the branded appendix" (§3.1 Phase B rule).
- **Reporting an unfiltered brand-report blend as a competitive
  headline.** The platform's brand report, run without a
  branded/non-branded filter, mixes branded and non-branded prompts.
  For competitive comparison, this silently inflates the own brand
  relative to every tracked competitor — every competitor is
  measured on the same set of branded prompts about the own brand,
  where they score ~0% by construction (the prompt is about the own
  brand, not them). The blended figure is therefore not a clean
  roster comparison and must never be the headline of a competitive
  slide. Always filter to non-branded only for roster comparisons.
  This is the §14.2 sibling of the rate-summing rule — both apply to
  aggregating across distinct measurement instruments with
  structural asymmetries between the own brand and competitors. See
  §3.1 for the worked example.
- **Presenting a per-question at-least-once count as visibility.**
  "Present in N of M questions" counts prompts where the brand was
  named in *any* answer over the window; it is an upper bound on the
  share of answers naming the brand, and it flatters badly — on one
  observed set, 77% by question against 41.6% by answer over the same
  prompts and window. The stakeholder figure is **"named in x of N
  answers"**, with the answer count and the window in the caption.
  A per-question figure appears only when explicitly labelled as
  at-least-once and placed beside the per-answer share, never as a
  headline, and never in a per-grouping or per-market breakdown that
  decides where effort goes. Where the platform's API exposes only the
  flag, the per-answer figure comes from wherever the platform does
  publish it — see §13.5 and the companion's §13.
- **Internal methodology vocabulary in any stakeholder-facing
  surface.** Off-limits as terms of art: "rig", "instrument",
  "dimension" (as the skill's five axes), "Phase A / Phase B",
  "loop", "Ring 1/2/3", "non-branded cohort", "branded cohort",
  "analyse phase", "write phase". Replace with plain-English
  equivalents appropriate to the audience — "the setup", "what we
  measure", "the signal streams", "iteration", "brand-name prompts",
  "category prompts", "the review", "updates to the setup". If a
  slide would only land with someone who had read the skill file, it
  is the wrong slide for a stakeholder.
- **Methodology-proving content as a primary slide.** Blind-spot
  case studies, "here's how the setup catches its own errors",
  "here's where every number comes from" provenance tables, "how
  the setup evolves" narratives — all are Phase A artefacts. They
  belong in back-pocket / Q&A, not in the body of the deck. If the
  stakeholder asks, have the answer ready. Don't spend a primary
  slide on it.
- **Structure-only or process-only slides.** "Here's how the setup
  works" is not a slide. "Here's how the setup works, and the one
  decision in it that made finding X possible" is a slide. Every
  structure / process / data-source slide must pair architecture
  with a specific audience-relevant finding. A good positive
  example: a data-source breadth slide listing every platform data
  surface used (domain citation report, URL citation report, the
  platform's own recommendations, fanout mining, chat content
  analysis) paired with the one concrete finding each surface
  produced — structure-with-insight and serves as a "strategy
  backed by multiple data sources" value prop. The same slide
  listing surfaces without findings is not a stakeholder slide.
- **Tracking-infrastructure work on stakeholder slides.**
  Detection-regex fixes, brand-roster additions, prompt additions,
  topic reorganisations, alias repairs, and any other change to the
  tracking project's configuration belong in the internal findings
  doc, not on stakeholder slides. These are legitimately interesting
  and belong in the findings record so the analyst doesn't lose
  track of what's been done — but they are noise to the stakeholder,
  and worse, they draw attention away from the brand-visibility
  story the deck is supposed to tell. The filter: *if a bullet
  describes a change to the measurement apparatus rather than a
  signal about the thing being measured, it does not belong on the
  stakeholder slide.* Before/after example: "The tracking strategy
  identified and fixed a detection gap within 48 hours — sister
  brand aliases were silently breaking" → drop from deck, keep in
  findings. See §14.3 positive rule "every bullet answers a
  brand-visibility question". Applies equally to primary slides,
  caption lines, footers, and methodology-slide supporting copy.
- Using caveats as rhetorical cover (§3.3).
- Cherry-picking date windows to inflate headlines.
- Leaking internal methodology language into stakeholder register
  (§3.5).

*Avoid unless justified:*
- Round-number windows (e.g. "last 30 days" when signal maturity
  argues for a different cut).
- False precision (visibility=14.3% when sample supports one decimal
  at best).
- Simplification-beyond-reframing (simpler framing for a non-technical
  audience is fine; dropping essential caveats to make the story
  cleaner is not).

### 14.3 Positive rules

- **Provenance preserved** (§3.2). Every stakeholder claim traces back
  to a platform query recorded in the Phase A findings.
- **Label travel intact** (§3.6). Labels used in the deck match labels
  in the tracking platform, the Strategy sign-off, and findings.
- **Audience separation** (§3.5). Register is stakeholder-appropriate;
  internal methodology stays out unless explicitly requested.
- **Read the engine roster before drafting contrast copy.** Before
  any explainer or positioning slide that contrasts AI search with
  something else ("AI search, not X"), list the active engines on
  the tracking project (from the platform's project listing, or the
  roster entry in intake state). Choose contrast language consistent
  with what is actually on the roster. If Google AI Mode or AI
  Overview is tracked, the contrast is with classical SERP /
  "klassische Suchmaschinen", never with "Google". If Perplexity is
  tracked, the contrast is with "traditional search", not "search
  engines" (Perplexity *is* a search engine). See §14.2 hard rule
  on Google-family engines.
- **Topic-average lead on split topics.** When a topic has a
  dramatic per-prompt split (§11.19 category-ranking mirror, or
  any case where best and worst prompts sit more than 40 percentage
  points apart), the slide leads with the topic-average figure and
  reveals the split below. See §14.2 anti-pattern on flattering-
  niche leads.
- **Every bullet answers a brand-visibility question.** For every
  line on every stakeholder slide (including footers and captions),
  ask: *does this tell the stakeholder something about the brand?*
  If the line answers "what did we change about the tracking
  setup?", "what does the measurement apparatus look like?", or
  "how did the tracking itself evolve?", it belongs in the findings
  doc, not on the deck. Stakeholders pay for brand-visibility
  insights, not for visibility into the tracking apparatus. This is
  the positive-rule companion to the §14.2 anti-pattern on
  tracking-infrastructure content, and it generalises beyond any
  one platform: it applies to any analytics engagement where the
  author does both the instrumentation and the reporting.
- **Every named content piece references its URL as a clickable
  hyperlink on the same slide.** Whenever a slide names a specific
  page — own URL, competitor URL, gap URL, listicle, comparison
  site, Reddit thread, Wikipedia entry, authoritative source — the
  page's URL must appear on that same slide as a clickable
  hyperlink. Not just in the findings file, not just spelled out as
  body copy without a hyperlink. The canonical pattern is a short,
  visually distinct line placed near the named page (e.g. *"→
  running-magazine.example/gear/best-running-shoe-brands"* in the
  deck's accent colour, underlined, with `run.hyperlink.address`
  set on the URL run). This turns the deck from a presentation
  artefact into a working artefact: the stakeholder can click
  through to verify any claim, and outreach / content owners can
  act on the slide directly without re-deriving the URL. Use ASCII
  arrow markers (`→ `) rather than the unicode link emoji (🔗) —
  the emoji renders as a tofu box in a LibreOffice → PDF QA pass.
- **Group / family / portfolio shown as one row per brand, never as
  a summed bar.** When a competitive chart needs to display a
  group, family, or portfolio of own brands alongside competitors,
  list each owned brand as its own row. Do not draw a single
  "combined" / "group" / "family" bar from arithmetic addition of
  the per-brand percentages — that violates §14.2 (rate-summing
  hard rule) and the failure shape is the bar itself. If the
  stakeholder needs a single group figure, run a combined-brand
  query on the platform (or do a manual chat-ID union) and label
  the result as a single combined-brand query, not as a sum. A
  footnote on the chart noting *"per-brand rates cannot be summed:
  a single chat may mention more than one"* is the right place to
  surface the constraint to the stakeholder.
- **Every gap-list slide carries a host-classification.** On any
  "where the brand is missing" / "editorial gaps" slide, every
  named target must be classified as one of: (a) third-party
  editorial (independent publisher, trade pub, community site); (b)
  competitor-owned multi-brand listicle (ranks rivals — outreach
  feasibility depends on competitor's editorial policy); (c) other
  (UGC, reference, encyclopaedic). Targets in (a) get plain
  outreach framing. Targets in (b) carry an explicit
  *"competitor-owned"* label so the stakeholder can see the
  conflict was not missed. Targets that don't fit (a) or (b) — most
  obviously, competitor homepages, category pages, and product
  pages — should not appear on this slide at all (see §13.9 host
  classification rule). Filtering happens at analysis time; the
  slide should not be the place where the user discovers the
  filter wasn't applied.
- **Time-series captions name the prompt-set stability window.**
  For any time-series chart in a stakeholder deck, the caption
  states the window over which the tracked prompt set was unchanged
  ("stable cohort: 14 days, no prompt-set changes"). If the prompt
  set changed inside the window, the chart does not appear in the
  deck at all (see §14.2 trend-with-changing-cohort rule); use a
  snapshot metric instead. The caption is not a rhetorical
  caveat — it's the assertion that the chart represents real
  movement rather than an instrument shift.
- **Editorial pitch targets are browser-verified before deck
  inclusion.** Tool-surfaced URL gap targets are signals, not
  actions; promotion to a deck action item requires browser
  verification of all of: (a) brand X is genuinely absent from the
  page (cases (a)/(b)/(c) of the §13.9 brand-detection
  verification disambiguated), (b) the page is open-access — drop
  paywalled sources or frame as visible-snippet targets only,
  (c) the page URL is the right one for the brand's commercial
  positioning (right tier on a tiered industry directory or
  ranking listing — a "top brokers" list with bands, for example),
  (d) the page editorial quality justifies a pitch (vs an
  AI-generated SEO farm). The cost of one browser verification per
  candidate URL is much lower than the cost of presenting a wrong
  target to a stakeholder. Verification belongs **upstream of
  deck-content drafting**, not downstream of stakeholder pushback.
- **No internal artifact references on stakeholder slides.** The
  audience-separation rule (§3.5) applies at the artefact-identifier
  level, not just at the methodology-vocabulary level. Provenance
  discipline (§3.2) and provenance display are different things — the
  audit trail belongs in the working findings artefact, not on the
  stakeholder deck. Methodology slides, footers, and captions must
  not carry platform project IDs, internal findings file paths,
  prompt / brand / tag IDs, session IDs, or workspace paths. Use
  stakeholder-register language: "Source: daily tracking of N
  questions across M engines, P-day window", never "Source data:
  [platform] project [project ID]; queries reproducible from
  findings-YYYY-MM-DD.md". Internal artifact identifiers on
  stakeholder slides are register violations regardless of how
  relevant they feel to the analyst.
- **Terminology consistency across the full deck.** Pick one
  preferred term for each of the 4–6 key concepts the deck depends
  on and use it everywhere. Common drift surfaces: AI engines vs AI
  tools vs AI assistants vs LLMs; branded vs non-branded vs "by
  name" vs category-level; product pages vs category pages vs range
  pages; policy count vs premium volume vs customer numbers. Each
  individual term may be defensible in isolation, but mixed across
  slides it reads as inattention to a stakeholder audience. The
  decision on which term to use is less important than using one
  consistently. Run a grep-based terminology-consistency check on
  every deck before delivery (see §15.3 pre-Phase-B gate).
- **Cover slides land one message.** Pick the single most important
  framing — competitive standing OR opportunity OR baseline OR
  trajectory — and commit. Multi-stat hero compositions belong on
  body slides, where the audience has accumulated enough context to
  absorb the dual angle. The §14.8 combined-cover pattern is for
  internal headline slides, not for the literal cover slide.
  Practical heuristic for picking the cover message:
    - **Trajectory-goal projects** (showing movement over time):
      lead with the trajectory or the change.
    - **Benchmark-goal projects** (showing where we stand today):
      lead with competitive standing, OR the absolute level — but
      not both.
    - **Strategy-update projects** (mid-engagement, showing
      direction): lead with the strategic claim, not the metric.
  A cover's job is to make the audience want to turn to slide 2.
  It's a hook, not a summary. Hooks land cleaner with one message;
  summaries can carry multiple. When in doubt, pick one and trust
  the body of the deck to carry the nuance.

### 14.4 Post-delivery feedback

Accept user edits to Phase B deliverables in place. If a requested
change would soften the methodology or misrepresent findings (e.g.
"drop the branded/non-branded split", "move the bottom line up"),
flag the risk and explain. Don't block — advise. The user is the
decider; the agent's job is to make sure they know what they're
trading off.

### 14.5 Proactive timing check-in (each loop)

§14.1 says "don't ask for Phase B commitment at intake" and "offer
Phase B at stabilisation." Between those two points, which may be
4–8 weeks apart, the skill has historically been silent on timing.
In practice, stakeholder-deck needs are often driven by commercial
triggers (plan-upgrade decisions, board meetings, client sign-off
gates, procurement cycles) that arise mid-engagement and don't
follow the skill's natural stabilisation signal. If the agent waits
for stabilisation before discussing timing, users with compressed
timelines end up having to raise it themselves.

**Rule:** At the end of each Analyse loop's findings hand-off
(§13.6), the agent surfaces Phase B timing proactively. Not as a
sales push — as a routine check that avoids the user having to
raise it. One sentence is enough:

> "Any stakeholder deliverable timeline I should be aware of?
> Stabilisation criteria suggest Loop N+2 at the earliest, but
> commercial triggers can compress that — if so, I can produce a
> baseline+methodology deck sooner with appropriate caveats."

- If the user signals **no commercial trigger**, proceed with
  normal stabilisation-driven timing.
- If the user signals **a compressed timeline**, document the
  trigger (plan gate, board meeting, committed reporting cadence,
  procurement deadline) and produce a deck calibrated to that
  trigger — with explicit caveats about data maturity and likely
  number movement.

**Two deck modes.** Phase B is not one-size-fits-all. The agent
should recognise and name which mode is being produced:

- **Compressed deck (pre-stabilisation):** baseline +
  methodology-focused. Explicit "numbers will move" disclaimer.
  Focus on the strategic framework and what's being measured, not
  on findings. Appropriate when Loop 2–3 and a commercial trigger
  forces it.
- **Stabilised deck (normal Phase B):** findings-focused,
  trajectory-over-time, roster and prompt set treated as stable
  inputs, recommendations derived from several loops of converged
  signal. Appropriate at Loop 4+ once stabilisation gates pass.

**Check-in cadence once a compressed timeline is known.** If the
user flags a compressed timeline at any loop, the agent briefly
confirms Phase B scope at the start of each subsequent session
until the deck is delivered: "Still targeting [date] for the deck?
Any scope change?" This prevents drift and keeps the two parallel
tracks (iterating strategy + preparing deck) from diverging.

**Principle:** Optional terminal phases that depend on user
triggers still need proactive agent prompts at regular intervals.
"Don't ask for commitment at intake" (§14.1) is correct — but the
mirror-image failure mode is "never ask again until stabilisation,"
which makes the skill reactive to commercial realities that don't
follow its timeline. A low-friction periodic check-in neither
pushes for Phase B nor assumes it will never happen. This pattern
generalises: any multi-loop skill with an optional terminal
deliverable should prompt on timing at each loop boundary, not
just at intake and at stabilisation.

### 14.6 Pre-build data-surface enumeration (before any slide is drafted)

Phase A findings files can have blind spots the Phase B build will
inherit unless the gap is broken explicitly. A deck drawn only from
a narrative findings file inherits whatever that findings file
missed — and the cure is a structural enumeration step before
drafting, not more care during drafting. When the user's feedback on
an early draft is "not enough substance," the correct first response
is almost always "which of the platform's data surfaces haven't we
touched?" — not "how do I rewrite what we already have more
punchily?"

**Rule:** Phase B starts with a data-surface enumeration, not a slide
outline. Before any slide is drafted, produce a short table naming
each data surface the platform exposes and whether the engagement
has touched it. Pull the untouched surfaces **before drafting the
deck**, not as enrichment during revision.

Minimum surfaces to enumerate (generic names — read §14 in the
platform companion for the platform's actual report / tool behind
each row, and add any platform-only surfaces the companion lists):

| Surface                                                        | Touched?  | Touched in which loop / artefact?  |
|----------------------------------------------------------------|-----------|------------------------------------|
| Brand report (visibility / SoV / position / sentiment)         |           |                                    |
| Domain citation report                                         |           |                                    |
| URL citation report                                            |           |                                    |
| The platform's own recommendations (mandatory §13.17)          |           |                                    |
| Page-content reading of top gap URLs                           |           |                                    |
| Shopping / product-query surface, where exposed (ecomm)        |           |                                    |
| Query fanout (where the platform exposes it)                   |           |                                    |
| Per-engine chat reading (§13.14)                               |           |                                    |
| Own-brand URL citation map (§13.15)                            |           |                                    |

Any untouched surface is pulled, analysed, and integrated into the
findings before drafting starts. The deck's data backbone is
enumerated-and-pulled, not enumerated-and-hoped-for. Record the
enumeration outcome in the findings file so future sessions inherit
the provenance.

### 14.7 Composition gate — before any slide is rendered

Density constraints get violated because the prose has already been
written by the time the agent sees the render. Density is a
composition-time concern, not a review-time concern. The check must
fire before ink hits the slide.

**Rule:** Before rendering any slide, list every text block the slide
will contain and its intended size. Then reject the slide if any of:

- **More than four text blocks.** (Title, headline, body, caption
  are four. Additional eyebrows, footers, methodology notes,
  attribution, source credits turn a scannable slide into a dense
  one — each feels minor, together they drown the signal.)
- **More than one text block below 14pt.** Source citations, page
  numbers, and legal lines are exempt from the count.
- **URL/domain/entity-as-caption** when the URL, domain, or entity
  name is the slide's main signal. For slides whose primary signal
  is a URL, domain, or entity name, that element must be the
  visual (≥24pt or equivalent prominence), not a supporting
  caption in small type.
- **Fails the 15-second read test in composed-prose form.** Apply
  the read test before the render call, not after.

**Visual PNG inspection (mandatory for multi-column layouts and
non-English labels).** Logic-based layout checks ("will this fit in
the column width I defined") systematically underestimate rendered
width for non-English strings, for compound nouns, and for labels
mixing narrow and wide letters. Visual inspection is the cheapest
reliable check.

After the first render of any multi-column slide, and of any slide
containing labels in languages the agent has not previously
built-to-column-width (German, Dutch, Finnish, Swedish, and other
languages that produce systematically longer strings than English),
convert the slide to PNG (`pdftoppm -r 200` is sufficient) and
inspect for:

1. Text overflow into adjacent columns.
2. Text bleeding past page margins.
3. Baseline collisions with horizontal dividers, separators, or
   arrows.
4. Font-size inconsistency across similar elements.

If any check fails, adjust column widths, font sizes, or line
breaks, re-render, and re-inspect. Do not rely on logic-based
layout checks alone.

### 14.8 Cover-slide composition — combine two angles when both hold

When the data produces two headline angles where each is strong
individually but each leaves a defensible objection unaddressed,
combine them on the cover with a visual divider rather than picking
one or offering the user a menu.

Worked example (illustrative): a specialty-retailer deck could pair
a ranking-gap angle ("Northwind Coffee is #2 — around a point from
#1") with an inverted-headroom angle ("~18% visibility — ~82% up for
grabs"). Ranking alone reads as "we're already winning"; headroom
alone reads as "we're losing". The combined cover tells the real
story: close-to-leader on position, lots of opportunity on volume.

**Rule:** If each of two candidate cover angles independently passes
the defensibility test (§14.9 backing) but each leaves a natural
counter-question hanging, compose a combined cover:

- Top half = ranking / competitive-position statement.
- Horizontal divider line.
- Bottom half = volume / headroom statement.
- Typography: bold heading for each half, with the more surprising
  angle accented. Both halves carry equal visual weight.

Prefer the combined cover over offering the user an A/B/C menu —
menus push composition work onto the user, and the combined cover is
strictly stronger when both halves hold up. Reserve single-angle
covers for cases where the second angle actively weakens the first
or doesn't pass scrutiny on its own.

**Where this pattern applies — body slides, not the literal cover.**
The "combined cover" name in this section refers to *internal
combined-headline slides* in the deck's narrative arc, not the
literal first slide the audience opens to. The combined-headline
composition needs the audience to be already engaged enough to absorb
two messages on one frame — divider lines, "one part / other part"
logic, contrastive typography. The literal cover slide doesn't have
that audience attention yet (it's the first 2-3 seconds), and the
default §14.3 cover-single-message rule applies there: pick one
framing and trust the body to carry nuance. If a deck's narrative
opens with a combined-headline slide, that slide is slide 2 (or
later), not slide 1.

### 14.9 Stakeholder-deck attribution — procedural, not personal

Agency language in stakeholder output carries strategic weight.
First-person attribution ("we filtered", "we declined", "we kept")
frames decisions as personal judgement and invites the easiest
stakeholder counter-move: "that was just your call." Procedural
attribution ("our tracking strategy filtered", "the methodology
kept", "the criteria flagged") makes the decision procedure visible
and shifts the conversation from the consultant's taste to the
rules of the decision.

**Rule:** For any sentence in a stakeholder deck that describes
filtering, keeping, declining, accepting, or otherwise making a
selection decision, attribute the action to the tracking strategy
or the methodology — not to "we" or the consultant personally.

- "we filtered X" → "our tracking strategy filtered X"
- "we declined" → "our tracking strategy declined"
- "we kept" → "the methodology kept" / "our strategy retained"
- "we chose" → "the criteria selected"

First-person is still fine for observational sentences ("we see
X"), interpretive sentences ("we read this as Y"), and
recommendation framing ("we propose Z"). The shift applies
specifically to selection / filtering / inclusion / exclusion
actions.

### 14.10 Topic-priority claims — external backing required

Any topic-priority claim in a stakeholder deck ("these are our four
highest-priority gaps", "these topics represent our biggest
opportunity", "these topics matter most") must be backed by a
signal the stakeholder can verify independently, without the
agent's help.

**Preferred backing sources, in priority order:**

1. **Live product category mapping** (topic → category page on the
   client's own site, with URL). For ecommerce clients this is the
   first-line methodology — see §14.11.
2. **Active SKU count** in the mapped category.
3. **Published brand position or editorial commitment** on the
   client's site or public channels.
4. **External search data** (GSC for the brand's own site; Semrush,
   Ahrefs, or equivalent for competitive volume).
5. **Industry report or analyst coverage** that names the category
   as material.

**What is not sufficient:**

- The platform's own prompt-volume ordinals on their own — where
  the platform exposes a coarse volume rating per prompt, it
  collapses to "low" / "very low" across most commercial topics in
  regulated verticals and doesn't discriminate between priority
  and noise (§13.18).
- Consultant assertion alone ("we decided these matter"). The
  assertion is the conclusion that needs backing, not a backing.
- Visibility or SoV numbers from within the engagement — these are
  the claim, not the evidence behind it.

**If a candidate topic can't be backed by at least one external
source,** downgrade it to an observation, demote it off the
priority slide, or drop it from the deck. The deck's stakeholder
defence rests on backing; unbacked topics are indefensible under
pushback.

### 14.11 Topic-to-shop-category mapping (ecommerce recipe)

For ecommerce Phase B decks, the topic-priority backing in §14.10
has a specific, reusable methodology that is concrete enough to
earn its own recipe: every tracked topic in the deck's priority set
maps to a live product category on the client's site. The mapping
produces a stakeholder-facing defence that reads as "we track these
because you sell these" — a claim grounded in commercial reality
rather than consultant judgement, and verifiable by the stakeholder
in two clicks.

**Recipe (run at deck-build time):**

1. For each tracked topic in the deck's priority set, find the
   matching live product category on the client's site (category
   URL, active product count, visible brand commitment).
2. Verify each mapping by **web fetch** or **a browser tool** —
   don't rely on agent inference from the topic name alone. The
   category must exist, must be live, and must be discoverable
   from the site's main navigation.
3. Record the mapping in a two-column table in the deck: left
   column = tracked topic (stakeholder-register label), right
   column = live product category (with URL, or at minimum the
   category name visible in the site's main navigation). Add an
   SKU count column where the site exposes one.
4. Any tracked topic that fails to map to a live product category
   is a red flag — either the category was removed, the topic
   wasn't aligned with the client's actual commercial footprint,
   or the topic is too generic. Surface these for user review
   before including them in the deck.

The methodology is not decorative. It produces the deck's
defensibility: the stakeholder can verify every mapping in two
clicks, and the consultant-judgement claim "these topics matter"
is replaced by the commercial-reality claim "these topics map to
live categories on your own site."

### 14.12 Reviewing the tracking platform's own recommendations — surface where the strategy improved on the tool

When a slide reviews a vendor tool's recommendations (the tracking
platform's own recommended actions, Ahrefs opportunity scores,
Semrush gap suggestions, etc.), the implicit stakeholder question is
always "what are we paying the consultant for that the tool doesn't
already do?" The KEEP column is the natural surface to answer that
question — it's where the tool was right but the consulting layer
added timing, sequencing, reinterpretation, or prioritisation.
Letting the KEEP column read as pure agreement wastes the answer
space.

**Rule:** On any slide reviewing a vendor tool's recommendations,
the KEEP column should surface at least one callout showing where
the strategy's interpretation improved on the tool's literal
recommendation.

Composition pattern:

- Coloured tint block around the highlighted KEEP item.
- "Tool said: [original recommendation]" in a warning / attention
  colour.
- "Our strategy said: [reinterpreted action]" in the deck's accent
  colour.
- Stacked below the headline KEEP line.

Worked example: the tracking platform's recommendation said
"publish on comparison sites"; the strategy said "join the
affiliate network" (§13.17.4). The reinterpretation is the
consulting layer. Surface it visibly.

**If no reinterpretation exists in the KEEP set** — i.e., every
kept recommendation was accepted as-literally-written — surface
that fact too: "five recommendations kept as written, no
reinterpretation needed." This is better than letting the
stakeholder infer the unasked question. Never invent differentiation
where none exists; say so directly.

### 14.13 Closing-slide — strategy commitments, not tool dependence

A strategy deck is a defence of a direction, not an advertisement
for the vendor tool that was used to build it. Defaults produced by
the agent tend to reference the tool that surfaced the data ("next
[vendor tool] review in two weeks", "next crawl snapshot", "next
rank-tracking update") because that's the natural cadence surface —
but the stakeholder audience may not have made the tool-renewal
decision yet, and a closing that hinges on tool renewal reads as
tool-dependent rather than direction-dependent.

**Rule:** Closing commitments in a stakeholder deck must be phrased
to survive any vendor-tool renewal decision.

- Good: "Four moves. Four measurements."
- Good: "Three priorities. One quarter."
- Good: "[Named outcome] by [date]."
- Weak: "Next [vendor tool] review in two weeks."
- Weak: "Continue tracking via [vendor]."

The tool may be named in earlier slides where its data is the
subject; the closing is where the strategy, not the tool, needs to
be the subject.

**Test:** "If the client decides not to renew [the vendor tool]
tomorrow, does the closing still hold?" If no, rewrite. If yes, the
closing is tool-independent and stakeholder-defensible.

If the vendor tool's ongoing use is a firm commitment (contract
renewed, budget locked, included in a multi-year agreement), the
tool can be named in the closing — but confirm that commitment
status before defaulting to a tool-dependent close. Default to
tool-independent phrasing when the renewal status is unknown.

**Closing commitments must be outcome-shaped or backed by booked
timing.** Alongside the tool-independence rule, the closing slide
must pass a cadence-commitment test:

- **Outcome-shaped (always safe):** "Five moves. Five measurements.",
  "Three priorities, one quarter.", "[Named outcome] by [result]".
- **Timing-shaped (only when booked):** "Next review: 14 May, as
  agreed." — the date must be in writing in the engagement scope
  (contract, kickoff notes, or a confirmed follow-up booking).
- **Weak (avoid):** "Next analysis in 7 days.", "Trend data by
  early May.", "We'll review monthly." These phrasings commit the
  agent (and the client relationship) to cadences that nobody has
  explicitly agreed. The skill's internal iteration cadence (§12.7,
  §13.7) is an agent-side working assumption, not a stakeholder
  commitment, and it must not leak into deliverables as a
  time-bound promise.

**Test:** "If we don't actually run that analysis on the promised
day, will the stakeholder think we missed a commitment?" If yes,
drop the timing or replace with outcome language. Closings are the
highest-stakes slide for inferences-from-language — small phrasings
like "the next" or "in 7 days" land harder than the same words mid-
deck.

### 14.14 Single-firm focus-area bias disclosure

**Applies to:** Phase B decks for single-firm or single-brand
tracking projects — any engagement where the prompt set was built
to cover what *this* brand sells or does, and where the stakeholder
audience might interpret a "we rank #N" claim as a market-wide
ranking.

**Issue:** Single-firm tracking projects produce a visibility figure
that is, by construction, biased toward the own brand's chosen
market. The prompts cover the brand's practice areas, product
categories, service lines — not an unbiased sample of what
competitors focus on. When such a deck reports "we're #1 of N
tracked competitors at X%", the unstated assumption is that the
comparison is fair across all N competitors' business lines. It
isn't: competitors measured against *their* own focus areas would
likely show different — possibly higher — numbers. Without
disclosing this, the #1 claim reads as "we're the best firm /
retailer / provider in the vertical" when it actually means "we
cover our own chosen market best among these tracked competitors."

**Rule:** Every headline visibility slide in a single-firm deck
carries a procedural focus-area-bias disclosure. Suggested
language (adapt to register):

> *"These figures reflect [brand]'s focus areas. Other [firms /
> brands / retailers] measured against their own focus areas would
> show different visibility pictures — this is a measure of
> [brand]'s coverage of its chosen market, not an absolute
> [industry] ranking."*

Place as body-text / italic note directly beneath the headline
stat. This is a procedural caveat (§14.9 procedural attribution),
not a weakening hedge. The purpose is to turn an indefensible
absolute claim ("we're #1 in our vertical") into a defensible
relative one ("we have the strongest coverage of our chosen market
among the N firms this project tracks"). Defensibility under
stakeholder cross-examination is the test.

**Does not apply to:** multi-brand portfolio projects where the
prompt set deliberately spans multiple brands' focus areas, or
portfolio-level reporting where the scope is explicitly stated as
cross-industry. The disclosure is specifically for the shape where
one brand's business defined the prompt universe.

**Pair with §11.19 category-ranking mirror** in ranking-dominated
verticals: the focus-area disclosure is additional protection
against the natural but misleading inference that the brand's
visibility is a market-wide quality signal rather than a coverage-
of-chosen-niches signal.

### 14.15 Phase B data-to-deck handoff format (for subagent delegation)

Phase B deck composition is commonly delegated to a subagent (a
dedicated PPTX or docx build agent) because the parent agent is
running Phase A in parallel or the deck build is mechanically
intensive. The skill prescribes what Phase B decks must and must not
contain (§14.2, §14.3) and where each claim must come from (§3.2
provenance) — but the parent agent still has to translate Phase A
findings into a form the subagent can render without re-deriving
anything.

This section specifies the handoff format so the translation is
consistent across projects and the subagent receives a
self-contained brief. Without a standard format, each Phase B
delegation produces a bespoke ~3,000-word prompt that re-invents
the structure; most of that re-invention is redundant, and the
inconsistency across projects makes review harder.

**Required structure of the handoff document**

For every slide in the intended deck, the handoff captures:

1. **Slide ID and purpose** — one sentence describing what this
   slide achieves in the narrative arc. (e.g. "Slide 3 — headline
   visibility result, anchors the rest of the deck.")
2. **Headline stat (if any)** — the exact number, the exact label,
   the exact unit (%, rank, count). Pre-formatted, not derived.
   The subagent does not compute — it renders.
3. **Supporting body copy** — the exact text that appears on the
   slide, in stakeholder register (§3.5). If the deck is in a
   non-English target language, write the target-language copy
   verbatim; do not ask the subagent to translate.
4. **Data sources (provenance)** — the platform query or report
   (brand report, domain/URL citation report, per-engine breakdown,
   chat-level reading) that produced each number on the slide,
   with its filters and window, referenced for audit but not for
   the subagent to re-query. Format: `brand report (non-branded,
   30-day window) → visibility = 37%`. The platform companion gives
   the platform's own call-notation for this line.
5. **Compliance checks already applied** — explicit notes
   confirming which §14.2 hard rules were checked in the
   translation: no branded visibility number, no methodology
   vocabulary, no unsummed-across-brands figures, no Google-vs-AI
   contrast if Google-family engines are tracked. The subagent
   should not re-verify these — it should trust them — but the
   parent agent should have verified them at translation time.
6. **Visuals** — for any chart or data table, the *exact* dataset
   the visual should display, pre-filtered, pre-sorted, in final
   display order. Do not hand the subagent a broader dataset and
   ask it to filter. Subagents fabricate or reorder data when
   given more than they need (cross-cutting observation).
7. **Layout directives** — any composition rules that aren't
   visible from the data (e.g. "three stat callouts in a row; all
   boxes must fit the widest label", "disclosure italic, 14pt,
   directly beneath the headline stat per §14.14").

**Structure template (YAML sketch):**

```yaml
deck_metadata:
  project: [brand / project name]
  loop_reference: Loop N findings, YYYY-MM-DD
  register: [language and tone register]
  deck_mode: [compressed | stabilised | benchmark-snapshot]

slides:
  - id: 1
    purpose: cover — title, branding, date
    headline: [exact title copy]
    body: [exact subtitle copy]
    visuals: none

  - id: 2
    purpose: [one-sentence narrative purpose]
    headline:
      value: [exact number]
      label: [exact label]
      unit: [unit]
    body: [exact body copy in target language]
    visuals:
      - type: [chart|table|none]
        data: [exact pre-filtered rows]
    provenance:
      - [platform report / query, filters, window → number]
    compliance_checks:
      - branded_visibility_excluded: yes
      - methodology_vocab_absent: yes
      - google_vs_ai_contrast: not applicable (engines: ChatGPT, Perplexity, Claude)
      - summed_across_brands: no (all figures single-brand or pre-computed group query)

  # …one entry per slide
```

**Rule:** Phase B delegation without this handoff format is a
last-resort pattern, not a default. The parent agent bears the
cost of the translation; the subagent bears the cost of the build.
Splitting the work at the wrong seam produces bespoke briefs and
inconsistent decks.

**Delegation decision: when to delegate at all.** Short decks
(≤6 slides) and decks that reuse a template the parent agent has
already produced twice can be built in-line without delegation.
Delegate when (a) the deck is ≥ 8 slides, (b) the rendering
toolchain is different from what the parent has open (e.g. the
parent agent's environment lacks a PPTX runtime and a subagent has
it), or (c) the deck involves ≥ 3 charts where rendering fidelity
matters.

See also: in-environment constraints around PPTX rendering engines,
chart rendering parity across viewers, and cover-slide composition
rules — these belong to whatever presentation tooling the subagent
runs, and are subagent concerns, not parent-agent concerns. The parent agent's
job is the translation; the subagent's job is the render.

### 14.16 Configuration deliverable for platforms without a write API

Not every tracking platform can be written to by the agent. Where
the platform has no write API (or the engagement has no API access),
the Write step (§12) is replaced by a configuration deliverable that
a human loads into the platform — by bulk import or by manual entry.
Structure the output in whatever format the tool needs — JSON for
API push, CSV for bulk import, or a human-readable document for
manual entry. Read the platform companion for the platform's import
format and field names before producing the structured file.

The final output should include:

1. **Structured data file** (JSON or CSV) ready for tool import/API
   push
2. **Human-readable document** (markdown) with:
   - Complete prompt tables per brand/category
   - Competitor recommendations per market
   - Methodology notes explaining data sources used and selection
     rationale
3. **Category/brand structure definition** explaining what each
   category represents and why it was chosen

Save deliverables to the engagement's working directory in the
workspace.

This is a configuration artefact, not a stakeholder deliverable: the
§14.2 / §14.3 register rules do not apply to it, but label travel
(§3.6) does — labels in the structured file, the human-readable
document and the category definition must match the Strategy
sign-off, since they are what gets loaded into the platform.

---
