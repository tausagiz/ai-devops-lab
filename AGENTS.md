# AGENTS

Short guide for agents working in this repository.

## Repository character

- Educational sandbox for Docker automation and AI workflow testing.
- Risk is intentionally very low: fast and cheap experiments are more important than production-hard process rigor.
- The repo is used to compare multiple tools, especially those with free limits or cost tied to tokens/calls.
- Instructions should stay short and non-duplicative to reduce context cost.

## Work priorities

- Prefer small, reversible changes and short validation loops.
- Start with the cheapest checks: `pytest tests/unit`, `pytest tests/integration`, then coverage or more expensive steps.
- Minimize context: read only needed files and avoid duplicating the same rules across many instructions.
- Do not overengineer; this repo is for experimentation.

## Token-efficiency policy

- Keep responses compact by default: report outcomes first, include only necessary detail, and avoid long explanations unless the user asks.
- Do not create extra Markdown/docs files, new tests, or helper scripts by default.
- If adding docs/tests/scripts could improve quality but is not explicitly requested, stop and ask for user confirmation first.
- Prefer editing existing files over introducing new files.
- Before running broader validation, heavy analysis, or multi-step refactors not explicitly requested, ask for confirmation and suggest the cheapest next check.

## Project map

- `src/docker_automation/cli.py` - CLI entry point and command routing.
- `src/docker_automation/config.py` - constants (`IMAGE_TAG`, `BUILD_PATH`).
- `src/docker_automation/docker_client.py` - `get_client()` factory.
- `src/docker_automation/commands/*.py` - command implementations.
- `tests/unit/` - unit tests (Docker SDK mocked).
- `tests/integration/` - CLI smoke tests.
- `scripts/check_docs.py` - commit message + docs gate validation.

## Repository rules

- Implementation: access Docker only through `get_client()`; keep constants in `config.py`; each new command must live in `commands/` and be registered in `cli.py`.
- Language: developers may chat in any language, but all repository artifacts must be in English (code, comments, docstrings, variable/function names, CLI messages, tests, documentation, commit/PR descriptions).
- Branches: create a new branch only from up-to-date `main`; dirty worktree blocks branch switching and should return a short transfer handoff (commit/stash current changes, then rerun `/Branch Start`); format `type/short-slug`; allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`; slug lowercase, hyphen-separated, 2-4 meaningful words, no type duplication; when the task description is too generic, return exactly 3 numbered branch suggestions and allow selection by number (`1`/`2`/`3`) instead of guessing.
- Commits: only `/Prepare Commit` workflow may auto-create a commit; other workflows must not commit or push without explicit request; title format `type(scope): summary` or `type: summary`; docs gate for code changes requires `README.md` or `AGENTS.md`; docs-gate auto-fix is allowed only by staging already existing changes in those files; do not create new documentation content only to pass the gate; with mixed scope, stop and ask for confirmation.
- Validation and PR: by default run `pytest tests/unit`, `pytest tests/integration`, `python scripts/check_docs.py`; narrower scope only on explicit request and then clearly state what was skipped; full validation only on explicit request (`pytest tests/ --cov=docker_automation`); target PR to `main` by default; if branch is behind `main`, ask for `merge` or `rebase` unless preference is already explicit; before push, stop on dirty worktree and suggest `/Prepare Commit`; include extra PR context in the body.
- User confirmation guardrail: when a proposed action increases token/call usage or project surface (new files, broader tests, extra scripts, large documentation updates), ask for explicit confirmation before proceeding unless already requested.
- Branch closing: never delete `main` or `master`; delete only branches merged into `origin/main` unless user explicitly confirms risky operation; when merge state is uncertain or `-D` would be needed, stop and wait for confirmation; never force-push or force-delete without explicit request.

## Tooling integration

- `AGENTS.md` is the repo-neutral layer and the primary source of rules for any agent.
- Files in `.github/agents/` and `.github/prompts/` are thin wrappers for slash commands, `argument-hint`, and response format; kept minimal to preserve token budget.
- Copilot-specific note: commands shown as `/Command` are GitHub Copilot Chat slash commands (type them in chat input).
- Other AI tools may require different syntax (for example plain text commands, menu actions, or different prefixes).
- If a rule applies to the whole repo, keep it here; in Copilot files keep only what is necessary to run the workflow.

## Next Action UX Policy

- Every workflow response must include one short, friendly `Next Action` suggestion.
- Keep it concise: one action only, no long decision trees.
- If blocked, suggest the cheapest unblock step.
- If action is command-based, include a short invocation hint.
- For Copilot wrappers, use slash command examples.
- For other tools, keep the same intent and adapt syntax to that tool.
- Section naming: generic workflows should prefer a `### Next Action` heading; workflows explicitly required to end with `### Next Step` (for example `/Prepare Commit`) MUST treat that section as their `Next Action` and are considered compliant with this policy.

