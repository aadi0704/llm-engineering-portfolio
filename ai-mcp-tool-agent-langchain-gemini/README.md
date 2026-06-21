# 🧠 MCP Agent with Gemini + Composio (Tavily Tools)

An advanced AI Agent system built using **Model Context Protocol (MCP)** that connects Gemini LLM with external tools like web search via Composio.

---

## 🚀 Features

- 🤖 Gemini 2.5 Flash LLM integration
- 🔗 MCP (Model Context Protocol) support
- 🌐 Web search using Tavily via Composio MCP server
- 🧩 Multi-server tool architecture
- ⚡ Dynamic tool usage by AI agent
- 🧠 Intelligent query reasoning system

---

## 🧠 What This Project Does

This AI agent can:

- Connect to external MCP servers
- Use tools like web search dynamically
- Understand user queries using Gemini
- Fetch real-time information from internet tools
- Act like a smart autonomous assistant

---

## 🏗️ Tech Stack

- Python
- LangChain
- MCP (Model Context Protocol)
- Google Gemini API
- Composio MCP Server
- Tavily Search Tool

---

## 📂 Project Structure


app.py → Main agent logic
mcp_config.py → MCP server configuration
requirements.txt → Dependencies
.env.example → API keys
notes/ → Setup notes


---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/mcp-agent-skillmap-gemini-composio.git
cd mcp-agent-skillmap-gemini-composio
2. Install dependencies
pip install -r requirements.txt
3. Add API keys

Create .env file:

GEMINI_API_KEY=your_key
COMPOSIO_API_KEY=your_key
4. Run project
python app.py
💡 How It Works
User sends a query
Gemini LLM interprets the request
MCP client connects to external tool servers
Tools (like Tavily search) are called if needed
Final response is generated
📌 Use Cases
AI research assistant
Real-time web intelligence agent
Tool-augmented LLM systems
MCP-based AI applications
Autonomous AI agents