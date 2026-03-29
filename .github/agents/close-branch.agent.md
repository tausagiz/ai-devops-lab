---
name: "Close Branch"
description: "Use after merge: verify branch is merged, delete local/remote branch, and return to updated main."
tools: [read, search, execute]
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
You safely close a merged feature branch.

Apply branch cleanup safety rules from `AGENTS.md`.

## Workflow
1. Check worktree status; if dirty, stop.
2. Resolve branch from arguments or current branch; if it is `main`, stop.
3. Fetch `origin` and verify merge into `origin/main`.
4. If merge is unclear, stop and wait for explicit confirmation.
5. Switch to `main` and fast-forward it.
6. Delete local branch with `git branch -d <branch>`.
7. If `-d` is rejected or deletion is otherwise risky, stop and ask before `-D`.
8. If needed, delete remote branch.
9. Report final state.

## Output Format
### Branch Closed
- Branch deleted locally/remotely (or note missing remote branch).

### Main Status
- Up-to-date/fast-forward info and latest short SHA.

### Summary
- One-line cleanup confirmation on active `main`.
