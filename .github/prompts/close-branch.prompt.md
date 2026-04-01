---
name: "Close Branch"
description: "After merge, close a feature branch safely and return to updated main. Handles both normal branches and post-split cleanup."
agent: "Close Branch"
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
Close a merged feature branch safely.

Follow branch cleanup rules from `AGENTS.md`.

If the branch is a split-operation artifact (source branch or backup branch), verify that split-child branches are merged before cleanup. Before running any branch deletion command with `-D`, stop and ask for explicit confirmation. If the branch to close is `main` or `master`, do not proceed automatically; stop and ask for explicit confirmation instead.
