import json
import requests

from langchain_text_splitters import RecursiveJsonSplitter

json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()

json_splitter = RecursiveJsonSplitter(max_chunk_size=100)
# split_json = json_splitter.split_json(json_data)
# print(split_json)
split_json_to_docs = json_splitter.create_documents(texts=[json_data])
for i in range(3):
    print(split_json_to_docs[i])
