import os
import requests
from crewai_tools import BaseTool

class UclMcpTool(BaseTool):
    name = "ucl_mcp_tool"
    description = "Calls Fastn UCL MCP server tools."

    def _run(self, *args, **kwargs):
        payload = None
        if args:
            first = args[0]
            if isinstance(first, dict):
                payload = first
            elif isinstance(first, str) and len(args) > 1 and isinstance(args[1], dict):
                payload = {"tool": first, "input": args[1]}
            else:
                payload = {}
        else:
            payload = kwargs or {}

        if isinstance(payload, dict) and "argument" in payload:
            payload = payload["argument"]

        tool_name = payload.get("tool") or payload.get("tool_name") or payload.get("name")
        input_dict = payload.get("input") or payload.get("params") or payload.get("arguments") or {}

        if not tool_name:
            return {"error": "Missing tool name"}

        base_url = os.environ.get("MCP_SERVER_URL")
        api_key = os.environ.get("MCP_API_KEY")

        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        payload_out = {"tool": tool_name, "input": input_dict}

        try:
            r = requests.post(base_url, json=payload_out, headers=headers, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            return {"error": str(e)}
