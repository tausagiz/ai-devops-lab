---
name: "Open PR"
description: "Sync the feature branch with main (merge or rebase), validate the entire PR, and push to create a GitHub PR."
agent: "PR Coach"
argument-hint: "Optional: context for the PR (e.g. reviewer, notes) or merge/rebase preference"
---
Prepare and push the current branch to open a pull request for this project.

First, ensure the feature branch is up to date with main:
- Check if the branch is behind main.
- If behind, ask whether you prefer `merge` or `rebase` to update (or accept the preference from the prompt arguments).
- Update the branch using the chosen strategy.

Then validate and create the PR:
- Run `python scripts/check_docs.py` to validate commit messages and docs gate across the entire PR scope.
- Derive a PR title from the commit subjects,
- Draft a PR body with Summary and Commits sections,
- Push the branch with `git push --set-upstream origin <branch>`,
- Create the PR with `gh pr create` if available, otherwise print the manual URL and the full PR body ready to paste.

If the worktree still has uncommitted changes, warn me and ask whether to commit them first using Prepare Commit.

If I provided extra context in the prompt arguments, include it in the PR body.
