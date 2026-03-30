# RAG Document Assistant

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user queries based on custom documents.

It uses embeddings + vector search to retrieve relevant context and a language model to generate answers.

---

## 🚀 Features

* Document ingestion and chunking
* Embedding generation using HuggingFace
* Vector similarity search using FAISS
* Context-aware question answering
* Debug view to inspect retrieved context

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* HuggingFace Transformers
* Sentence Transformers

---

## 🧠 Architecture

User Query
→ Convert to Embedding
→ Retrieve Relevant Documents (FAISS)
→ Inject Context into Prompt
→ LLM Generates Answer

---

## 📂 Project Structure

```
rag-document-assistant/
│── data/                # Source documents
│── vectorstore/         # FAISS index (generated)
│── app.py               # Main chatbot application
│── ingest.py            # Document ingestion & embedding
│── requirements.txt     # Dependencies
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 📥 Step 1: Ingest Documents

Place your documents inside the `data/` folder, then run:

```
python ingest.py
```

This will:

* Split documents into chunks
* Generate embeddings
* Store them in FAISS vector database

---

## 🤖 Step 2: Run Chatbot

```
python app.py
```

Example:

```
Ask a question: reset password
```

---

## 🔍 Debug Mode

The app prints retrieved context:

```
--- Retrieved Context ---
<relevant document chunks>
-------------------------
```

This helps verify:

* Retrieval quality
* Data correctness

---

## ⚠️ Known Issues / Learnings

* LangChain APIs are evolving (deprecations like `.run()` → `.invoke()`)
* FLAN-T5 model has limited reasoning capability
* Prompt design significantly affects output quality
* Retrieval works better when `k` is tuned (e.g., k=1 or 2)

---

## 🚧 Future Enhancements

* Replace FLAN-T5 with stronger model (Mistral / GPT)
* Add FastAPI backend
* Build frontend UI (Streamlit / React)
* Support PDFs and multiple document formats
* Add conversation memory

---

## ✅ Status

✔ Fully working RAG pipeline
✔ Retrieval + generation integrated
✔ Ready for backend/API integration

---

## 🙌 Author Notes

This project was built step-by-step to understand:

* RAG architecture
* Vector databases
* Prompt engineering
* LLM limitations

---

## 💡 Example Use Cases

* Internal knowledge assistant
* FAQ chatbot
* Document search system
* Customer support automation

---