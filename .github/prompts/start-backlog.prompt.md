---
name: "Start Backlog"
description: "Pick one backlog item on request and start a new branch for that item using repo branch rules."
agent: "Roadmap Coach"
argument-hint: "Optional: backlog item text, priority, or keyword"
---
Start work from the roadmap backlog.

Use backlog and branch rules from `AGENTS.md`.

Expectations:
- Select exactly one backlog item unless I explicitly ask for more.
- If no roadmap backlog item matches the request, ask one short clarification.
- Propose a branch name and either create it (if safe) or hand off to `/New Branch` with ready-to-use task text.
