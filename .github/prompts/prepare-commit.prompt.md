---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Follow commit and docs-gate rules from `AGENTS.md`. Use provided context to refine scope, title, and body.

If commit succeeds and all changes are committed:
- include one short, friendly sentence naming the next slash command (either `/Open PR` if this closes the work, or `/New Branch` if the user is starting *separate new work on a new branch*),
- then end with a `### Next Step` section followed immediately by a fenced code block containing only that slash command, formatted exactly like one of these examples:

  - For a final commit where you should open a PR:

    ### Next Step
    ```text
    /Open PR
    ```

  - For a commit where the user is starting *separate new work on a different branch*:

    ### Next Step
    ```text
    /New Branch
    ```
If the right next step is unclear from context, default to `/Open PR` and include one short note: "Assuming this closes current work — if you have more commits to add to *this* branch, just continue and re-run `/Prepare Commit`; if you are starting *separate new work*, run `/New Branch` instead." Always end with the `### Next Step` section; never omit it or replace it with a question.
