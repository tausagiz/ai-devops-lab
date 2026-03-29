---
name: "Close Branch"
description: "After merge, close a feature branch safely and return to updated main."
agent: "Close Branch"
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
Close a merged feature branch safely.

Follow branch cleanup rules from `AGENTS.md`. If the target branch is `main` or `master`, stop. If deletion would require `-D`, stop and ask for explicit confirmation.
