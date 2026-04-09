---
description: "Use when writing or reviewing Python source code in src/. Covers module boundaries, constants, and lightweight implementation patterns for course-aligned code."
applyTo: "src/**/*.py"
---
# Python Source Conventions

- Keep implementations small and topic-focused; avoid cross-module coupling between unrelated course areas.
- Centralize repeated runtime constants in one module per topic and import from there.
- Prefer pure functions where possible so examples are easy to test and reuse.
- Use explicit return types on public functions.
- Handle operational errors clearly and fail with actionable messages.
- Keep comments concise and only where logic is not obvious.
