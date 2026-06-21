from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
import os

file_path = "attention_is_all_you_need.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db"
)

vector_store.add_documents(documents=all_splits)

api_key = os.getenv("GEMINI_API_KEY")

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=api_key
)

@tool
def retrieve_from_pdf(query: str) -> str:
    retrieved_docs = vector_store.similarity_search(query, k=2)
    docs_content = ""
    for doc in retrieved_docs:
        docs_content += f"Source: {doc.metadata}\n"
        docs_content += f"Content: {doc.page_content}\n\n"
    return docs_content

tavily_api_key = os.getenv("TAVILY_API_KEY")

web_search_tool = TavilySearch(
    max_results=3,
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)

system_prompt = """You are a helpful research assistant with access to two tools:

1. retrieve_from_pdf: Use this to find information from the Attention Is All You Need paper
2. TavilySearch: Use this for external or recent information

Use retrieve_from_pdf for paper-related questions.
Use TavilySearch for anything outside the paper.
"""

agent = create_agent(
    model=model,
    tools=[retrieve_from_pdf, web_search_tool],
    system_prompt=system_prompt
)

user_query = "Compare the attention mechanism from the paper with Flash Attention"

response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
})

print(response["messages"][-1].content)