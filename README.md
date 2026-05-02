# RAG Chatbot (HR Policy Assistant)

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user queries based on company HR policy documents.

The system retrieves relevant context from documents using vector search and generates answers using a local LLM via Ollama.

---

## Objective
To build a reliable question-answering system that:
- Uses document-based retrieval
- Minimizes hallucination
- Works efficiently on local hardware

---

## Tech Stack
- Python
- LangChain
- FAISS (Vector Store)
- Ollama (Local LLM)
- Sentence Transformers

---

## Setup Instructions

### 1. Clone the repository

git clone <repo-link>
cd rag-chatbot


### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Install Ollama
Download from: https://ollama.com

Pull lightweight model:

ollama pull llama3.2:1b


---

## Run the Application

python app.py


---

## Project Structure

rag-chatbot/
│── app.py
│── data/
│ └── company_hr_policy.txt
│── src/
│ ├── loader.py
│ ├── splitter.py
│ ├── embeddings.py
│ ├── vector_db.py
│ ├── retriever.py
│ └── rag_pipeline.py
│── vectorstore/
│── README.md


---

## Sample Queries
- What is the leave policy?
- What are the working hours?
- What benefits do employees receive?
- Summarize the HR policies

---

## System Workflow
1. Load documents from `data/`
2. Split text into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant chunks
6. Generate answer using LLM

---

## Notes
- Uses a lightweight model (`llama3.2:1b`) to support low-memory systems
- Answers are strictly based on provided documents
- Vector database must be rebuilt if data changes

---

## Improvements (Future Work)
- Web UI using Streamlit
- Conversation memory
- Improved ranking and retrieval

---

## Author
Mohammed Safwan