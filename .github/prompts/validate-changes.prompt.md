---
name: "Validate Changes"
description: "Run local validation for the current branch before commit or PR, including tests and docs-gate readiness."
agent: "Validate Changes"
argument-hint: "Optional: validation scope, e.g. unit only or full validation"
---
Validate the current branch before I commit or open a pull request.

By default, run the repository's local checks:
- `pytest tests/unit`
- `pytest tests/integration`
- `python scripts/check_docs.py`

If I explicitly ask for full validation, also run `pytest tests/ --cov=docker_automation`.

Report:
- The current branch,
- Whether the worktree has uncommitted changes,
- Which checks passed, failed, or were skipped,
- Whether the branch is ready for `/Prepare Commit` or `/Open PR`.