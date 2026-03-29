---
name: "Close Branch"
description: "After a PR is merged: delete the current feature branch locally and remotely, then return to the latest main."
agent: "Close Branch"
argument-hint: "Optional: name of the branch to close (defaults to the current branch)"
---
Clean up after a merged pull request.

Verify that the current feature branch (or the branch named in the arguments) has been merged into `main`, then:
1. Switch to `main`.
2. Fast-forward `main` to the latest `origin/main`.
3. Delete the feature branch locally.
4. Delete the feature branch from `origin` if it still exists there.

If my worktree has uncommitted changes, stop and tell me to clean it up before switching branches.

If the branch does not appear merged, warn me clearly and ask for explicit confirmation before deleting anything.

Never force-delete without my explicit confirmation.

If local deletion fails because git does not consider the branch merged, explain that squash merges can cause this and ask whether to force-delete.

Report:
- Which branch was closed (local and remote),
- The update status of `main` and its latest commit,
- A one-line confirmation that cleanup is complete and `main` is active.
