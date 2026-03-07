# 🤖 AI Agent with Long-Term Memory

A conversational AI assistant that remembers previous interactions using vector memory.
This project demonstrates how to build an AI agent with persistent memory using modern LLM tools.

The assistant can recall past conversations and use them to generate better responses.

---

# 🚀 Features

* 🧠 Long-term memory using vector database
* 💬 Interactive chat interface
* ⚡ Fast LLM responses
* 🔍 Semantic memory retrieval
* 🖥 Simple web UI

The system retrieves relevant past conversations and provides them as context to the AI model before generating a response.

---

# 🧰 Tech Stack

Backend

* Python
* LangChain

AI Model

* Groq API
* Model: Llama 3

Memory System

* ChromaDB

Frontend

* Streamlit

Embeddings

* HuggingFace sentence-transformers

---

# 📁 Project Structure

```
ai-agent-memory
│
├── app.py          # Streamlit user interface
├── agent.py        # AI logic and LLM interaction
├── memory.py       # Vector memory system
├── .env            # API key storage
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```
git clone https://github.com/Chintan1545/ai-agent-memory.git
cd ai-agent-memory
```

---

## 2️⃣ Create Conda Environment

```
conda create -n ai_agent python=3.10
conda activate ai_agent
```

---

## 3️⃣ Install Dependencies

```
pip install langchain
pip install langchain-community
pip install langchain-groq
pip install chromadb
pip install streamlit
pip install python-dotenv
pip install sentence-transformers
```

---

# 🔑 Setup API Key

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the Groq developer console.

---

# ▶️ Run the Application

```
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

# 💬 Example Interaction

User:

```
My name is Chintan
```

AI:

```
Nice to meet you Chintan!
```

Later:

User:

```
What is my name?
```

AI:

```
Your name is Chintan.
```

The AI retrieves previous information from the vector database.

---

# 🧠 How Memory Works

1. User message is converted into embeddings.
2. Embeddings are stored in the vector database.
3. When a new query is asked, the system retrieves similar past conversations.
4. The retrieved memory is added to the prompt for the AI model.

This allows the AI to recall past interactions.

---

# 🏗 Architecture

```
User
 ↓
Streamlit UI
 ↓
LangChain Agent
 ↓
Groq LLM
 ↓
ChromaDB Memory
```

---

# 📌 Future Improvements

* Voice interaction
* Document-based RAG
* Tool-enabled agents (search, calculator, APIs)
* Chat history viewer
* Deployment on cloud

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Chintan Dabhi
AI / ML Developer
