---
name: "Open PR"
description: "Push the current feature branch to remote and create a GitHub PR with a drafted title and description based on the commits on this branch."
agent: "PR Coach"
argument-hint: "Optional: extra context for the PR, e.g. reviewer or notes"
---
Push the current branch to remote and open a pull request for this project.

Inspect all commits on this branch that are not yet on main, then:
- derive a PR title from the commit subjects,
- draft a PR body with Summary, Commits, and Checklist sections,
- push the branch with `git push --set-upstream origin <branch>`,
- create the PR with `gh pr create` if available, otherwise print the manual URL and the full PR body ready to paste.

If the worktree still has uncommitted changes, warn me and ask whether to commit them first.

If I provided extra context in the prompt arguments, include it in the PR body.
