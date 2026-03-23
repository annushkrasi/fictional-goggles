# AGENTS.md

This file defines the default project instructions for coding agents (Cursor and other MCP-compatible agents).

## How to use this file

- Put your long system prompt in this file.
- Keep requirements concrete and testable.
- Prefer short sections with clear "do / don't" rules.
- Update this file when project conventions change.

## Project agent prompt template

Copy and edit this template:

```md
# Project Agent Instructions

## Role
You are the coding agent for this repository.

## Objectives
1. Implement requested changes end-to-end.
2. Keep behavior backward compatible unless explicitly requested.
3. Favor small, reviewable commits.

## Technical constraints
- Language/runtime:
- Frameworks:
- Allowed dependencies:
- Forbidden dependencies/tools:

## Code quality rules
- Follow existing project style and patterns.
- Keep functions focused and small.
- Add comments only for non-obvious logic.
- Do not introduce unrelated refactors.

## Testing and verification
- Run these checks before finishing:
  - ...
  - ...
- Add/adjust tests for behavior changes.
- If tests are skipped, explain why.

## Git workflow
- Work only on the current feature branch.
- Commit with clear messages.
- Do not rewrite history unless asked.

## Communication style
- Be concise and practical.
- Summarize changes with file paths.
- Mention risks and follow-ups explicitly.

## Project-specific rules
- ...
- ...
```

## Recommended sections for a "big prompt"

If you want a strong, detailed prompt, include:

1. Product context and domain terms
2. Architecture boundaries (what can/cannot change)
3. Security and data handling rules
4. Performance and reliability constraints
5. Testing matrix (unit/integration/e2e expectations)
6. Definition of done
7. Review checklist
8. Example "good" and "bad" answers

