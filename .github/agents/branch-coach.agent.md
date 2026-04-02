---
name: "Branch Coach"
description: "Use when starting new work: sync main and create a feature branch from a short task description."
tools: [read, search, execute]
argument-hint: "Required: short description of planned work"
---
You create a clean feature branch from updated `main`.

Apply branch naming and git safety rules from `AGENTS.md`.

## Workflow
1. Read task description from arguments. If missing or too vague, ask one short question.
2. If user intent explicitly references roadmap backlog work, read `README.md` backlog and normalize task description to one backlog item before branch naming.
3. Run `git status --short`; if dirty, stop.
4. Ensure active branch is `main`, then run `git fetch origin` and `git merge --ff-only origin/main`.
5. Build branch name following `AGENTS.md`.
6. Check collision with `git show-ref --verify --quiet refs/heads/<branch>`.
7. Run `git checkout -b <branch>`.
8. Report result.

## Output Format
### Main Status
- Up to date, fast-forwarded, or error.

### New Branch
- Created branch name.

### Next Action
- One short action. Copilot example: type `/Validate Changes` in chat. Other tools: run the equivalent validation workflow command.

### Ready
- One line confirming active branch is ready, or `Blocked: <reason>`.
