---
name: "Prepare Commit"
description: "Inspect current repository changes, validate commit requirements, and quickly create a compliant commit for this repository when the worktree is ready."
agent: "Commit Coach"
argument-hint: "Optional: describe the change you are preparing to commit"
---
Inspect the current repository state and handle commit preparation for this project.

Use the repository rules from `AGENTS.md`, `README.md`, and the docs-check workflow enforced in CI.

Default behavior:
- if the current changes are coherent and commit-ready, stage the relevant files and create the commit directly,
- if there is a real blocker, stop before committing and explain exactly what must be fixed,
- if the user provided extra context, use it to choose the right branch name, commit title, and scope.

Return:
- a recommended branch name if the current one is not appropriate,
- one Conventional Commit title that matches this repository's allowed types,
- a short commit body with what, why, and docs updated,
- a clear docs-gate decision for `README.md` or `AGENTS.md`,
- the smallest relevant validation step before push,
- whether the commit was created or why it was blocked,
- a short PR checklist.

If I provided extra context in the prompt arguments, use it together with the actual git changes.