## Roadmap Hygiene Policy

- Keep roadmap visibility in `README.md` under a dedicated `## Roadmap` section with buckets: `Current Focus`, `Next Up`, `Backlog`, `Done Recently`.
- When work implements a roadmap item, update roadmap status in the same change: remove or mark completed from active buckets and add to `Done Recently`.
- When user asks to start work from backlog, first pick one explicit backlog item, then run branch-start workflow for that item (do not pick multiple backlog items at once unless user explicitly asks).
- If roadmap status is stale or unclear after implementation, run a roadmap sync step before commit/PR (or stop and ask for confirmation when mapping is ambiguous).
- Keep roadmap updates concise; do not add large planning documents by default.

## Scope Drift Decision Policy

- Goal: keep PRs reviewable without forcing unnecessary branch splits.
- `low` drift: branch name and changes are aligned; proceed normally.
- `medium` drift: changes are still one coherent topic but broader than branch name; suggest branch re-scope first (rename branch), and use an explicit PR scope note as fallback when rename is not practical.
- `high` drift: multiple unrelated topics, or PR would be hard to review due to size/surface; split is recommended before commit/PR.
- Reviewability heuristics for `high`: mixed unrelated domains, many independent intents, or large surface with weak thematic cohesion.
- If user intentionally keeps a broader but coherent scope, allow continuation after explicit confirmation and require clear PR summary of included subtopics.

## Vendor-agnostic policy

- Prefer vendor-neutral conventions and references in shared instructions (for example `#file:AGENTS.md` as the canonical rule source for automation).
- Keep provider-specific capabilities (tool names, frontmatter keys, slash-command wiring, platform-only metadata) in provider-scoped wrapper files only.
- Provider-scoped files must stay minimal adapters and must not duplicate agent workflow policy from `AGENTS.md`.
- When provider-specific behavior is documented in generic sections, explicitly label it (for example `Copilot-specific note`) and add a short sentence that other tools may need different syntax.
- When adding or changing automation guidance, update the universal rule in `AGENTS.md` first, then reference it from tool/vendor-specific files.
- Design new instruction/tool structures so another tool can adopt the same universal base without rewriting agent workflow policy.

## New Tool Onboarding

- At the start of onboarding a new AI tool, run a quick capability-gap check against this repo workflow primitives.
- Compare these capabilities explicitly: workflow command entry, prompt equivalent, agent/subagent equivalent, tool execution permissions, branch/commit/PR automation, and validation runner behavior.
- If any capability is missing or partially mapped, report it immediately and suggest the smallest implementation steps needed.
- Ask one explicit question before implementing gaps: is this a test-only evaluation or a real onboarding for adoption?
- If user chooses test-only evaluation, do not force implementation; keep working and include a short `Deferred onboarding gaps` list in the result.
- If evaluation succeeds and adoption is intended, remind the user to implement deferred gaps before merge/release and include one concrete next command or task.

