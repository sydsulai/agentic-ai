from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Data Loading
attention_file_path = Path(__file__).resolve().parent / "attention.txt"
loader = TextLoader(attention_file_path)
docs = loader.load()

# text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)
# print(len(split_docs))

# Vector Embedding and Vector Store
openai_embeddings_1024 = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
vector_store = Chroma.from_documents(documents=split_docs, embedding=openai_embeddings_1024, persist_directory="./chroma_db")
print(vector_store)

# Vector retrieve using persist Directory
vector_retrieve = Chroma(persist_directory="./chroma_db", embedding_function=openai_embeddings_1024)
query = "Self-attention, sometimes called intra-attention"
retrieved_results = vector_retrieve.similarity_search(query, k=3)
print(f"Retrieved results for query '{query}':")
for result in retrieved_results:
    print(result)