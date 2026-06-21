# 🧠 RAG Agent System using LangChain + Tavily + Chroma

An advanced **AI Agent system** that combines **Retrieval-Augmented Generation (RAG)** with **tool-based reasoning** using LangChain.

This project allows an AI assistant to:
- Retrieve information from a PDF (knowledge base)
- Perform web search using Tavily API
- Act like an intelligent agent that decides which tool to use

---

## 🚀 Features

- 📄 PDF-based knowledge retrieval (RAG system)
- 🔍 Web search integration using Tavily API
- 🧠 Vector database using ChromaDB
- 🤖 LLM-powered agent using Gemini (via LangChain)
- 🧩 Tool-based reasoning system
- 💬 Conversational AI agent behavior

---

## 🧠 What This Project Does

This AI agent can:

- Answer questions from a research paper (Attention Is All You Need)
- Search external web sources when needed
- Decide automatically which tool to use
- Combine multiple information sources for better answers

---

## 🏗️ Tech Stack

- Python
- LangChain
- LangGraph / Agents
- Google Gemini API
- ChromaDB (Vector Database)
- Tavily Search API
- HuggingFace Embeddings
- PyPDF

---

## 📂 Project Structure


app.py → Main agent logic
tools.py → Custom tools (PDF + web search)
data/ → PDF documents
chroma_db/ → Vector database storage
requirements.txt → Dependencies
.env.example → API keys template


---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/rag-agent-langchain-tavily-chroma.git
cd rag-agent-langchain-tavily-chroma
2. Install dependencies
pip install -r requirements.txt
3. Add API keys

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
4. Add PDF file

Place your document inside:

data/attention_is_all_you_need.pdf
5. Run the project
python app.py
💡 How It Works
Step 1: User asks a question

Example:

What is self-attention in transformers?

Step 2: Agent decides action
Use PDF RAG → if question is about document
Use Tavily search → if external knowledge is needed
Step 3: Retrieval
Relevant chunks are fetched from ChromaDB
Step 4: Response generation
Gemini LLM generates final structured answer
🧠 Key Concepts Used
Retrieval-Augmented Generation (RAG)
Vector Embeddings
Semantic Search
Tool Calling Agents
Multi-source reasoning