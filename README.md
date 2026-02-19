# Fastn UCL + CrewAI Studio Demo

This folder contains everything used for Fastn UCL x CrewAI Studio

1. tool.py
Custom CrewAI Tool that forwards calls to Fastn UCL MCP server.

## Env vars required:
MCP_SERVER_URL
MCP_API_KEY

## Workflow (created in CrewAI Studio)
- Agent: Document Creator + Email Assistant
- Tool: UclMcpTool
- Task: Create Google Doc + Send Email

### Flow:
User -> CrewAI Agent -> UCL MCP -> Google Docs + Gmail

### Install:
pip install crewai crewai-tools requests

### Create tool:
crewai tool create ucl_mcp_tool

## Replace tool.py with this one.

## Publish:
git add .
git commit -m "UCL MCP tool"
crewai tool publish

Then attach the tool inside the CrewAI Studio Agent. Fastn UCL tool will then be available in the studio.
