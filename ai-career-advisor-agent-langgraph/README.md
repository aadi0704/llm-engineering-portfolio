# AI Career Advisor Agent (LangGraph + Gemini + Tools)

An advanced AI agent that acts as a **career advisor**, helping students analyze skill demand and find real job opportunities using multiple tools and LLM reasoning.

---

## 🚀 Features

- 🧠 Powered by Google Gemini 2.5 Flash
- 🔗 LangGraph Agent with memory
- 🔍 Web search via Tavily API
- 💼 Real-time job search via RapidAPI (JSearch)
- 🧩 Tool-based reasoning (Agentic AI system)
- 💬 Multi-turn conversation memory

---

## 🧠 What This Project Does

This AI agent can:
- Analyze demand for skills like AI, ML, Web Dev, etc.
- Search real job openings in India and globally
- Explain career trends
- Continue conversation with memory
- Answer follow-up questions like “tell me more about job 2”

---

## 🏗️ Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini API
- Tavily Search API
- RapidAPI (JSearch)
- Requests

---

## 📂 Project Structure


app.py → Main AI agent logic
tools/ → Custom tools (job search)
requirements.txt → Dependencies
.env.example → API keys template


---

## ⚙️ Setup Instructions

### 1. Clone repo

git clone https://github.com/your-username/ai-career-advisor-agent-langgraph.git
cd ai-career-advisor-agent-langgraph


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add API keys
Create `.env` file:

GEMINI_API_KEY=your_key
TAVILY_API_KEY=your_key
RAPIDAPI_KEY=your_key


---

### 4. Run project

python app.py


---

## 💡 How It Works

1. User asks career-related question
2. Agent decides which tool to use:
   - Skill demand → Tavily search
   - Jobs → RapidAPI tool
3. Results are combined by LLM
4. Memory allows follow-up questions

---

## 📌 Example Use Case

Input:
> What is demand for Generative AI in India?

Output:
- Industry demand summary
- Job listings (titles, companies, links)

Follow-up:
> Tell me more about second job

Agent remembers previous results and responds correctly.

---

## 🚀 Future Improvements

- Add resume analyzer
- Add salary prediction model
- Add LinkedIn job scraping
- Add Streamlit UI
- Deploy as web app

---

## 👨‍💻 Author

AI/ML + LLM Agent project for portfolio showcasing real-world tool-based AI systems.