## Session Focus & Context Shift Policy

- **Session Focus Rule**: Agents must maintain focus on the current session's primary goal to preserve model context coherence.
- **Context Shift Detection**: When a user's requests drift dramatically from the session's established direction (e.g., switching from workflow automation to unrelated feature work, or from this repo to a different codebase topic), the agent should pause and assess whether a new session is needed.
- **Drift Indicators (suggest new session if multiple appear)**:
  - Request involves a completely different domain or codebase area unrelated to prior context.
  - User explicitly states intent to work on something new or separate.
  - Conversation has spanned many unrelated subtopics without thematic cohesion.
  - Token context is at risk of dilution due to context switching.
- **Recommendation Pattern**: When context shift is detected, offer: "It looks like you're shifting to [new topic], which is quite different from [session direction]. Would you like to start a fresh session? This helps the model maintain sharper focus on the new goal. You can always reference these changes later by commit SHA or branch name if needed."
- **Boundary Between Subtasks vs New Session**: Continuing work on related subtasks within the same logical context (e.g., commit → PR → branch cleanup, or testing → refactor → PR all for same feature) is one session. Switching to an unrelated goal in parallel is a new session.

## Workflow entrypoints

For GitHub Copilot Chat, use the simplest entrypoint for the job:
- Prompt-first lightweight workflows via slash commands (`/Command`).
- Agent-first complex workflows via direct agent mentions (`@Agent Name`).
If you use another tool, keep the same workflow intent and adapt invocation syntax.

Core default lane (use these for day-to-day feature delivery):
- `@Branch Coach` - update `main` and create a feature branch. If task text is missing or vague, return exactly 3 numbered suggestions and allow selection by number.
- `@Validate Changes` - run local tests + docs gate and the primary scope-drift sanity check before readiness output.
- `@Commit Coach` - prepare and create commit with docs gate and next-step guidance.
- `@PR Coach` - sync branch, push, and create or refresh PR details. Reuse recent validate/scope context by default; re-run checks only when explicitly requested.
- `/Close Branch` - close merged branch safely and return to `main`.

Advanced on-demand lane (use when needed):
- `/Workflow Help` - list available workflow entrypoints.
- `/Check Scope` - assess scope drift against branch intent and recommend rename/re-scope vs split.
- `/Rescope Branch` - rename current branch to match coherent scope drift.
- `/Fix Validation` - diagnose and fix failed validation checks, then rerun impacted checks.
- `@Split Scope` - safely split a high, non-cohesive drift branch while preserving original and backup branches.
- `@Roadmap Coach` - roadmap sync and roadmap hygiene updates.
- `@Branch Cleanup Report` - scan branches periodically and build author contact map.
- `@Cleanup Stale Branches` - interactively delete confirmed stale branches with audit trail.
- `@Learning Coach` - run a structured learning workflow: mandatory problem discovery, adaptive tasks, and test-based or rubric-based validation.
## Agent maintenance rule

- When adding, removing, or renaming workflow files in `.github/agents/` or `.github/prompts/`, update this workflow list and `.github/prompts/workflow-help.prompt.md` in the same change.
- Keep roadmap workflow entrypoints (`@Roadmap Coach`) aligned with the `## Roadmap` section structure in `README.md`; if bucket names change, update the corresponding agent and wrappers in the same commit.
- Keep the Copilot-specific slash-command note accurate when command names change.
- Keep `Commit Coach` UX rule: successful output must include one short usage hint before the `### Next Step` block; next step should be chosen dynamically based on user intent and session context.
- Apply `Next Action UX Policy` to every existing and new workflow wrapper.
- If adding support wrappers for another tool, add or update an equivalent workflow-command index and tool-specific invocation note in the same change.
- When updating PR Coach's PR body edit step, preserve the `gh api` REST fallback for environments where `gh pr edit` fails with deprecation errors; document both methods in the agent.
