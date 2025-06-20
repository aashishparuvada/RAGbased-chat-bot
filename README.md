# RAG Chatbot Project

This project implements a Retrieval-Augmented Generation (RAG) chatbot using:
- **Chroma** for vector storage
- **OpenAI** for LLM responses
- **n8n** as the orchestration layer
- **Streamlit** for a user-friendly chat UI

## 🏗️ How It Works

1. **Document Ingestion & Embedding**: PDF documents are loaded, chunked, and embedded using OpenAI embeddings, then stored in ChromaDB.
2. **Query Workflow (n8n)**: When a user asks a question, the workflow:
   - Retrieves relevant context from ChromaDB (via a Python script)
   - Calls OpenAI's API to generate an answer using the retrieved context
   - Returns the answer via an HTTP webhook
3. **Streamlit UI**: Provides a chat interface that sends user queries to the n8n webhook and displays the bot's answers.

---

## 📦 Prerequisites
- Python 3.10+
- Node.js + n8n
- OpenAI API Key
- `pip install langchain openai chromadb pymupdf streamlit requests`

---

## 📁 Project Structure
```
ragbasedchatbot/
├── workflows/                  # n8n workflow export
│   └── rag-chatbot-workflow.json
├── scripts/                    # Setup and query code
│   ├── setup.py                # Document loader + vector indexer
│   └── query_chroma.py         # Used in n8n to perform query
├── data/
│   └── sample-documents/       # FAQ PDFs
├── docs/                       # Documentation
│   ├── README.md
│   └── technical-approach.md
├── tests/
│   └── sample-queries.json     # For testing chatbot
├── streamlit_app.py            # Streamlit chat UI
```

---

## ⚙️ Setup & Run

### 1. **Setup Embeddings**
```bash
python3 scripts/setup.py
```

### 2. **Start n8n**
```bash
n8n start
```

### 3. **Import Workflow**
- Go to n8n UI → Import `workflows/rag-chatbot-workflow.json`
- Activate the workflow (ensure the webhook is listening at `http://localhost:5678/webhook/faq-query`)

### 4. **Test via HTTP Webhook (Optional)**
```bash
curl -X POST http://localhost:5678/webhook/faq-query \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the values of Altibbe?"}'
```

### 5. **Run the Streamlit Chat UI**
```bash
streamlit run streamlit_app.py
```
- Open the provided local URL (usually `http://localhost:8501`) in your browser.
- Type your question and chat with the bot!

---

## 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI key (required for both embedding and LLM generation)
- `CHROMA_DB_PATH`: Local path to Chroma persistence (default: `chroma_db`)

---

## 🧪 Testing
- Run all sample queries in `tests/sample-queries.json` and verify expected keywords are returned.
- Add your own PDFs to `data/sample-documents/` and re-run the embedding setup as needed.

---

## 📝 Project Workflow Summary

1. **Ingest & Embed**: Load and embed documents with `setup.py`.
2. **n8n Orchestration**: Handles query routing, retrieval, and LLM response.
3. **Streamlit UI**: User-friendly chat interface, interacts with n8n via HTTP.

---

## 🙌 Credits & Further Improvements
- Built with [LangChain](https://github.com/langchain-ai/langchain), [Chroma](https://www.trychroma.com/), [OpenAI](https://platform.openai.com/), [n8n](https://n8n.io/), and [Streamlit](https://streamlit.io/).
- See `docs/technical-approach.md` for more details and future improvement ideas.
