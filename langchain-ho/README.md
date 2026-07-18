# LangChain

## Installation

```bash
uv add langchain
uv add langchain_community
uv add langchain-text-splitters
```

## API Keys and Setup

- Create OPENAI API Key in [OpenAI Platform](https://platform.openai.com/home)
- Create LangChain API Key in [LangChain Portal](https://smith.langchain.com)
- Add both API keys in .env file

## Components

1. Load

- TextLoader
- PyPDFLoader
- WebBaseLoader

```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
```

1. Split

- RecursiveCharacterTextSplitter (Generic One)
- CharacterTextSplitter = Splits based on the separators that we mention, default =\n\n
- HTMLHeaderTextSplitter = Split based on the headers that we mention
- RecursiveJsonSplitter = Splits based on the json depth or chunk size mentioned.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import HTMLHeaderTextSplitter
```

1. Embed

## Reference Docs

- [DataIngestion-DocumentLoaders](https://docs.langchain.com/oss/python/integrations/document_loaders)
