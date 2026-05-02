from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

def build_rag(retriever):
    llm = Ollama(
        model="llama3.2:1b",
        temperature=0
    )

    prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant.

Answer the question ONLY using the provided context.

Rules:
- If the answer is clearly found in the context → give the answer only.
- If the answer is NOT found → reply ONLY with:
  Not available in the knowledge base.

- Do NOT give both answer and fallback.
- Do NOT add extra explanation.

Context:
{context}

Question:
{question}
"""
)
    

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa