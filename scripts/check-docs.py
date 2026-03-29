#!/usr/bin/env python3
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

    msg_ok = re.match(r"^(feat|fix|docs|chore|refactor|test|build)(\([a-zA-Z0-9_-]+\))?: .+", msg)
    if not msg_ok:
        print("❌ Invalid commit message format. Expected: type(scope): describe")
        print("Example: docs(readme): update docs to reflect new command")
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
    try:
        changed = subprocess.check_output(["git", "diff", "--name-only", "HEAD~1..HEAD"], text=True).strip().splitlines()
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
