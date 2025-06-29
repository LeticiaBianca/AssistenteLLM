import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

import os

st.title("Assistente Conversacional Baseado em LLM")

st.markdown("""
Passos:
1. Carregar um PDF;
2. Esperar o assistente indexar localmente com embeddings BERT;
3. Digitar sua pergunta;
4. O assistente busca os trechos mais parecidos com sua pergunta;
""")

uploaded_file = st.file_uploader("Faca Upload do seu PDF: ", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF carregado com sucesso!")

    with st.spinner("Lendo PDF..."):
        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)

    with st.spinner("Processando PDF..."):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.from_documents(chunks, embeddings)

    st.success("PDF processado!")

    question = st.text_input("Faca sua pergunta:")

    if question:
        with st.spinner("Pensando..."):
            docs = db.similarity_search(question, k=3)
            st.subheader("Respostas encontradas:")
            for i, d in enumerate(docs, 1):
                st.markdown(f"**Resposta {i}:** {d.page_content}")
