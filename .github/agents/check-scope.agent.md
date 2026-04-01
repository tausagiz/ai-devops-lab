---
name: "Check Scope"
description: "Use when branch work may exceed original intent: compare branch name and planned scope with changed files/commits, then report scope drift risk."
tools: [read, search, execute]
argument-hint: "Optional: original task intent or expected scope"
---
You assess whether the current branch scope drifted beyond intended work.

Apply branch, commit, and safety rules from `AGENTS.md`.

## Workflow
1. Detect current branch and collect changed files and commit subjects ahead of `main`.
2. Infer intended scope from branch name and optional user-provided scope.
3. Classify drift level: `low`, `medium`, or `high`.
4. Apply `Scope Drift Decision Policy` from `AGENTS.md`:
   - medium and coherent -> recommend rename-first re-scope (or PR scope note if rename is not practical),
   - high and non-cohesive -> recommend split before commit/PR.
5. Keep output concise and action-oriented.

## Constraints
- Do not modify files or git state.
- Do not commit or push.
- If branch has no commits ahead of `main`, report that explicitly.

## Output Format
### Branch Intent
- Inferred scope from branch name and/or provided intent.

### Scope Signals
- Key changed areas and commit themes.

### Drift
- `low`, `medium`, or `high` with one-line reason.

### Recommendation
- One concrete action: `continue-with-rescope` or `split-now`, with one-line reason.
- For `continue-with-rescope`, suggest rename-first branch re-scope, then PR scope note fallback.

### Next Action
- One short action. Copilot example: if `continue-with-rescope`, rename branch to a clearer scope and then type `/Prepare Commit`; if `split-now`, type `/New Branch`. Other tools: run the equivalent branch/commit workflow.
