---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Follow commit and docs-gate rules from `AGENTS.md`. Use provided context to refine scope, title, and body.

If commit succeeds and all changes are committed:
- include one short, friendly sentence naming the next slash command (either `/Open PR` if this closes the work, or `/New Branch` if more work is planned),
- then end with a `### Next Step` section followed immediately by a fenced code block containing only that slash command, formatted exactly like one of these examples:

  - For a final commit where you should open a PR:

    ### Next Step
    ```bash
    /Open PR
    ```

  - For a commit where more work on a new branch is planned:

    ### Next Step
    ```bash
    /New Branch
    ```
If the right next step is unclear from context, ask briefly: "Is this the final commit for this branch, or do you have more changes planned?", and by default assume this is the final commit: still end with a `### Next Step` section using `/Open PR` as the command block, and include one short note that you are assuming it is ready to open a PR unless the user says otherwise.
