[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/edgarrmondragon-limesurvey-mcp-badge.png)](https://mseep.ai/app/edgarrmondragon-limesurvey-mcp)

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
      // For example, /Users/<YOUR USERNAME>/.local/bin/uv
      "command": "/path/to/uv",
      "args": [
        "--directory",
        // For example, /Users/<YOUR USERNAME>/mcp-servers/limesurvey-mcp
        "/path/to/limesurvey-mcp",
        "run",
        "main.py"
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
