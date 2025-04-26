# LimeSurvey MCP Server

This is an MCP server for LimeSurvey. It is a simple server that allows you to manage your LimeSurvey surveys and responses.

## Configuration

| Name | Description |
|------|-------------|
| LIMESURVEY_URL | The URL of your LimeSurvey instance, e.g. `https://myinstance.limequery.com/admin/remotecontrol` |
| LIMESURVEY_USERNAME | Your LimeSurvey username |
| LIMESURVEY_PASSWORD | Your LimeSurvey password |

## Using with MCP clients

```json
{
  "mcpServers": {
    "limesurvey-mcp": {
      "command": "/Users/<YOUR USERNAME>/.limesurvey-mcp/.venv/bin/mcp",
      "args": [
        "run",
        "/Users/<YOUR USERNAME>/.limesurvey-mcp/.venv/lib/python3.12/site-packages/limesurvey_mcp/main.py"
      ],
      "env": {
        // see config above
        // "LIMESURVEY_URL": "https://myinstance.limequery.com/admin/remotecontrol"
        // "LIMESURVEY_USERNAME": "myusername"
        // "LIMESURVEY_PASSWORD": "mypassword"
      }
    }
  }
}
```
