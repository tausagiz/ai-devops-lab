---
name: "Close Branch"
description: "After merge, close a feature branch safely and return to updated main."
agent: "Close Branch"
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
Close a merged feature branch safely.

If worktree is dirty, stop. Verify branch is merged into `main` before deletion. If not merged, require explicit confirmation. Update `main`, delete local branch, then delete remote branch if it exists.

Report branch closure status and main update status.
