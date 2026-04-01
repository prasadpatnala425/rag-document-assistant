from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

# Initialize FastAPI
app = FastAPI()

# Request schema
class QueryRequest(BaseModel):
    question: str

# Load embeddings (same as ingest.py)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load FAISS DB
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# Retriever
retriever = db.as_retriever(search_kwargs={"k": 1})

# Load model
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256,
)

llm = HuggingFacePipeline(pipeline=pipe)

# Prompt
prompt_template = """
Use the context below to answer the question.

Context:
{context}

Question: {question}

Answer in one short sentence.
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}

# Query endpoint
@app.post("/ask")
def ask_question(request: QueryRequest):
    query = request.question

    # Retrieve docs (debug)
    docs = retriever.invoke(query)
    context = [doc.page_content for doc in docs]

    # Get answer
    answer = qa.run(query)

    return {
        "question": query,
        "answer": answer,
        "context": context
    }