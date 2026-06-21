import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chat_models import init_chat_model


PDF_PATH = "attention_is_all_you_need.pdf"  # local file OR replace with URL
PERSIST_DIR = "./chroma_langchain_db"
COLLECTION_NAME = "research_collection"

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")



def load_documents(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    splits = text_splitter.split_documents(docs)
    return splits




embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)



def build_vector_store(docs):
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=PERSIST_DIR
    )

    vector_store.add_documents(documents=docs)
    return vector_store




def retrieve_context(query: str, vector_store, k: int = 2):
    retrieved_docs = vector_store.similarity_search(query, k=k)

    context = ""
    for doc in retrieved_docs:
        context += f"Source: {doc.metadata}\n"
        context += f"Content: {doc.page_content}\n\n"

    return context, retrieved_docs



model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=api_key
)



def docu_chat(user_query, vector_store):
    context, source_docs = retrieve_context(user_query, vector_store, k=2)

    system_message = f"""
You are a helpful chatbot.
Use ONLY the following context to answer.
Do NOT hallucinate or add external information.

Context:
{context}
"""

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_query}
    ]

    response = model.invoke(messages)

    return {
        "answer": response.content,
        "source_documents": source_docs,
        "context_used": context
    }



def main():
    print("\nLoading and processing PDF...\n")

    docs = load_documents(PDF_PATH)
    vector_store = build_vector_store(docs)

    print("RAG system ready!\n")

    while True:
        query = input("Ask a question (type 'exit'): ")

        if query.lower() == "exit":
            break

        result = docu_chat(query, vector_store)

        print("\n--- ANSWER ---")
        print(result["answer"])
        print("\n----------------\n")


if __name__ == "__main__":
    main()