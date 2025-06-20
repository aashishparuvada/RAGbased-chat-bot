import streamlit as st
import requests

# n8n webhook endpoint
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/faq-query"

st.title("RAG Chatbot UI")
st.write("Ask a question about your documents:")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Your question", key="input")

if st.button("Send") and user_input:
    # Display user message
    st.session_state["chat_history"].append(("user", user_input))
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json={"query": user_input},
            timeout=30
        )
        if response.status_code == 200:
            answer = response.text.strip()
        else:
            answer = f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        answer = f"Request failed: {e}"
    st.session_state["chat_history"].append(("bot", answer))
    st.experimental_rerun()

# Display chat history
for role, msg in st.session_state["chat_history"]:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}") 