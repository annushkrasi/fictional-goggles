# AGENTS.md

Guidance for coding agents working in this repository.

## Project purpose

This is a minimal repo for configuring a Cursor MCP server for Atlassian Confluence.
Primary files:

- `README.md`
- `.cursor/mcp.json`

## Working rules

1. Keep changes focused and minimal.
2. Prefer updating docs/config directly over broad refactors.
3. Preserve valid JSON formatting in `.cursor/mcp.json`.
4. Do not commit real credentials, tokens, or other secrets.
5. If example values are needed, use obvious placeholders.

## Validation checklist

After editing `.cursor/mcp.json`, run a quick JSON validation:

```bash
python -m json.tool .cursor/mcp.json >/dev/null
```

Also confirm `README.md` still matches the configuration flow.

## Commit guidance

- Use clear, scoped commit messages.
- Include only relevant file changes.
- Avoid unrelated formatting-only edits.
