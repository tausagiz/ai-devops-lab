---
name: "Roadmap Sync"
description: "Refresh README roadmap buckets after implemented work by closing completed items and keeping backlog actionable."
agent: "Roadmap Coach"
argument-hint: "Optional: implemented items, PR/issue refs, or roadmap notes"
---
Synchronize the roadmap snapshot in `README.md`.

Use roadmap rules from `AGENTS.md`.

Expectations:
- Keep edits compact and only in roadmap-relevant sections unless explicitly requested.
- Close or move completed items to `Done Recently`.
- Keep `Backlog` actionable and avoid duplicate items across buckets.
- If mapping implemented changes to roadmap items is ambiguous, ask one concise clarification.
