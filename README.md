Fastn UCL + CrewAI Studio Demo

This folder contains everything used in the demo.

1. tool.py
Custom CrewAI Tool that forwards calls to Fastn UCL MCP server.

Env vars required:
MCP_SERVER_URL
MCP_API_KEY

2. Workflow (created in CrewAI Studio)
- Agent: Document Creator + Email Assistant
- Tool: UclMcpTool
- Task: Create Google Doc + Send Email

Flow:
User -> CrewAI Agent -> UCL MCP -> Google Docs + Gmail

Install:
pip install crewai crewai-tools requests

Create tool:
crewai tool create ucl_mcp_tool

Replace generated tool.py with this one.

Publish:
git add .
git commit -m "UCL MCP tool"
crewai tool publish

Then attach tool inside CrewAI Studio Agent.

That's it.
