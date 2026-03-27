# RAG Document Assistant

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system using LLMs.

## Features
- Document ingestion and chunking
- Embedding generation
- Vector similarity search (FAISS)
- Context-aware question answering

## Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Transformers (GPT-2)

## Architecture
User Query → Embedding → Vector Search → Context → LLM → Answer

## Future Enhancements
- Switch to FLAN-T5
- FastAPI integration
- PDF support
- Frontend UI

## Sample Output
Q: How to change password?  
A: Employees can reset their password using the internal security portal.

## ▶️ How to Run

### 1. Create virtual environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# run ingestion
python ingest.py

#run app
python ingest.py



