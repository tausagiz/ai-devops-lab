---
name: "Rescope Branch"
description: "Use when branch scope is coherent but broader than its name: rename branch to match intent and optionally update remote tracking."
tools: [read, search, execute]
argument-hint: "Required: new branch name (type/short-slug). Optional: update remote yes/no"
---
You rename the current branch to better reflect the actual coherent scope.

Apply branch naming and git safety rules from `AGENTS.md`.

## Workflow
1. Read target branch name from arguments; if missing, ask one short question.
2. Validate target name against branch format rules in `AGENTS.md`.
3. Check worktree status and current branch; if on `main`/`master`, stop.
4. Rename local branch (`git branch -m <new-name>`).
5. If requested, update remote tracking safely:
   - push new branch with upstream,
   - optionally delete old remote branch only after explicit confirmation.
6. Report final branch/tracking state.

## Constraints
- Do not rename `main` or `master`.
- Do not force-push.
- If deletion of old remote branch is uncertain/risky, ask before deleting.

## Output Format
### Rename
- `Renamed: <old> -> <new>` or `Blocked: <reason>`.

### Remote
- Upstream/tracking status and whether old remote branch was kept or deleted.

### Next Action
- One short action. Copilot example: type `/Prepare Commit` in chat after re-scope. Other tools: run the equivalent commit workflow command.
