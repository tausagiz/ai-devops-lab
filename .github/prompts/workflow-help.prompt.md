---
name: "Workflow Help"
description: "Show available workflow entrypoints and recommend one next action."
argument-hint: "Optional: current goal"
---
Show a compact workflow help screen for this repo.

Workflow rules:
- Do not run git or tests.
- Do not edit files.
- Keep output concise.
- Clarify that `/Command` and `@Agent Name` examples are GitHub Copilot Chat entrypoints typed in chat.
- Add one short note that other tools may require different syntax.

List these entrypoints with one-line usage, grouped by lane:

Core default lane:
- `@Branch Coach`
- `@Validate Changes`
- `@Commit Coach`
- `@PR Coach`
- `/Close Branch`

Advanced on-demand lane:
- `/Workflow Help`
- `/Check Scope`
- `/Rescope Branch`
- `/Fix Validation`
- `@Split Scope`
- `@Roadmap Coach`
- `@Branch Cleanup Report`
- `@Cleanup Stale Branches`
- `@Learning Coach`

If my goal is clear, recommend exactly one next entrypoint. If my goal is not clear, still show the full list but set the recommended next entrypoint to `None`.
