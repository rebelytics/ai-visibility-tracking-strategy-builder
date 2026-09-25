# Quality gates (§15)

Part of the **ai-visibility-tracking-strategy-builder** skill (CC BY 4.0 — Eoghan Henn / [rebelytics.com](https://rebelytics.com)). Section numbers are global across the skill family — the section map in `SKILL.md` says where each § lives; platform companions extend some sections with their own "Peec implementation" / "Sistrix implementation" parts.

**Load trigger:** Read at every phase transition. The relevant gate must pass before §12 Write, §13 Analyse, or §14 Phase B begins, and the §15.4 merged-set gates must pass before any prompt set is written to the platform or delivered as an import file — a failed gate item blocks the transition. Read the matching "§15.N — <platform> implementation" part in the platform companion at the same time; it names the tool calls and fields through which each gate is checked on that platform.

**Contents:**

- §15 Quality gates — how gates work
- §15.1 Pre-Write gates (before §12 runs)
- §15.2 Pre-Analyse gates (before §13 runs)
- §15.3 Pre-Phase-B gates (before §14 runs)
- §15.4 Merged-set validation gates (before any prompt set is written or delivered)

---

## 15. Quality gates

Gates are grouped by phase so they can be applied at the right point
in the loop. Missing any gate is grounds to pause and address before
proceeding.

Two rules apply to every gate in this file:

- **A delivery that fails a check gets corrected, not caveated.** A
  gate item that fails is fixed before the transition; it is never
  carried across the transition as a note, a footnote, or a "known
  limitation".
- **Gates are platform-agnostic; their checks are not.** Every item
  below is phrased in terms of what must be true. How to verify it on a
  given platform — which tool call, which field, which report — is in
  the platform companion's "§15.N — <platform> implementation"
  part. Where the companion names a check, run that check; where it
  does not, verify the item by whatever means the platform offers and
  record how.

### 15.1 Pre-Write gates (before §12 runs)

**Visible-in-output rule:** The agent must write these checklist results
into the Intake summary block (§8.4) verbatim, including ✓ / ✗ marks
and the rationale for any ✗. This turns the checklist from an internal
practice into a visible artefact the user can inspect and challenge.

- [ ] Intake state is populated for every critical field (brand,
      markets, owned domains, known competitors, regulatory context)
- [ ] Each applicable ring's path was attempted; skipped paths have a
      documented rationale (§3.10 — rings are paths, not an ordinal
      sequence) — first loop only
- [ ] Ring 3 was attempted on first loop (§3.8, §8.3) — "user had no
      data" is valid; "agent decided Ring 1 was enough" is not
- [ ] Ring 3 automated inventory (§8.3.1) was completed before
      composing the user ask
- [ ] Sitemap baseline (§8.3.2) was fetched and parsed before any
      user-facing ask about URL structure or crawl data
- [ ] Ring 3 data request (§8.3.3a) was sent as plain text, separate
      from the scoping widget (§8.3.3b) — not collapsed into one
      AskUserQuestion call (§3.8 shape 1)
- [ ] **External data — itemised disposition.** Every row of the
      `ring3_data_disposition` table (§7.2) is in one of three
      resolved states: `received`, `declined_by_user`,
      `not_applicable`. The fourth state, `outstanding`, is explicitly
      disallowed at this gate — no rows may be `outstanding`, and none
      may be marked "deferred to Loop 2", because that
      framing is the planned-deferral skip shape (§3.8 shape 3) and
      the gate rejects it. A blanket "Ring 3 confirmed unavailable" is
      not acceptable; each category must be individually
      dispositioned.
- [ ] Every Strategy recommendation in the output is **tagged with its
      evidence source** — Ring 1 (tool), Ring 2 step letter, Ring 3
      user-provided file, or "no direct evidence — recommendation is
      the skill default". Recommendations without evidence-source tags
      pass too easily; the tag forces the agent to confront whether
      the recommendation is data-driven or intuition-driven (§4.1,
      §4.2, §3.8).
- [ ] Every field the platform can expose (market, plan limits,
      active engines, existing configuration) was derived from the
      platform before the user was asked for it; the platform
      companion's known-gaps table (§8.1) says which fields the
      platform's API genuinely does not expose, and only those were
      asked — framed as "the platform doesn't expose this", not
      "tell me"
- [ ] Every Strategy recommendation (§9.1–9.7) has a Recommended,
      Reasoning, and Override block
- [ ] **Allocation direction settled before any allocation ran**
      (§9.1.0) — the user was asked whether the budget is fixed or being
      sized; where fixed, the sign-off states how many of the brand's
      products the budget leaves unmeasurable; where sized, every
      product cell carries the two-prompt floor and the budget is the
      output
- [ ] Prompt disposition table (existing projects only) classifies
      every existing prompt into one of six buckets
- [ ] Brand roster specifies owned domains, name variants (aliases),
      and — where the platform supports one — a detection pattern for
      own brand and every tracked competitor
- [ ] Tag taxonomy has no more than 3 dimensions and 25 total tags
- [ ] Every proposed prompt has at least one tag from each taxonomy
      dimension, exactly one brand-mention tag (§9.7), and a market
      (country) assignment
- [ ] Branded-prompt count is within 5–10 and tagged consistently
- [ ] **Disambiguation pass run on the finalised set, per language**
      (§9.9) — every domain-specific noun with a mainstream homonym
      flagged, and each one either anchored with its product category
      or the drift accepted with the decision recorded
- [ ] Where a trust / reviews block is included (§9.9), it sits inside
      the branded allocation, carries the branded brand-mention tag,
      and is marked for exclusion from the headline visibility figure
- [ ] Brand-mention taxonomy was chosen against the intermediary test
      (§4.10) — where a large share of the brand's value comes from
      entities it does not own, `other-brand` is tracked as its own
      cohort rather than folded into `non-branded`
- [ ] **Multi-market only:** no market's allocation was inherited from
      a sibling market on structural grounds. The cross-market
      divergence check (§9.2) was run on one demand source classified
      identically per market, and independent allocations were used
      wherever a topic's share diverged by more than ~2×
- [ ] Engine coverage recommendation (§9.6) was made against the
      engines actually available to this project on its plan — not
      against the platform's full engine list — and routed to the
      correct branch
- [ ] Sister-brand relationships are recorded in the intake state and
      reflected in the brand roster configuration
- [ ] Regulatory context (if applicable) has a dedicated tag and a
      reporting-split note
- [ ] Content strategy findings section is populated with any
      actions outside the tracking tool surfaced during intake
- [ ] Intake state is saved with `last_refreshed` set to today's date
- [ ] Strategy sign-off artefact is in place (§9.8)
- [ ] The §15.4 merged-set validation gates have passed on the full
      proposed prompt set (all markets, all authors' batches merged)
      — not on any batch in isolation

### 15.2 Pre-Analyse gates (before §13 runs)

- [ ] Write verification (§12.5) completed cleanly; any reconciliation
      mismatches were replayed and closed out
- [ ] Earliest re-analysis date (§12.7) has passed — don't analyse
      before signal maturity
- [ ] Detection-pattern spot-check (§13.1) is ready to run as the
      pre-flight step; the sample-5-detected + 5-not-detected approach
      is understood, not skipped
- [ ] Cohort maturity map is available (which prompts are how old)
- [ ] **First run of a new prompt set: the cited sources of the
      disambiguation-flagged prompts have been read** (§9.9) — drift is
      invisible in the mention rate and visible only in the sources
- [ ] **Every visibility figure is a per-answer share** — executions as
      the denominator, window stated (§13.5). No per-question
      at-least-once count is being carried as visibility, and where the
      platform's API exposes only a per-question flag, the per-answer
      figure has been taken from the surface that publishes it
- [ ] **No run-frequency conclusion drawn from a between-population
      comparison** (§12.7); where frequencies are mixed, the run count
      per market is recorded and low-run markets are limited to
      breakage-only changes
- [ ] Hand-off from the previous Write sub-phase (§12.8) is in hand
- [ ] Where the platform exposes its own recommendation / action
      feed, it has been pulled for the loop's window, with
      high-opportunity slices drilled into (§13.17.1)
- [ ] Each platform-generated recommendation has been run through the
      critical-filter step with signal / action / review-outcome
      recorded separately (§13.17.2)
- [ ] Every editorial / comparison target surfaced by the platform
      in a commercial vertical has been legitimacy-checked via the
      fetch-then-browser fallback chain (§13.17.3), with action-shape
      routed to PR (genuine editorial) or network-join
      (affiliate-driven) accordingly (§13.17.4)

### 15.3 Pre-Phase-B gates (before §14 runs)

- [ ] Phase A has stabilised — the most recent Analyse loop produced
      no material action for the next Strategy iteration (§13.6)
- [ ] Every finding included in Phase B traces back to a platform
      data pull recorded in Phase A findings (§3.2 provenance)
- [ ] Labels used (tag names, topic names, strategy terms) match
      across the platform configuration, the Strategy sign-off, and
      Phase A findings (§3.6 label travel)
- [ ] The deck's register is stakeholder-appropriate — the audience
      separation check (§3.5) has been run on the draft
- [ ] Data-surface enumeration table (§14.6) is complete — every data
      surface the platform exposes has been touched or explicitly
      marked not-applicable, with no untouched surfaces remaining
      before drafting begins
- [ ] Branded visibility figure does not appear in any Phase B slide
      (§3.1 Phase B rule, §14.2)
- [ ] No internal methodology vocabulary ("rig", "instrument",
      "dimension", "Phase A/B", "loop", "Ring 1/2/3", "cohort")
      appears in any stakeholder-facing slide (§14.2)
- [ ] No methodology-proving slide (blind-spot case study, provenance
      table, "how the setup evolves") is used as primary content —
      all are moved to back-pocket / Q&A (§14.2)
- [ ] Every structure / process / data-source slide pairs
      architecture with a specific audience-relevant finding (§14.2)
- [ ] Every topic-priority claim is backed by at least one external
      source from the §14.10 list (product category mapping, SKU
      count, published brand commitment, external search data, or
      industry report) — not the platform's own prompt-volume
      estimate alone
- [ ] For ecommerce decks: topic-to-category mapping table (§14.11)
      is populated and every mapping is verified by fetching or
      opening the page in a browser; unmappable topics are surfaced
      for review
- [ ] Any vendor-tool review slide (KEEP/CUT of the platform's
      recommendation feed or equivalent) has at least one KEEP callout
      showing where the strategy improved on the tool — or an explicit
      "no reinterpretation needed" statement (§14.12)
- [ ] Selection / filtering / inclusion-exclusion sentences use
      procedural attribution ("our tracking strategy filtered",
      "the methodology kept") rather than personal attribution
      ("we filtered", "we kept") (§14.9)
- [ ] Closing slide is tool-independent — survives a decision not to
      renew the tracking tool (§14.13); test applied before sign-off
- [ ] Composition gate passed for every slide (§14.7): ≤4 text
      blocks, ≤1 block below 14pt exempting citations/page numbers,
      URL/domain/entity-as-primary-visual rule honoured, 15-second
      read test passes in composed prose
- [ ] Visual PNG inspection (§14.7) has been run on every
      multi-column slide and every slide with non-English labels;
      no overflow, margin bleed, baseline collision, or font-size
      inconsistency remains
- [ ] Every brand-mention cohort the project tracks is reported on its
      own line in every headline slide — two where the split is
      branded / non-branded, three where `other-brand` is tracked
      (§3.1, §4.10, §9.7)
- [ ] No tautological findings (§13.3) are used as lead lines
- [ ] No visibility, SoV, retrieval-share, citation-share, or any
      chat-share metric is computed by adding per-brand percentages.
      Any "group" / "family" / "combined" figure was produced by a
      single platform query over the whole brand set (or by manual
      response-ID set union) — and is labelled as such with the
      composition method named in the caption. No "combined" / "group"
      bar drawn by arithmetic addition appears on any chart (§14.2,
      §14.3 group-as-rows rule)
- [ ] Every named page or content piece on every slide has its URL
      as a clickable hyperlink on the same slide (§14.3 every-named-
      piece-clickable-URL rule). Hyperlink markers use ASCII arrows
      (`→ `), not the unicode link emoji
- [ ] No time-series chart appears in a window during which the
      tracked prompt set changed (prompt creation, prompt-text edits,
      or prompt deletion). For any surviving time-series chart, the
      caption names the prompt-set stability window (§14.2
      trend-with-changing-cohort, §14.3 time-series caption rule,
      §13.7 stable-cohort gate)
- [ ] For every named gap URL on any slide, the URL's host has been
      classified against the tracked brand roster. Competitor
      homepages, category pages, and product pages have been
      excluded from editorial-gap slides. Competitor-owned
      multi-brand listicles that appear are explicitly flagged as
      competitor-owned in the slide content (§13.9, §14.3 gap-list
      classification rule)
- [ ] Every named factual claim on every slide (especially
      comparison claims of the form "X includes Y, Z doesn't") has
      been verified in this session or in the most recent loop's
      findings. Claims older than the most recent loop are flagged
      for re-verification before inclusion or removed from the slide
      (§13.6 carry-forward claim re-verification)
- [ ] The cover slide carries a single message; multi-stat hero
      compositions sit on body slides only. The §14.8 combined-
      headline pattern is not used on the literal cover slide
      (§14.3 cover-single-message rule)
- [ ] **Editorial pitch targets are browser-verified.** Every
      editorial pitch target named on any slide has been opened in
      a browser and verified to satisfy all of: (a) the own brand
      is genuinely absent from the page (cases (a)/(b)/(c) of the
      §13.9 brand-detection verification have been disambiguated);
      (b) the page is open-access — paywalled sources are dropped
      or framed as visible-snippet targets only; (c) the page URL
      is the right one for the brand's commercial positioning
      (e.g. mid-market vs upper mid-market — the listicle that
      ranks the wrong tier is not a pitch target); (d) the page's
      editorial quality justifies a pitch (vs an AI-generated SEO
      farm). Tool-surfaced action candidates from URL gap reports
      are signals, not actions; promotion to action requires
      browser verification.
- [ ] **No internal artifact references on stakeholder slides.**
      Stakeholder methodology slides, footers, and captions must
      not carry: platform project IDs, internal findings file
      paths (`findings-YYYY-MM-DD.md`), prompt IDs, brand IDs, tag
      IDs, session IDs, workspace paths, or any other internal
      artifact identifier. Provenance for audit purposes belongs in
      the working findings artefact, not on the deck. Methodology
      slides describe the data and method in stakeholder-register
      language ("Source: daily tracking of N questions across M
      engines, P-day window"), not in internal-tooling language. The
      §3.2 provenance discipline governs the findings file; the
      stakeholder methodology slide describes the methodology, not
      the audit trail (§14.3 audience-separation rule).
- [ ] **Terminology consistency check across the full deck.**
      Identify the 4–6 key concept terms the deck depends on
      (engines / AI tools / AI assistants; branded / non-branded /
      "by name" / category-level; product pages / range pages /
      category pages; policies written / policy count / premium
      volume; etc.) and grep the build script for each
      variant. Pick one preferred term per concept and replace
      every alternate. The decision on which term to use is less
      important than using one consistently — terminology drift
      across slides reads as inattention to the stakeholder
      audience even when each individual choice is defensible
      (§14.3 register-consistency rule). Ship a small terminology-
      check helper alongside the build script when feasible:
      a `{key concept: preferred term, forbidden alternates}`
      map with grep-and-report output, run as the last
      pre-render check.

### 15.4 Merged-set validation gates (before any prompt set is written or delivered)

These gates apply to the prompt set as a whole — whether it is about to
be written to the platform through its API (§12) or delivered as an
import file for someone else to load. They run on the **merged set,
not per batch.** Per-batch validation can only check properties local
to a batch. Uniqueness, vocabulary consistency and cross-slice balance
are global properties and are unverifiable from inside any slice; where
several people (or parallel agent runs) authored batches, the
merge-time pass is the only place the global invariants can be checked.
It is not tidying.

They also apply to the **whole finished set, not the part of it this
session authored.** A merged set frequently contains prompts carried
over from an existing project or an earlier delivery, and those arrive
with the implicit authority of already being tracked. Inheriting feels
like a smaller act than authoring, so the inherited share is the part
that never gets checked — which is exactly why gates 12 and 13 name it.

Automate whatever can be automated (counts, field integrity, tag
conformance, the near-duplicate sweep, roster uniqueness, the realised
composition, the product-detector assertion, the language validator)
and read the rest. Run the gates in this order — the cheap structural
checks first, so that the judgement-heavy ones run on a set that is
already structurally sound. Gates 12–15 are numbered in the order they
were added, never re-slotted, so that the platform companions' gate
references stay stable — companions point at these gates by number and
never restate the list. Run gate 12 alongside gate 1 (it is a count
check), gate 13 alongside gate 8 (it is a read-every-prompt check),
gate 14 alongside gate 7 (it is the mapping gate 7 relies on) and gate
15 alongside gate 2 (it is a text check).

1. **Counts.** Every grouping (topic / brand / category /
   market) has exactly the number of prompts the approved allocation
   gives it. Off-by-one errors are common when building large sets.
   Automate the count validation; do not eyeball it.

2. **Field integrity.** Every row has every field the platform's
   import contract requires; required fields are non-empty; text is
   UTF-8 clean (no mojibake from a spreadsheet round-trip, no smart
   quotes where the platform rejects them).

3. **Tag conformance.** Every tag comes from the agreed vocabulary
   (§9.4) — no ad-hoc tags invented by an author. Every prompt carries
   at least one tag from each taxonomy dimension and exactly one tag
   from each single-valued dimension (brand-mention always; funnel and
   intent where the taxonomy defines them that way). No duplicate tags
   on a row.

4. **Brand-mention consistency.** Every prompt carries exactly one
   brand-mention value, assigned on who is named in the prompt text
   (§4.10, §9.7). Where several people authored batches in parallel,
   check this across the merged set rather than within batches —
   inconsistent labelling of the other-brand case is invisible from
   inside any one batch, and two authors flagging the same ambiguity
   means the brief is the defect.

5. **Placement.** The brand-mention value and the grouping agree with
   the taxonomy decision made in §9.5 / §9.7. Where the taxonomy
   reserves a dedicated grouping for branded prompts (a brand-only topic
   or equivalent), branded prompts sit only there — no branded prompt
   appears in a category grouping, and no category prompt appears in
   the brand grouping. Where the taxonomy instead lets branded prompts
   live under the category grouping they are about and carries the
   split on the brand-mention tag alone, the check is that no grouping
   named after the own brand or a competitor exists at all (a brand
   name as a grouping is a roster-classification defect, §9.3, §9.5).

6. **Cross-batch near-duplicates.** Token-similarity sweep across the
   whole set, not within batches. Two authors given the same source
   anchor will independently write the same prompt, and neither
   self-check can see it. Also scan for prompts that are too similar
   across categories: two categories shouldn't both contain "best
   accounting software for freelancers" unless they represent
   genuinely different intents.

   A high-similarity pair is a **decision to make, not an automatic
   defect**: a deliberate branded/unbranded twin ("what's the best
   running shoe for a beginner?" against "is *brand X*'s running shoe
   good for a beginner?") scores high on token overlap and is exactly
   the comparison the set exists to make. Read every flagged pair;
   merge the accidental ones, and record the deliberate ones so the
   next run does not re-litigate them.

7. **Coverage.** Map prompts back to the client's product/service
   pages (the sitemap baseline from §8.3.2 is the reference list). Are
   all major offerings represented? Are any significant product lines
   missing? The mapping uses the product detectors of §9.9 (gate 14),
   never token overlap — a prompt covers a product only if its text
   names it. Where the allocation direction was "budget fixed"
   (§9.1.0), the products this gate finds uncovered are the count the
   sign-off reports as unmeasurable.

8. **Commercial intent.** Re-read every prompt and ask: "Is this close
   enough to a purchasing decision?" Remove any that drift into purely
   educational territory. The one exception is a prompt kept
   deliberately as an owned-territory informational probe — it passes
   only if it carries the tag that identifies it as such; an untagged
   informational prompt fails this gate.

9. **Cross-market allocation** (multi-market sets only). Confirm no
   market's allocation was inherited from a sibling market on
   structural grounds, and that the divergence check (§9.2) behind any
   reused allocation is written down.

10. **Competitor roster.** Brand names unique, no domain claimed twice,
    exactly one entry identified as the project's own brand (§9.3).

11. **Format conforms to the platform's import contract — see the
    platform companion.** Whatever the platform needs — an API payload
    shape, a CSV with a fixed column set, a particular encoding of
    multi-valued fields, a controlled vocabulary for language and
    country values, a human-readable document for manual entry — is
    checked against the platform's *current* contract, read from its
    own documentation or the project's own schema registry, not from
    memory or from this skill. Where the contract is unconfirmed,
    state every assumption explicitly and choose the ones that are
    cheap to reverse: encoding, whether an identifier is supplied,
    value vocabularies and defaulted timestamps are all format-level
    and correctable in one pass. None of them should block authoring.

12. **Realised composition.** Wherever the strategy states a
    composition — the instrument split of §9.1 (provider-selection /
    how-to / branded cohort), the funnel or volume mix, an
    other-brand share, a cap on an audience-exploration band —
    recompute the mix the finished set actually has, per market and
    per container, and compare it with the specified one. Run it
    after *every* selection or disposition pass (§9.1.4, §10), not
    only after authoring: a set cut to budget by ranking looks
    well-chosen, hits every count exactly, and can still have lost an
    entire instrument, because a ranking removes whatever it scores
    lowest wholesale and leaves no trace in the result. Failure
    shape: whole markets come out almost entirely provider-selection,
    leaving the source-citation instrument almost nothing to measure
    with. Within the branded cohort, count the
    head-to-head competitor comparisons against the cap in §9.1.4 — a
    cohort that is four or five comparisons out of five measures
    neither reputation nor source authority. A band that is more
    than a few points off its share is refilled from the eligible pool
    by the fill-by-quota rule; it is not caveated.

13. **Service grounding.** Every prompt that names a product, a
    product line, a service, a programme or a standard must map to
    something the brand actually offers, **verified against the
    brand's own catalogue** — the sitemap baseline of §8.3.2, the live
    service or product pages, fetched — not recalled and not inferred
    from the industry. Every prompt in the set is a claim that the
    brand could plausibly be the answer; where the claim is false the
    prompt is not a neutral measurement but a structural zero that can
    only ever surface competitors and drags the headline down for a
    reason unrelated to visibility. Where a prompt fails, remove it or
    reclassify it by intent: "how do I prepare for X" is legitimate
    for a topic the brand sells nothing for and stays as an
    owned-territory or diagnostic probe with the matching tag; "who
    should I hire for X" / "best providers for X" is not, and goes.
    Two further shapes fail this gate: a prompt asking how to obtain
    something only a third party issues or grants, and a prompt naming
    one market's regulator, retailer or programme inside another
    market's set. **Apply the gate to carried-over prompts with the
    same rigour as to new ones** — inherited prompts fail it as often
    as new ones, and an authoring pass that grounds only the prompts it
    wrote itself leaves the inherited share unchecked. **The check is
    also of kind.** A product the brand does offer, phrased through a
    template for a service kind the brand does not deliver for it — an
    integration the brand documents but does not sell, templated as a
    purchase ("how much does [product] cost") — fails here too. Read
    each product's template kind off the product's own page, not off the
    catalogue heading it sits under (§9.9).

14. **Product detection.** Where the set has product cells (§9.1.0) or
    product tags, one detector per product exists (§9.9: distinctive
    pattern, word-bounded, case-sensitive for short acronyms), and the
    **same** detector was used for carry-over matching (§10), product
    tagging and the coverage baseline (§8.5.6). Assert, automatically,
    that every prompt authored or carried over for a product cell is
    detected as its own product and as no other; a product-cell prompt
    its own detector does not fire on fails, and so does a prompt two
    detectors claim. Failure shape without this gate: token-overlap
    matching credits generic prompts to products they never name, and a
    short acronym matches inside a longer one, so the "already tracked"
    baseline is wrong before any authoring begins.

15. **Language validation.** A language-aware validator has run over
    **every** generated prompt in **every** language of the set, not
    only the language the author reads best, and every hit has been
    fixed in the text. Minimum checks per language: the article before
    an initialism follows its pronunciation (English "an SME…" against
    "a UK…"); no doubled noun where a product name already ends in the
    template's noun; no stray article or preposition left by
    substituting a product name that carries one ("for of X", "best the
    X"); no parenthetical from a product name inside the question. Run
    it before any write wave (§12) — on platforms where prompt text is
    immutable after creation, a miss here is not an edit but a
    retire-and-recreate, and the retired prompts stay in the project
    (the companion says what that costs). Failure shape without this
    gate: one language has a validator, the other has none, and the
    unchecked language's broken prompts go live.

#### Pre-delivery pre-flight

Before the set is written to the platform or handed over, confirm:

1. The import contract / schema was read from the platform's current
   documentation or the project's own schema registry, not from
   memory or from this file.
2. Allocation was derived per the allocation rules (§9.1), with the
   direction settled first (§9.1.0 — budget fixed, with the unmeasurable
   product count reported, or budget sized from the two-prompt product
   floor), and with the navigational-traffic exclusion from the
   denominator and the editorial redistribution both applied wherever
   the allocation was demand-derived.
3. Cross-market divergence check (§9.2) run, and independent
   allocations used where it fired.
4. All fifteen §15.4 validation gates passed on the **merged** set —
   including every prompt carried over from an existing project or an
   earlier delivery, which is grounded (gate 13), matched to its product
   cell by detector (gate 14) and counted into the realised composition
   (gate 12) exactly like a newly authored one.
5. Every unconfirmed import assumption written down in the handover,
   with its reversal cost.
6. The branded-split and regulatory-refusal reporting instructions are
   in the handover note: never blend branded prompts into a headline
   number (§9.7), and prompts tagged as regulatory-restricted mark
   cases where a refusal is not a miss — a policy decline is a
   different outcome from a brand not being mentioned, and if the two
   land in one bucket the regulated categories read as systematically
   worse than they are. Relatedly, confirm whether the platform can
   distinguish "engine returned empty" from "brand not mentioned" —
   they are different states and conflating them silently corrupts
   the denominator (§13.4).

A delivery that fails a check gets corrected, not caveated.

---
