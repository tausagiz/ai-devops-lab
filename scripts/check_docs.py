#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def git_output(args):
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def check_copyright_year():
    """Verify LICENSE file copyright year is current."""
    import datetime

    license_file = REPO_ROOT / "LICENSE"
    if not license_file.exists():
        return True  # Skip if no LICENSE yet

    current_year = datetime.datetime.now().year
    license_content = license_file.read_text()

    # Extract copyright year(s) from "Copyright (c) 2026" or "Copyright (c) 2026-2027"
    copyright_match = re.search(r"Copyright \(c\) (\d{4})(?:-(\d{4}))?", license_content)

    if not copyright_match:
        print("⚠️  LICENSE file missing copyright year. Expected: Copyright (c) YYYY")
        return False

    start_year = int(copyright_match.group(1))
    end_year = int(copyright_match.group(2)) if copyright_match.group(2) else start_year

    if end_year < current_year:
        print(f"⚠️  COPYRIGHT YEAR STALE: LICENSE shows {start_year}-{end_year}, current year is {current_year}")
        print(f"   Update to: Copyright (c) {start_year}-{current_year}")
        print(f"   Or if this is fresh work: Copyright (c) {current_year}")
        return False

    return True


def main():
    # Commit message check
    try:
        msg = ((REPO_ROOT / ".git" / "COMMIT_EDITMSG").read_text().strip())
    except FileNotFoundError:
        # in CI we can use git log for current commit
        import subprocess

        msg = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B"],
            text=True,
            cwd=REPO_ROOT,
        ).strip()

    # GitHub creates merge commits like "Merge <sha> into <sha>" on some flows.
    # Skip conventional-commit validation for those auto-generated messages.
    is_merge_commit = msg.startswith("Merge ")
    msg_ok = re.match(r"^(feat|fix|docs|chore|refactor|test|build|ci)(\([a-zA-Z0-9_-]+\))?: .+", msg)
    if not msg_ok and not is_merge_commit:
        print("❌ Invalid commit message format. Expected: type(scope): describe or type: describe")
        print("Example: docs(readme): update docs to reflect new command")
        print("or: docs: update docs to reflect new command")
        print("or: ci: update CI config")
        print(f"Got: {msg!r}")
        sys.exit(1)

    # Documentation checks
    readme = REPO_ROOT / "README.md"
    agents = REPO_ROOT / "AGENTS.md"

    if not readme.exists() or not agents.exists():
        print("❌ README.md and AGENTS.md are required.")
        sys.exit(1)

    # Require that at least one docs file is updated in the current diff,
    # to encourage attention to docs as code evolves.
    changed = []
    base = os.environ.get("GITHUB_BASE_REF")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    base_sha = os.environ.get("GITHUB_BASE_SHA")
    head_sha = os.environ.get("GITHUB_HEAD_SHA")
    before_sha = os.environ.get("GITHUB_BEFORE_SHA")
    current_sha = os.environ.get("GITHUB_SHA")

    changed_out = None

    if event_name == "pull_request" and base_sha and head_sha:
        # PR: compare exactly base..head from the event payload.
        changed_out = git_output(["diff", "--name-only", f"{base_sha}...{head_sha}"])

    if changed_out is None and event_name == "push" and before_sha and current_sha:
        # Push: compare exactly previous..current commit from the event payload.
        changed_out = git_output(["diff", "--name-only", f"{before_sha}..{current_sha}"])

    if changed_out is None and base:
        # PR in CI: fallback to remote base branch when event SHAs are unavailable.
        changed_out = git_output(["diff", "--name-only", f"origin/{base}..HEAD"])

    if changed_out is None:
        # Works for typical local commits and many CI push builds.
        changed_out = git_output(["diff", "--name-only", "HEAD~1..HEAD"])

    if changed_out is None:
        # Initial commit or very shallow history: inspect files from HEAD commit.
        changed_out = git_output(["show", "--name-only", "--pretty=", "HEAD"])

    if changed_out is None:
        # Last fallback for local pre-commit checks.
        changed_out = git_output(["diff", "--name-only", "--cached"])

    if changed_out:
        changed = changed_out.splitlines()

    if not any(f in ["README.md", "AGENTS.md"] for f in changed):
        print("❌ Docs update required: commit must include README.md or AGENTS.md changes.")
        print("Changed files:", changed)
        sys.exit(1)

    # Copyright year check
    if not check_copyright_year():
        print("⚠️  License copyright year is stale.")

    print("✅ Commit message and docs checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
