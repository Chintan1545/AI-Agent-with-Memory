import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from memory import load_memory

load_dotenv()

vectordb = load_memory()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_with_memory(user_input):

    docs = vectordb.similarity_search(user_input, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful AI assistant.

Previous memory:
{context}

User: {user_input}
AI:
"""

    response = llm.invoke(prompt)

    vectordb.add_texts([user_input])
    vectordb.persist()

    return response.content