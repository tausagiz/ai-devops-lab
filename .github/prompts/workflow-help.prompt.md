---
name: "Workflow Help"
description: "Show natural command examples for workflow/git tasks and recommend one next action without requiring manual agent switching."
argument-hint: "Optional: current goal"
---
Show a compact workflow help screen for this repo.

Workflow rules:
- Do not run git or tests.
- Do not edit files.
- Keep output concise.
- Clarify that examples are plain natural-language commands typed in chat in the current execution mode.
- Add one short note that other tools may require different syntax.

Show these natural command examples first:
- create branch for <task>
- validate changes
- commit these changes
- open or update PR
- close current branch after merge

Then show optional specialized fallbacks only:
- `@Split Scope` (high drift / non-cohesive branch split)
- `@Learning Coach` (learning workflow)
- `/Workflow Help` (show this help again)

If my goal is clear, recommend exactly one short natural command as next action. If my goal is not clear, still show the examples and set the recommended next action to `None`.
