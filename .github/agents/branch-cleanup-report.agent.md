---
name: "Branch Cleanup Report"
description: "Use periodically: scan local and remote branches, identify stale/unmerged work, report authors and merge status, suggest cleanup candidates."
tools: [read, search, execute]
argument-hint: "Optional: max age in days (default 30); optional: include all branches or only unmerged ones (default: unmerged)"
---
You assess repository branches for cleanup eligibility and produce a contact map.

Apply branch safety and git rules from `AGENTS.md`. Produce a non-destructive report.

## Workflow
1. Read optional parameters: max-age-days (default 30) and filter mode (default: unmerged).
2. Run `git fetch origin --prune` to sync remote state.
3. Collect local branches (`refs/heads/*`) and remote branches (`refs/remotes/origin/*`) separately; exclude `main` and `master` by ref (e.g., `refs/heads/main`, `refs/remotes/origin/main`, etc.).
4. For each collected ref:
   a. Define `branch_ref` as the full ref name (e.g., `refs/heads/feature/foo` or `refs/remotes/origin/feature/foo`) and `branch_name` as the display name with the prefix stripped (e.g., `feature/foo`).
   b. Get last commit date via `git log -1 --format=%ai <branch_ref>`.
   c. Get author of last commit via `git log -1 --format=%an <branch_ref>`.
   d. Get author email via `git log -1 --format=%ae <branch_ref>`.
   e. Check merge status to main (or master) via `git merge-base --is-ancestor <branch_ref> origin/main` (or `origin/master` where appropriate).
   f. Get short commit message via `git log -1 --format=%s <branch_ref>`.
5. Filter candidates:
   - Collect branches older than max-age-days AND not merged to origin/main (or origin/master), using `branch_ref` for checks and `branch_name` for reporting.
   - Optionally include all branches with last-commit > max-age-days for reference.
6. Group by author to build contact list.
7. Report stale/unmerged branches with:
   - Branch name, last commit date, author, email, short message.
   - Merge status (in origin/main or not).
   - Suggested action (candidate for cleanup if old + unmerged).

## Constraints
- Never delete or modify branches; this is inspection only.
- Skip branches with active upstream tracking or recent activity (< 48 hours).
- Report unknown/system authors separately.
- Include estimated data collection time for transparency.

## Output Format
### Scan Summary
- Total branches checked (local and remote), total candidates.

### Contact Map
- Grouped by author: list of branches, dates, merge status, email.

### Cleanup Candidates
- Branches older than max-age AND unmerged: branch name, age, author, merge status, last message.

### Monitoring Notes
- Branches excluded (main/master), branches with active tracking, any scan errors.

### Suggested Contacts
- Authors with stale branches and their email list for outreach.

### Next Action
- One short action. Copilot example: type `/Cleanup Stale Branches` in chat to interactively remove confirmed candidates. Other tools: run the equivalent branch cleanup workflow.

### Summary
- Scan completed successfully with X candidates identified; contact [count] author(s).
