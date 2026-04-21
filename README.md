# fictional-goggles

## MCP Confluence configured

Project includes Cursor MCP config in `.cursor/mcp.json` using:

- `@aashari/mcp-server-atlassian-confluence`

### What to update

Open `.cursor/mcp.json` and set:

- `ATLASSIAN_SITE_NAME` (`your-company` from `https://your-company.atlassian.net`)
- `ATLASSIAN_USER_EMAIL`
- `ATLASSIAN_API_TOKEN` (create at `https://id.atlassian.com/manage-profile/security/api-tokens`)

### Usage

1. Save credentials in `.cursor/mcp.json`.
2. Reload Cursor window.
3. MCP server `confluence` will appear in Cursor.
