import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(api_key=api_key)


response = embeddings.embed_documents(
    [
        "I love playing video games",
        "I am going to have movie",
        "I love coding",
        "Hello World",
    ]
)
print(len(response))
print(response[0])