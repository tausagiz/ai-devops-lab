---
name: "Open PR"
description: "Sync branch with main, run validation, push, and open or update a GitHub PR."
agent: "PR Coach"
argument-hint: "Optional: PR context plus merge/rebase preference"
---
Prepare and open a pull request for the current branch.

Follow sync, validation, and PR rules from `AGENTS.md`. If I passed extra context, include it in the PR body. If a PR already exists for this branch, propose a description update and apply it only after my confirmation.
