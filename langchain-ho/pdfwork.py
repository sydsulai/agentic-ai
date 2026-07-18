from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import bs4


# parse_only = bs4.SoupStrainer(id="main-col-body")
# loader = WebBaseLoader(
#     web_paths=["https://docs.aws.amazon.com/eks/latest/userguide/argocd-comparison.html"],
#     bs_kwargs={"parse_only": parse_only},
# )
# docs = loader.load()

file_path = Path(__file__).resolve().parent / "attention.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)
print(f"Number of split documents: {len(split_docs)}")
