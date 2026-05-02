from src.loader import load_documents
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vector_db import create_db, load_db
from src.retriever import get_retriever
from src.rag_pipeline import build_rag
import os

DATA_PATH = "data"

def setup():
    print("Setting up chatbot...\n")

    embeddings = get_embeddings()

    
    if not os.path.exists("vectorstore"):
        print("Loading documents...")
        docs = load_documents(DATA_PATH)

        if not docs:
            print(" No documents found in 'data/' folder!")
            return None

        print("Splitting documents...")
        chunks = split_documents(docs)

        print("Creating vector database...")
        db = create_db(chunks, embeddings)
    else:
        print("Loading existing vector database...")
        db = load_db(embeddings)

    print("Preparing retriever...")
    retriever = get_retriever(db)

    print("Loading LLM (this may take a few seconds)...")
    qa = build_rag(retriever)

    print("\nChatbot ready!\n")
    return qa


def chat():
    print("Starting application...\n")

    qa = setup()

    if qa is None:
        print("Setup failed. Please add documents and try again.")
        return

    print("You can now ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Ask: ").strip()

        if query.lower() == "exit":
            print("\nExiting chatbot. Goodbye!")
            break

        if not query:
            print("Please enter a valid question.\n")
            continue

        print("\nGenerating answer...\n")

        try:
            result = qa(query)

            print("Answer:")
            print(result["result"])

            print("\nSources:")
            for doc in result["source_documents"]:
                print("-", doc.metadata.get("source"))

        except Exception as e:
            print("Error:", str(e))

        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    chat()