---
name: "Prepare Commit"
description: "Inspect current repository changes, validate commit requirements, and quickly create a compliant commit for this repository when the worktree is ready."
agent: "Commit Coach"
argument-hint: "Optional: describe the change you are preparing to commit"
---
Inspect the current repository state and handle commit preparation for this project.

Use the repository rules from `AGENTS.md`, `README.md`, and the docs-check workflow enforced in CI.

Default behavior:
- if the current changes are coherent and commit-ready, automatically handle any docs gate violations by staging required docs files, then create the commit,
- if there is a real blocker that cannot be auto-fixed, stop before committing and explain exactly what must be fixed,
- if the user provided extra context, use it to choose the right branch name, commit title, and scope.

Return:
- a recommended branch name if the current one is not appropriate,
- one Conventional Commit title that matches this repository's allowed types,
- a short commit body with what, why, and docs updated,
- a clear docs-gate decision, noting any auto-fixes applied,
- whether the commit was created or why it was blocked.

**When the commit is successful:**
If the commit was created and all changes are committed, end with a "Next Step" section containing a ready-to-click command block with `/Open PR` — this lets the user open the GitHub PR with a single click or paste-and-enter action. Full validation will run at PR preparation time.

If I provided extra context in the prompt arguments, use it together with the actual git changes.
