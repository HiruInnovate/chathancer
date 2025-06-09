import os

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader

from backend.ingestion import ingest_docs

st.title("📁 PDF Embedder")

with st.sidebar:
    st.header("Configuration")
    chunk_size = st.slider("Chunk Size", min_value=100, max_value=2000, value=500)
    chunk_overlap = st.slider("Chunk Overlap", min_value=0, max_value=500, value=50)

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Save the uploaded file to a specific directory
    save_dir = "uploads"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Embedding PDF..."):
        output = ingest_docs(file_path, chunk_size, chunk_overlap)
        if output == "Success":
            st.success("PDF has been embedded and uploaded to Pinecone!")
        else:
            st.error("Error occurred while ingesting the document!! ")