# 🧠 LLM Fine-Tuning with Unsloth (Gemma + QLoRA)

This project demonstrates **fine-tuning a large language model (LLM)** using **Unsloth + QLoRA** on a conversational dataset for game NPC dialogue.

---

## 🚀 Features

- 🤖 Fine-tunes Gemma 3 (270M Instruct Model)
- ⚡ Uses Unsloth for fast training
- 🧠 QLoRA (memory efficient fine-tuning)
- 🎮 Dataset: Mobile Game NPC Conversations
- 💬 Creates AI-powered game NPC chatbot
- 🔥 Optimized for low GPU usage

---

## 🧠 What This Project Does

This project:

1. Loads a pre-trained LLM (Gemma)
2. Applies LoRA adapters (QLoRA)
3. Loads NPC dialogue dataset
4. Converts conversations into chat format
5. Fine-tunes model on game character behavior
6. Produces a custom NPC chatbot model

---

## 🏗️ Tech Stack

- Python
- Unsloth AI
- HuggingFace Transformers
- PEFT (LoRA / QLoRA)
- Datasets library
- PyTorch

---

## 📂 Project Structure


train.py → Fine-tuning pipeline
inference.py → Model testing
dataset/ → Training dataset
model_output/ → Saved fine-tuned model
requirements.txt → Dependencies


---

## ⚙️ Setup Instructions

### 1. Install dependencies

pip install -r requirements.txt


---

### 2. Run training

python train.py


---

### 3. Run inference

python inference.py


---

## 💡 How It Works

- Base model (Gemma) is loaded
- LoRA adapters are added
- Dataset is formatted into chat format
- Model learns NPC-style responses
- Fine-tuned model can respond like a game character

---

## 📌 Use Cases

- Game NPC chatbot creation
- Custom assistant training
- Domain-specific LLMs
- Research in fine-tuning LLMs
- Lightweight model adaptation

