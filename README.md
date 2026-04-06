# 🤖 RAG Document Assistant

A full-stack Retrieval-Augmented Generation (RAG) chatbot that answers questions based on custom documents using FAISS vector search, FastAPI backend, and Streamlit frontend.

---

## 🚀 Features

- 📄 Document ingestion and chunking
- 🔍 Semantic search using FAISS
- 🤖 Context-aware answer generation (HuggingFace FLAN-T5)
- ⚡ FastAPI backend for API access
- 💬 Streamlit chatbot UI
- 🧠 Context debugging support

---

## 🏗️ Project Structure

```
rag-document-assistant/
│
├── data/                # Source documents
├── vectorstore/         # FAISS index
├── ingest.py            # Document processing & indexing
├── app.py               # CLI-based chatbot (initial version)
├── main.py              # FastAPI backend
├── ui.py                # Streamlit frontend
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd rag-document-assistant
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📥 Step 1: Ingest Documents

Place your documents inside the `data/` folder.

Run:
```bash
python ingest.py
```

This will:
- Split documents into chunks
- Create embeddings
- Store them in FAISS (`vectorstore/`)

---

## 💻 Step 2: Run CLI Chatbot (Optional)

```bash
python app.py
```

---

## ⚡ Step 3: Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Open Swagger UI:
👉 http://127.0.0.1:8000/docs

Example request:
```json
{
  "question": "reset password"
}
```

---

## 💬 Step 4: Run Streamlit UI

```bash
streamlit run ui.py
```

Open:
👉 http://localhost:8501

---

## 🧠 How It Works

1. Documents are split into chunks
2. Embeddings are generated using HuggingFace
3. FAISS stores vectors for similarity search
4. User query → converted to embedding
5. Relevant chunks are retrieved
6. LLM generates answer using context

---

## 🔧 Tech Stack

- **LangChain**
- **FAISS**
- **HuggingFace Transformers**
- **FastAPI**
- **Streamlit**
- **Python**

---

## ⚠️ Known Issues & Fixes

- Deprecated method:
  - `get_relevant_documents()` → replaced with `invoke()`
- Model mismatch:
  - Use `text2text-generation` for FLAN-T5
- Prompt issues:
  - Fixed by explicitly passing `{context}` and `{question}`

---

## 📈 Future Improvements

- Add chat memory
- Support PDF upload via UI
- Use OpenAI / Mistral for better responses
- Deploy on cloud (AWS / Render / Docker)

---

## 💡 Resume Highlight

> Built a full-stack RAG chatbot using FastAPI and Streamlit with FAISS-based semantic search and HuggingFace LLMs for context-aware question answering.

---