import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAIEmbeddings(api_key=api_key)

text = input("Enter the text: \n")
response = llm.embed_query(text)
print(response)
