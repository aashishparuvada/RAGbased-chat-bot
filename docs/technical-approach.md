# Technical Approach

## 🔍 Retrieval-Augmented Generation (RAG) Overview

We use a classic RAG pipeline consisting of:
1. **Document Ingestion + Chunking** using `PyMuPDF` and `langchain.text_splitter`
2. **Embedding Generation** with OpenAI Embeddings (`text-embedding-ada-002`)
3. **Vector Storage** in `ChromaDB` for fast semantic search
4. **n8n Workflow** to integrate query input, vector search, and LLM generation

## ⚙️ Design Decisions

### Embedding & Storage
- Chose **Chroma** for ease of local use and quick setup
- Used `RecursiveCharacterTextSplitter` for token-optimised chunking
- `OpenAIEmbeddings` ensure strong vector quality and fast search

### Workflow (n8n)
- HTTP Webhook used to trigger queries
- Custom function nodes handle:
  - Preprocessing
  - Python vector search (via CLI call)
  - Prompt formatting
  - Calling OpenAI API
- Final node returns formatted and attributed response

## 🧱 Challenges & Solutions
| Challenge                             | Solution                                        |
|--------------------------------------|-------------------------------------------------|
| n8n JS integration with Python DB    | Used `spawnSync` in JS to call Python script    |
| Embedding performance                | Batched chunking and caching with Chroma        |
| Ethical output generation            | Prompt design includes a responsible system role|
| API latency                          | Result caching planned as a future feature      |

## 🚀 Performance Considerations
- All search queries are limited to top 3 with similarity scores
- Context chunks are trimmed to avoid LLM token overflow
- Modular script enables switching vector DBs or LLMs easily

## 📈 Future Improvements
- Conversation memory across multiple queries
- Response caching using Redis/SQLite
- Support for multiple LLMs
- UI layer for input + response display
- Realtime document ingestion with auto-reindexing
