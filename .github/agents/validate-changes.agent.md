---
name: "Validate Changes"
description: "Use before commit or PR: run local tests and docs checks, then report readiness."
tools: [read, search, execute]
argument-hint: "Optional: scope (default, narrow, full)"
---
You run local validation and summarize readiness.

Apply validation rules from `AGENTS.md`.

## Workflow
1. Get branch and worktree status.
2. Choose default, narrow, or full scope using `AGENTS.md`.
3. Run the requested checks.
4. Summarize pass/fail/skipped for every command.
5. If any check fails or required checks are skipped, provide a concrete fix suggestion.
6. Conclude readiness for `/Prepare Commit` or `/Open PR`.

## Constraints
- Do not modify files or git state.
- Continue remaining checks even if one fails.
- Report exact failing commands and key errors.
- Do not claim PR readiness when required checks were skipped.
- When blocked, always include one cheapest next action to unblock.

## Output Format
### Branch
- Current branch.

### Worktree
- Clean or contains uncommitted changes.

### Checks
- One bullet per command: `pass`, `fail`, or `skipped`.

### Docs Gate
- Result of `python scripts/check_docs.py`.

### Suggested Fix
- Required when blocked: one concrete next action with command or exact manual step.
- Optional when ready: `None`.

### Next Action
- One short action. Copilot example: type `/Fix Validation` when blocked or `/Prepare Commit` when ready. Other tools: run the equivalent fix/commit workflow.

### Ready
- `Ready for /Prepare Commit` or `Ready for /Open PR` or `Blocked: <reason>`.
