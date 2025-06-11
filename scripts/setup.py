# Loads PDF, chunks it, embeds using OpenAI, and stores in Chroma

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load documents
doc_loader = PyMuPDFLoader("data/sample-documents/faq.pdf")
documents = doc_loader.load()

# Chunk documents
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# Embed and persist to Chroma
db = Chroma.from_documents(documents=chunks, embedding=OpenAIEmbeddings(), persist_directory="chroma_db")
db.persist()

print("Document embeddings stored successfully.")
