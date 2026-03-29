#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path


def main():
    # Commit message check
    try:
        msg = (Path(".git/COMMIT_EDITMSG").read_text().strip())
    except FileNotFoundError:
        # in CI we can use git log for current commit
        import subprocess
        msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True).strip()

    msg_ok = re.match(r"^(feat|fix|docs|chore|refactor|test|build|ci)(\([a-zA-Z0-9_-]+\))?: .+", msg)
    if not msg_ok:
        print("❌ Invalid commit message format. Expected: type(scope): describe or type: describe")
        print("Example: docs(readme): update docs to reflect new command")
        print("or: docs: update docs to reflect new command")
        print("or: ci: update CI config")
        print(f"Got: {msg!r}")
        sys.exit(1)

    # Documentation checks
    readme = Path("README.md")
    agents = Path("AGENTS.md")

    if not readme.exists() or not agents.exists():
        print("❌ README.md and AGENTS.md are required.")
        sys.exit(1)

    # Require that at least one docs file is updated in the current diff,
    # to encourage attention to docs as code evolves.
    changed = []
    try:
        base = os.environ.get("GITHUB_BASE_REF")
        if base:
            changed = subprocess.check_output(["git", "diff", "--name-only", f"origin/{base}..HEAD"], text=True).strip().splitlines()
        else:
            # Get commit count to handle initial commit gracefully.
            commits = int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"], text=True).strip())
            if commits > 1:
                changed = subprocess.check_output(["git", "diff", "--name-only", "HEAD~1..HEAD"], text=True).strip().splitlines()
            else:
                # Initial commit: list files introduced by HEAD.
                changed = subprocess.check_output(["git", "show", "--name-only", "--pretty=", "HEAD"], text=True).strip().splitlines()
    except Exception:
        try:
            # Last fallback for staged changes if history is unavailable.
            changed = subprocess.check_output(["git", "diff", "--name-only", "--cached"], text=True).strip().splitlines()
        except Exception:
            changed = []

    if not any(f in ["README.md", "AGENTS.md"] for f in changed):
        print("❌ Docs update required: commit must include README.md or AGENTS.md changes.")
        print("Changed files:", changed)
        sys.exit(1)

    print("✅ Commit message and docs checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
