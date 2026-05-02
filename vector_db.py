from langchain_community.vectorstores import FAISS

def create_db(chunks, embeddings):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vectorstore")
    return db

def load_db(embeddings):
    return FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)