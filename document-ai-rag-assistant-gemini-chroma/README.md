# PDF RAG Chatbot (Gemini + Chroma + LangChain)

An AI-powered **Retrieval-Augmented Generation (RAG)** system that allows users to upload a PDF and ask questions about its content.

---

## 🚀 Features

- 📄 PDF document loading
- ✂️ Text chunking using RecursiveCharacterTextSplitter
- 🧠 Embeddings using HuggingFace Sentence Transformers
- 🗄️ Vector storage using ChromaDB
- 🔍 Semantic search over document content
- 🤖 Gemini 2.5 Flash for answering questions
- 💬 CLI-based chatbot interface

---

## 🧠 What This Project Does

This system allows you to:

- Load a PDF document
- Convert it into searchable chunks
- Store embeddings in a vector database
- Retrieve relevant context for a question
- Generate accurate answers using LLM

Example:
> Q: What is attention mechanism?  
> A: Answer generated using PDF context

---

## 🏗️ Tech Stack

- Python
- LangChain
- Google Gemini API
- ChromaDB
- HuggingFace Embeddings
- PyPDF

---

## 📂 Project Structure


app.py → Main RAG pipeline
data/ → PDF documents
chroma_db/ → Vector database storage
requirements.txt → Dependencies
.env.example → API key template


---

## ⚙️ Setup Instructions

### 1. Clone repo

git clone https://github.com/your-username/pdf-rag-chatbot-chroma-gemini.git
cd pdf-rag-chatbot-chroma-gemini


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add API Key
Create `.env` file:

GOOGLE_API_KEY=your_api_key_here


### 4. Add PDF
Place your PDF inside:

data/


### 5. Run project

python app.py


---

## 💡 How It Works

1. PDF is loaded and split into chunks
2. Each chunk is converted into embeddings
3. Stored in Chroma vector DB
4. User asks a question
5. Most relevant chunks are retrieved
6. Gemini generates final answer using context

---

## 📌 Use Cases

- Study notes assistant
- Research paper Q&A
- Document understanding system
- AI knowledge base chatbot

---

## 🚀 Future Improvements

- Web UI using Streamlit / Gradio
- Multi-PDF upload support
- Chat memory
- Source highlighting UI
- Deployment on cloud

---

## 👨‍💻 Author

AI/ML + LLM RAG system project for portfolio showcasing real-world document intelligence.