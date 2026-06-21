# AI Study Assistant (Gemini + Gradio)

An interactive AI-powered study assistant built using **Google Gemini API** and **Gradio UI**.  
It supports multiple teaching personalities to help users understand concepts in different styles.

---

## 🚀 Features

- 🧠 Powered by Google Gemini (2.5 Flash)
- 🎭 Two AI personalities:
  - Friendly (simple, beginner-friendly explanations)
  - Academic (formal, structured university-level explanations)
- 💬 Interactive Gradio web interface
- ⚡ Fast responses with configurable temperature
- 📚 Educational focus with follow-up questions

---

## 🏗️ Tech Stack

- Python
- Google Gemini API
- Gradio
- Environment Variables (.env)

---

## 📂 Project Structure


app.py → Main application
requirements.txt → Dependencies
.env.example → API key template
assets/ → Optional screenshots


---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/llm-study-assistant-gradio-gemini.git
cd llm-study-assistant-gradio-gemini


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add API Key
Create a `.env` file:


GEMINI_API_KEY=your_api_key_here


### 4. Run the app

python app.py


---

## 🧪 How it works

1. User enters a question
2. Selects a personality (Friendly / Academic)
3. Prompt is modified using system instruction
4. Gemini generates contextual response
5. Output is displayed in Gradio UI

---

## 📌 Example Use Cases

- Learning DSA concepts
- Understanding Machine Learning topics
- Quick revision before exams
- Concept explanation in simple terms

---

## 📈 Future Improvements

- Add more personas (Coder, Mentor, Interviewer)
- Add chat history memory
- Add streaming responses
- Deploy on HuggingFace Spaces / Render

---

## 👨‍💻 Author

Built as part of an AI/LLM project portfolio.