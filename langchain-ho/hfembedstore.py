from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma, FAISS

from pathlib import Path

load_dotenv()

# Data Loading
attention_file_path = Path(__file__).resolve().parent / "attention.txt"
loader = TextLoader(attention_file_path)
docs = loader.load()

# Splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = splitter.split_documents(docs)

# Hugging Face Embeddings and Vector Store(Chroma DB)
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(documents=split_docs, embedding=hf_embeddings, persist_directory="./chroma_db_hf")

vector_retrieve = Chroma(persist_directory="./chroma_db_hf", embedding_function=hf_embeddings)
query = "Self-attention, sometimes called intra-attention"
retrieved_results = vector_retrieve.similarity_search(query, k=1)
# print(retrieved_results)

# FAISS DB
faiss_db_path = "./faiss_db_hf"
vector_store_faiss = FAISS.from_documents(documents=split_docs, embedding=hf_embeddings)
vector_store_faiss.save_local(str(faiss_db_path))

vector_retrieve_faiss = FAISS.load_local(
    str(faiss_db_path),
    hf_embeddings,
    allow_dangerous_deserialization=True,
)
query = "Self-attention, sometimes called intra-attention"
# retrieved_results_faiss = vector_retrieve_faiss.similarity_search(query, k=3)
retrieved_results_faiss = vector_retrieve_faiss.similarity_search_with_score(query, k=3)

for result, score in retrieved_results_faiss:
    print(result.page_content)
    print(score)
    print("###########################")
