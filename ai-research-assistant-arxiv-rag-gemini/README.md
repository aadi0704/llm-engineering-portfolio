# AI Research Paper Chatbot (RAG + Gemini + LangChain)

An AI-powered **research assistant chatbot** that reads academic papers and answers questions using Retrieval-Augmented Generation (RAG).

This project is built using the famous paper:
👉 "Attention Is All You Need" (Transformer Architecture)

---

## 🚀 Features

- 📄 Loads research papers from ArXiv
- ✂️ Splits documents into meaningful chunks
- 🧠 Embeddings using HuggingFace Transformers
- 🗄️ Vector database using ChromaDB
- 🔍 Semantic search over research paper
- 🤖 Gemini 2.5 Flash for reasoning answers
- 💬 CLI-based interactive chatbot

---

## 🧠 What This Project Does

This AI assistant:

- Reads a full research paper
- Understands semantic meaning of text
- Retrieves relevant sections based on question
- Generates accurate answers using LLM

Example:

Q: What is the role of attention in transformers?  
A: Answer generated using actual paper context

---

## 🏗️ Tech Stack

- Python
- LangChain
- Google Gemini API
- ChromaDB
- HuggingFace Embeddings
- PyPDF / ArXiv loader

---

## 📂 Project Structure


app.py → Main RAG pipeline
data/ → Research paper PDF
chroma_db/ → Vector database
requirements.txt → Dependencies
.env.example → API key template


---

## ⚙️ Setup Instructions

### 1. Clone repository

git clone https://github.com/your-username/ai-research-assistant-arxiv-rag-gemini.git
cd ai-research-assistant-arxiv-rag-gemini


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add API key
Create `.env` file:

GOOGLE_API_KEY=your_api_key_here


### 4. Run project

python app.py


---

## 💡 How It Works

1. Research paper is loaded
2. Text is split into chunks
3. Each chunk is embedded
4. Stored in Chroma vector DB
5. User asks question
6. Relevant chunks retrieved
7. Gemini generates final answer

---

## 📌 Use Cases

- Research paper understanding
- Student study assistant
- AI paper summarizer
- Transformer architecture learning tool

---

## 🚀 Future Improvements

- Multi-paper RAG system
- Streamlit web UI
- Citation highlighting
- PDF upload interface
- Chat memory support

---

## 👨‍💻 Author

AI/ML + LLM RAG Research Assistant project for portfolio showcasing deep document understanding systems.