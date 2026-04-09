---
name: "Learn"
description: "Start or resume a diagnostic-first learning session that maps a real problem to skill goals and adaptive validation."
argument-hint: "Optional: real problem context"
---
Start a compact learning session for this repository.

Workflow rules:
- First session for a course must run discovery before task generation.
- Discovery must produce: problem map, skill-gap map, success criteria, and scope rails.
- Do not generate the first task until discovery summary is confirmed.
- For each task, choose one validation mode: `test_mode`, `rubric_mode`, or `hybrid_mode`.
- Prefer test-based validation when the outcome is deterministic and automatable.
- If tests cannot be auto-run, provide one manual run command fallback.
- Keep each response concise and action-oriented.

If no active course exists, create one from the discovery interview.
If an active course exists, resume from the latest state and propose one next task.

End with exactly one recommended next action.
