# 🧠 LLM Evaluation Framework (Gemini + BLEU + BERTScore)

An AI system that not only generates responses using an LLM but also **evaluates the quality of those responses using NLP metrics like BLEU and BERTScore**.

---

## 🚀 Features

- 🤖 Gemini 2.5 Flash Study Assistant
- 🎭 Multiple Personas (Friendly / Academic)
- 📊 LLM Evaluation Pipeline
- 📏 BLEU Score for text similarity
- 🧠 BERTScore for semantic similarity
- 🧪 Automated testing of AI responses

---

## 🧠 What This Project Does

This system:

1. Takes a question
2. Generates AI response using Gemini
3. Compares response with reference answer
4. Calculates:
   - BLEU Score
   - BERTScore
5. Evaluates how good the LLM is

---

## 🏗️ Tech Stack

- Python
- Google Gemini API
- Evaluate library (HuggingFace)
- BERTScore
- BLEU metric
- NLP evaluation tools

---

## 📂 Project Structure


app.py → LLM Study Assistant
evaluator.py → Evaluation pipeline
test_data.json → Test dataset
requirements.txt → Dependencies


---

## ⚙️ Setup Instructions

### 1. Install dependencies

pip install -r requirements.txt


---

### 2. Add API key

export GEMINI_API_KEY=your_key


---

### 3. Run evaluation

python evaluator.py


---

## 💡 How It Works

- LLM generates answers
- Reference answers are provided
- Metrics compare similarity
- Final score shows model performance

---

## 📌 Use Cases

- LLM benchmarking
- AI assistant quality testing
- Prompt engineering evaluation
- Model comparison experiments

---

## 👨‍💻 Author

AI/ML + LLM Evaluation System project for analyzing and benchmarking AI model performance.