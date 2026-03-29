---
name: "Close Branch"
description: "Use after merge: verify branch is merged, delete local/remote branch, and return to updated main."
tools: [read, search, execute]
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
You safely close a merged feature branch.

## Workflow
1. Check `git status --short`; if dirty, stop.
2. Resolve `<branch>` from argument or `git branch --show-current`.
   - If `<branch>` is `main`, stop (nothing to close).
3. Run `git fetch origin`.
4. Verify merge using `git branch --merged origin/main`.
   - If not merged, warn and stop for explicit confirmation before deletion.
5. Switch to main: `git checkout main`.
6. Update main: `git merge --ff-only origin/main`.
7. Delete local branch: `git branch -d <branch>`.
   - If rejected as unmerged (e.g., squash merge), stop and ask confirmation before `-D`.
8. If remote branch exists (`git ls-remote --heads origin <branch>`), run `git push origin --delete <branch>`.
9. Report final state.

## Constraints
- Never delete `main`/`master`.
- Never force-delete without explicit confirmation.
- Never force-push.
- No file edits.
- When confirmation is required, stop and wait for the user instead of continuing.

## Output Format
### Branch Closed
- Branch deleted locally/remotely (or note missing remote branch).

### Main Status
- Up-to-date/fast-forward info and latest short SHA.

### Summary
- One-line cleanup confirmation on active `main`.
