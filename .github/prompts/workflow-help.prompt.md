---
name: "Workflow Help"
description: "Show available workflow prompts and recommend one next command."
argument-hint: "Optional: current goal"
---
Show a compact workflow help screen for this repo.

Workflow rules:
- Do not run git or tests.
- Do not edit files.
- Keep output concise.

List these commands with one-line usage:
- `/Workflow Help`
- `/New Branch`
- `/Validate Changes`
- `/Prepare Commit`
- `/Open PR`
- `/Close Branch`

If my goal is clear, recommend exactly one next command. If not, return `None`.
