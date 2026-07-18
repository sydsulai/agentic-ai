from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import HTMLHeaderTextSplitter
import bs4


# parse_only = bs4.SoupStrainer(id="main-col-body")
# loader = WebBaseLoader(
#     web_paths=["https://docs.aws.amazon.com/eks/latest/userguide/argocd-comparison.html"],
#     bs_kwargs={"parse_only": parse_only},
# )
# docs = loader.load()
# print(docs)

headers_to_split_on = [("h1", "Section"), ("h2", "Subsection"), ("h3", "Topic")]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_splits = html_splitter.split_text_from_url("https://docs.aws.amazon.com/eks/latest/userguide/argocd-comparison.html")
print(html_splits)