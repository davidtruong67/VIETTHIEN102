from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

embedding = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding)

def add_to_memory(content: str):
    doc = Document(page_content=content)
    vectorstore.add_documents([doc])
    vectorstore.persist()

def recall_from_memory(query: str):
    return vectorstore.similarity_search(query, k=2)