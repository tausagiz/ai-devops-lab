---
name: "Validate Changes"
description: "Run local checks for the current branch and report readiness for commit or PR."
agent: "Validate Changes"
argument-hint: "Optional: validation scope (default, narrow, full)"
---
Validate this branch before commit or PR.

Default checks: `pytest tests/unit`, `pytest tests/integration`, `python scripts/check_docs.py`. Add `pytest tests/ --cov=docker_automation` only when full validation is requested.

Report branch, worktree state, each check status, and readiness for `/Prepare Commit` or `/Open PR`.
