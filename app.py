import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline

from langchain.chains import RetrievalQA
from transformers import pipeline

# Step 1: Load embeddings (same as ingest.py)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Step 2: Load vector DB
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

# Step 3: Create retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# Step 4: Load local LLM (FREE)
pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=256,
)

llm = HuggingFacePipeline(pipeline=pipe)

# Step 5: Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
)

# Step 6: Ask questions loop
print("🤖 RAG Chatbot Ready! Type 'exit' to quit.\n")

while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    result = qa.run(query)
    print("\nAnswer:", result, "\n")