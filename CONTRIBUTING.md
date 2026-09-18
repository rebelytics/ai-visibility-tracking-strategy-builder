# Contributing to ai-visibility-tracking-strategy-builder

Thanks for helping this methodology evolve. It's a living workflow — every strategy build run against a new project has the chance to surface a pattern or gotcha worth encoding here.

## What's in scope

- **New gap patterns.** If you ran a build and found a failure mode that isn't in the pattern library yet, propose a new entry. Include the symptom, the diagnosis, and the action.
- **Revisions to existing patterns.** If a pattern's diagnosis or action turned out to be wrong or incomplete, propose a revision.
- **Core principle revisions.** If a principle held you back from a better outcome, explain why and propose a nuance.
- **Quality gate additions.** If a pre-execution check would have caught a mistake you made, propose it.
- **New data intake sources.** The skill's baseline path is deliberately minimal (the platform's own reads + web search + user's domain knowledge). Ring 1 (automated tools) and Ring 3 (optional enrichment) are designed to grow. If you wired up a new connected MCP or data source that strengthened the intake, add handling notes.
- **Prescriptive overrides.** The Strategy sub-phase of Phase A is intentionally prescriptive with explicit "Override this if…" callouts. If you hit a departure case the current overrides don't cover, propose an addition.

## What's out of scope

- Platform-specific mechanics — field names, API or MCP behaviour, import formats, plan-tier quirks. Those live in the platform companion skills (`peec-ai-tracking-strategy-builder`, `sistrix-tracking-strategy-builder`) and in the platform's tool companion; PR them there.
- Marketing of specific consulting services, agencies, or products.
- Client-specific or proprietary data. Keep patterns generalisable.

## How to contribute

### Via pull request

1. Edit `SKILL.md` on a branch off `main`.
2. Bump the version in the frontmatter (`version`):
   - **patch** for fixes and small clarifications
   - **minor** for new pattern library entries, new workflow sections, or a new data intake source
   - **major** for breaking workflow changes (phase restructure, renaming deliverables, dropping the prescriptive override model)
3. Open a PR with a clear description of the strategy build that motivated the change. Sanitised intake snapshots, override decisions, or before/after snippets are gold.

### Via issue

1. Open an issue.
2. Include: which section of `SKILL.md` you're talking about, what you observed during the build, what you expected, and any context that would help another contributor reproduce the case (without leaking client data).

## Style notes

- Write for an AI agent reading the skill as context. Keep statements precise and actionable.
- Prefer "when X, do Y" over general advice.
- Section headers are numbered (`§8.1`); keep that numbering stable across patch versions — external references rely on it.
- When adding a new pattern to the pattern library, follow the existing format: Symptom → Diagnosis → Action. Don't skip the diagnosis step; it's what turns a pattern into a teachable lesson.
- Prescriptive recommendations in the Strategy sub-phase of Phase A follow the three-line structure: **Recommended** / **Reasoning** / **Override this if**. Keep that shape — it's what makes the output usable by agents that can't reason well about menus.
- Flag anything plan-dependent or tool-dependent explicitly.
- Keep the body platform-agnostic: if a proposed rule only holds because of one platform's mechanism, it belongs in that platform's companion. The test: could the sentence survive having the platform's name removed?
- Phrase any claim about how platforms behave as a verified-at-last-check fact with a re-verification instruction; undated present-tense claims go silently wrong.

## Code of conduct

Be kind. The skill is meant to help every agent running a tracking strategy build, not just the ones you'd personally hire. Disagreements about methodology are fine and welcome; personal attacks are not.
