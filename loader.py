from langchain_community.document_loaders import PyPDFLoader, TextLoader, BSHTMLLoader
import os

def load_documents(folder):
    docs = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        elif file.endswith(".html"):
            loader = BSHTMLLoader(path)
        else:
            continue

        docs.extend(loader.load())

    return docs