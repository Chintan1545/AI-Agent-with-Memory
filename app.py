import streamlit as st
from agent import chat_with_memory
import time

# Page configuration
st.set_page_config(
    page_title="AI Agent with Memory",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Agent with Long-Term Memory")

st.markdown(
"""
This AI assistant remembers previous conversations using:
- LangChain
- Groq LLM
- ChromaDB memory
"""
)

# Sidebar
with st.sidebar:
    st.header("⚙ Settings")

    if st.button("🧹 Clear Chat History"):
        st.session_state.messages = []
        st.success("Chat cleared!")

    st.markdown("---")
    st.markdown("### Memory Info")
    st.write("This agent stores conversation embeddings for long-term recall.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

# User input
prompt = st.chat_input("Ask something...")

if prompt:

    # Show user message
    st.session_state.messages.append(("user", prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = chat_with_memory(prompt)

        message_placeholder = st.empty()
        full_response = ""

        # Simulated streaming
        for word in response.split():
            full_response += word + " "
            message_placeholder.markdown(full_response)
            time.sleep(0.03)

        st.session_state.messages.append(("assistant", full_response))