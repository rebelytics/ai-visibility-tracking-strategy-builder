# ai-visibility-tracking-strategy-builder

Open-source, platform-agnostic **methodology skill** for building or refining an AI visibility tracking strategy — the prompt set, grouping structure, brand roster and reporting split that measure how a brand appears in ChatGPT, Gemini, Perplexity, AI Overviews and similar — on any AI visibility monitoring platform. Load it into any MCP-capable AI agent (Claude, Cursor, Codex, n8n, etc.).

## What this skill does

Runs an iterative loop — **Intake → Strategy → Write → Analyse** — that produces concrete configuration changes and findings each pass, with an optional stakeholder presentation once the strategy has stabilised. Intake uses three rings (automated tools, a baseline path that always works, a batched user ask); Strategy outputs prescriptive recommendations with explicit override callouts; Write goes through the platform's API or a validated import file; Analyse reads the platform's data and feeds the next loop.

## When it triggers

AI visibility, GEO, AI brand monitoring, prompt tracking, "what prompts should we track", "how are we showing up in ChatGPT / Gemini / Perplexity", a prompt set for an AI monitoring tool, a tracking strategy review, or reusing one market's allocation in another.

## The skill family

This is the **core**. Load it together with the companion for the platform in use:

- Peec AI — [`peec-ai-tracking-strategy-builder`](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) (with [`peec-ai-mcp`](https://github.com/rebelytics/peec-ai-mcp) for tool mechanics)
- SISTRIX — [`sistrix-tracking-strategy-builder`](https://github.com/rebelytics/sistrix-tracking-strategy-builder) (with [`sistrix-mcp`](https://github.com/rebelytics/sistrix-mcp))

For any other platform, run the core alone and treat its import or API contract as the companion's job. Section numbers are shared across the family: every "§N — <platform> implementation" part in a companion extends the core's §N.

## What this repo contains

- `SKILL.md` — mental model, cross-cutting and core principles, workflow overview, and a section map saying when to load each reference file.
- `references/` — the phase playbooks, loaded on demand: data persistence (§7), intake (§8), strategy incl. prompt authoring (§9–§10), pattern library (§11), write-and-analyse principles (§12–§13), Phase B stakeholder deliverable (§14), quality gates (§15), and `allocate.py` (the damped revenue-share allocation of §9.1.2).
- `CONTRIBUTING.md` — how to propose changes.
- `LICENSE` — CC BY 4.0.

## Install

Install the whole skill directory — `SKILL.md` and `references/` must travel together — into your MCP-capable agent's skills directory, following the client-specific path, and install the platform companion beside it. Restart your client; the skill description triggers on the phrases above.

## Contributing

Open an issue or a PR at [github.com/rebelytics/ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder). Platform-specific findings belong on the companion's repository.

## Credits

- Original author: [Eoghan Henn](https://www.rebelytics.com) / [LinkedIn](https://www.linkedin.com/in/eoghanhenn)
- Not affiliated with any AI visibility platform.

## License

CC BY 4.0 — see [LICENSE](./LICENSE). Use it, fork it, adapt it, monetise it. Keep the attribution.
