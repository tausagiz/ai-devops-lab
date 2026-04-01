---
name: "Cleanup Stale Branches"
description: "Use after Branch Cleanup Report: interactively confirm and delete stale local and remote branches with author confirmation option."
tools: [read, search, execute]
argument-hint: "Optional: comma-separated branch names to delete (auto-confirm); optional: skip-author-check to bypass contact confirmation"
---
You safely delete stale branches after confirmation or pre-approval.

Apply branch safety and git rules from `AGENTS.md`.

## Workflow
1. If branch list is provided in arguments, parse and use it; otherwise, run a quick scan (same as report, but interactive).
2. For each branch candidate:
   a. Show: name, age, author, email, last commit message, merge status.
   b. If branch is not pre-approved and skip-author-check is false: ask for confirmation or note author approval.
   c. If merge status is uncertain or branch has recent activity: warn and ask before deletion.
3. For confirmed deletions:
   a. Delete local branch with `git branch -d <branch>`. If this fails with "not fully merged", clearly warn and explicitly ask whether to retry with `git branch -D <branch>`; only run `-D` after the user gives explicit confirmation.
   b. If remote exists, delete: `git push origin --delete <branch>`.
   c. Record outcome (deleted/skipped/error).
4. Report final deletion summary with counts and any rollback notes.
5. Suggest next cleanup report in X days (default 30).

## Constraints
- Never force-delete without explicit confirmation.
- Skip deletion if merge status is ambiguous; ask before proceeding.
- If local deletion fails with "not fully merged", warn and ask for -D confirmation.
- Always report remote deletion outcome (success/failure).
- Stop if worktree is dirty; ask user to clean up first.
- Build a deletion audit log: branch, deletion time, local/remote status.

## Output Format
### Cleanup Summary
- Branches deleted locally, branches deleted remotely, branches skipped, branches failed.

### Deletion Log
- Per branch: name, deletion result (deleted/skipped/failed), reason if skipped.

### Contact Notes
- Authors contacted (if confirmation was needed), any failed outreach attempts.

### Audit Trail
- Timestamp, branch, local status, remote status.

### Next Action
- One short action. Copilot example: run a new `/Branch Cleanup Report` in 30 days to repeat cycle. Other tools: schedule equivalent cleanup workflow.

### Summary
- X branches deleted locally, Y deleted remotely, Z skipped; no rollback needed.
