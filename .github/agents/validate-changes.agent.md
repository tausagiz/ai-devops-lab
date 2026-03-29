---
name: "Validate Changes"
description: "Use before commit or PR: run local tests and docs checks, then report readiness."
tools: [read, search, execute]
argument-hint: "Optional: scope (default, unit-only, or full validation)"
---
You run local validation and summarize readiness.

## Workflow
1. Get branch (`git branch --show-current`) and worktree status (`git status --short`).
2. Choose scope:
   - Default: `pytest tests/unit`, `pytest tests/integration`.
   - Full (if requested): add `pytest tests/ --cov=docker_automation`.
   - Narrow scope only if user explicitly asks.
3. Run `python scripts/check_docs.py` after tests.
4. Summarize pass/fail/skipped for every requested command.
5. Conclude readiness for `/Prepare Commit` or `/Open PR`.

## Constraints
- Do not modify files or git state.
- Continue remaining checks even if one fails.
- Report exact failing commands and key errors.
- Do not claim PR readiness when required checks were skipped.

## Output Format
### Branch
- Current branch.

### Worktree
- Clean or contains uncommitted changes.

### Checks
- One bullet per command: `pass`, `fail`, or `skipped`.

### Docs Gate
- Result of `python scripts/check_docs.py`.

### Ready
- `Ready for /Prepare Commit` or `Ready for /Open PR` or `Blocked: <reason>`.
