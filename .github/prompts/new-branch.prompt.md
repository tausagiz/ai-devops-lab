---
name: "New Branch"
description: "Start new work from updated main and create a branch from task description."
agent: "Branch Coach"
argument-hint: "Required: short description of planned work"
---
Create a fresh feature branch from updated `main` using my task description.

Follow naming `type/short-slug` with allowed prefixes from repo rules. If worktree is dirty, stop. If description is missing, ask for it.

Report main update status and created branch name.
