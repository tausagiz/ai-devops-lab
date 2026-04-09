---
name: "Close Branch"
description: "After merge, close a feature branch safely and return to updated main. Handles both normal branches and post-split cleanup."
tools: [read, search, execute]
argument-hint: "Optional: branch name to close (defaults to current branch)"
---
Safely close a merged feature branch, with special handling for post-split cleanup.

Apply branch cleanup safety rules from `AGENTS.md`.

## Workflow
1. Check worktree status; if dirty, stop.
2. Resolve branch from arguments or current branch; if it is `main` or `master`, stop and explain that main/master cannot be closed this way — suggest checking out the intended feature branch first.
3. Detect branch type:
   - If pattern matches `backup/<source>-pre-split-*`: treat as post-split backup branch.
   - Else if there is an explicit user-provided flag/context indicating split cleanup: treat as split-cleanup flow.
   - Otherwise: treat as normal post-merge cleanup; if the branch name or context is ambiguous (for example, it contains `split` but does not match the explicit backup pattern and there is no explicit flag), stop and ask the user to confirm the branch type before proceeding.
4. For normal cleanup:
   a. Fetch `origin` and verify merge into `origin/main`.
   b. If merge is unclear, stop and wait for explicit confirmation.
5. For split-related cleanup (source or backup branch):
   a. Fetch `origin`.
   b. For split-source branch: verify that all related split branches (inferred from commit/branch history) are merged to `origin/main`. If uncertain, ask for explicit confirmation of split branch list.
   c. For backup branch:
      - Verify that all related split-child branches are merged to `origin/main` (reuse results from split-source verification when available, or ask for explicit confirmation of the split branch list if uncertain).
      - Verify it is no longer actively used (can reference recent logs or user confirmation).
   d. Only after all related split-child branches are verified merged (for both split-source and split-backup flows), proceed with deletion.
6. Switch to `main` and fast-forward it.
7. Delete local branch with `git branch -d <branch>`.
8. If `-d` is rejected or deletion is risky, stop and ask before attempting `-D`.
9. If needed and safe, delete remote branch.
10. Report final state with explanation of what was cleaned up and why.

## Constraints
- Never delete `main` or `master`.
- Never force-delete (`-D`) without explicit user confirmation.
- Do not delete backup branches before split branches are verified merged.
- Do not delete split-source branches before all split-child branches are verified merged.
- Stop if merge state is uncertain or branch type is ambiguous; ask for clarification instead.

## Output Format
### Branch Close Context
- Branch name, detected type (normal/split-source/split-backup), and merge/cleanup rationale.

### Verification
- Merge status of source or split-child branches; any unmerged branches listed.

### Cleanup
- Local deletion result; remote deletion result (or note if not needed).

### Main Status
- Up-to-date/fast-forward info and latest short SHA.

### Next Action
- One short action. Copilot example: ask `@Branch Coach` in chat to start new work. Other tools: run the equivalent branch-start workflow.

### Summary
- One-line cleanup confirmation on active `main`, or `Blocked: <reason>`.
