import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("🤖 RAG Document Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Call API
    response = requests.post(API_URL, json={"question": user_input})

    if response.status_code == 200:
        data = response.json()
        answer = data["answer"]

        # Show bot response
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)

        # Optional: show context (debug)
        with st.expander("🔍 Retrieved Context"):
            for ctx in data["context"]:
                st.write(ctx)
    else:
        st.error("Error connecting to API")