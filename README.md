# RAG Chatbot Project

This project implements a Retrieval-Augmented Generation (RAG) chatbot using `n8n` as the orchestration layer, OpenAI for LLM responses, and Chroma for vector storage.

## 🔧 Setup Instructions

### 📦 Prerequisites
- Python 3.10+
- Node.js + n8n
- OpenAI API Key
- `pip install langchain openai chromadb pymupdf`

### 📁 Project Structure
```
rag-chatbot-project/
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
```

### ⚙️ Steps to Run

1. **Setup Embeddings**
```bash
python3 scripts/setup.py
```

2. **Start n8n**
```bash
n8n start
```

3. **Import Workflow**
- Go to n8n UI → Import `rag-chatbot-workflow.json`

4. **Test via HTTP Webhook**
```bash
curl -X POST http://localhost:5678/webhook/faq-query \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the values of Altibbe?"}'
```

## 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI key
- `CHROMA_DB_PATH`: Local path to Chroma persistence

## 🧪 Testing
Run all sample queries in `tests/sample-queries.json` and verify expected keywords are returned.

## 📬 Support
Contact: people@altibbe.com
