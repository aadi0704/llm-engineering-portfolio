# 🎮 AI Game Development Crew (CrewAI + Gemini)

An advanced multi-agent AI system that automatically **designs and generates full Python Pygame games** using CrewAI and Google Gemini.

---

## 🚀 Features

- 🤖 Multi-Agent AI system (CrewAI)
- 🎨 Game Designer Agent (creates game logic)
- 👨‍💻 Python Game Developer Agent (writes full Pygame code)
- 🧠 Gemini 2.5 Flash LLM integration
- 🔍 Optional web search tool (Serper API)
- 🎮 Automatic game generation pipeline

---

## 🧠 What This Project Does

This AI system can:

- Take a simple game idea (e.g., "spaceship shooter")
- Convert it into a structured game design
- Generate complete working Python Pygame code
- Output a playable game script

---

## 🏗️ Tech Stack

- Python
- CrewAI (Multi-Agent Framework)
- Google Gemini API
- LangChain
- Pygame
- Serper API (Search Tool)

---

## 📂 Project Structure


app.py → Main multi-agent system
agents.py → Agent definitions (optional split)
outputs/ → Generated game files
requirements.txt → Dependencies
.env.example → API keys template


---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/ai-game-development-crew.git
cd ai-game-development-crew
2. Install dependencies
pip install -r requirements.txt
3. Add API keys

Create .env file:

GEMINI_API_KEY=your_key
SERPER_API_KEY=your_key
4. Run project
python app.py
💡 How It Works
User provides a game idea
Game Designer Agent creates game blueprint
Game Developer Agent converts it into Pygame code
Final game code is generated automatically
📌 Example

Input:

Create a spaceship shooting game

Output:

Game design (rules, mechanics)
Full Python Pygame code
Ready-to-run game file