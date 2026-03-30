import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from transformers import pipeline

# Step 1: Load embeddings (must match ingest.py)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Step 2: Load FAISS vector DB
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


# Step 3: Create retriever (fetch top-k similar documents)
retriever = db.as_retriever(search_kwargs={"k": 2})

# Step 4: Load local LLM (FLAN-T5)
pipe = pipeline(
    task="text2text-generation",   
    model="google/flan-t5-base"
)

# Wrap HuggingFace pipeline for LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Step 5: Better Prompt (VERY IMPORTANT)
prompt_template = """
Answer the question using the most relevant sentence from the context.

Context:
{context}

Question: {question}

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Step 6: Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

# Step 7: Chat loop
print("🤖 RAG Chatbot Ready! Type 'exit' to quit.\n")

while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    # 🔍 DEBUG: Check retrieved context
    docs = retriever.get_relevant_documents(query)

    print("\n--- Retrieved Context ---")
    for doc in docs:
        print(doc.page_content)
    print("-------------------------\n")

    # 🤖 RAG answer from pipeline
    result = qa.invoke({"query": f"Answer this question: {query}"})

    answer = result["result"].strip()
    print("\nAnswer:", answer, "\n")