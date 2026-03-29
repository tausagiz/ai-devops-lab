---
name: "Open PR"
description: "Sync branch with main, run validation, push, and open or prepare a GitHub PR."
agent: "PR Coach"
argument-hint: "Optional: PR context plus merge/rebase preference"
---
Prepare and open a pull request for the current branch.

If branch is behind `main`, update using merge/rebase preference. Run validation (`pytest tests/unit`, `pytest tests/integration`, `python scripts/check_docs.py`; plus coverage test only when requested). If I passed extra PR context, include it in the PR body. If checks pass, push and create PR via `gh` or provide manual URL/body fallback.
