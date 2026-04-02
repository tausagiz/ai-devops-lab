---
name: "New Branch"
description: "Start new work from updated main and create a branch from task description."
agent: "Branch Coach"
argument-hint: "Required: short description of planned work"
---
Create a fresh feature branch from updated `main`.

Follow branch naming and safety rules from `AGENTS.md`.

If the description is missing or too vague:
- provide exactly 3 concise numbered suggestions,
- allow selection by number (`1`, `2`, or `3`) without requiring the user to rewrite the text,
- then continue branch creation using the selected suggestion.
