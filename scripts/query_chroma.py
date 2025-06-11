# Usage: python3 query_chroma.py "your query text"

import sys
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os

query = sys.argv[1] if len(sys.argv) > 1 else ""
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-api-key")

# Load Chroma DB
db = Chroma(persist_directory="chroma_db", embedding_function=OpenAIEmbeddings())

# Perform semantic search
results = db.similarity_search_with_score(query, k=3)

# Format results
context = "\n\n".join([doc.page_content for doc, _ in results])
scores = [float(score) for _, score in results]

print({"context": context, "scores": scores, "query": query})