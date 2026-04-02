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
- Clarify that `/Command` examples are Copilot Chat slash commands entered in chat.
- Add one short note that other tools may require different syntax.

List these commands with one-line usage:
- `/Workflow Help`
- `/New Branch`
- `/Validate Changes`
- `/Fix Validation`
- `/Check Scope`
- `/Split Scope`
- `/Rescope Branch`
- `/Prepare Commit`
- `/Open PR`
- `/Close Branch`
- `/Branch Cleanup Report`
- `/Cleanup Stale Branches`

If my goal is clear, recommend exactly one next command. If my goal is not clear, still show the full command list but set the recommended next command to `None`.
