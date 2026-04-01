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
3. Collect local branches and remote branches; exclude `main` and `master`.
4. For each branch:
   a. Get last commit date via `git log -1 --format=%ai <branch>`.
   b. Get author of last commit via `git log -1 --format=%an <branch>`.
   c. Get author email via `git log -1 --format=%ae <branch>`.
   d. Check merge status: `git merge-base --is-ancestor <branch> origin/main`.
   e. Get short commit message via `git log -1 --format=%s <branch>`.
5. Filter candidates:
   - Collect branches older than max-age-days AND not merged to origin/main.
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
