1. IMPORTS


import os
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
2. EMBEDDINGS


embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)
3. FAISS VECTOR DB


vector_store = FAISS.from_texts(
    chunks,
    embedding=embeddings
)
4. retrieve_context()


def retrieve_context(query, top_k=3):


5. ask_chatbot()


def ask_chatbot(query):
