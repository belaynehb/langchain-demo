import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=API_KEY)

question = input("Enter the question: \n")
response = llm.invoke(question)
print(response.content)

# import os
# from dotenv import load_dotenv

# load_dotenv()
# from langchain_openai import ChatOpenAI

# api_key = os.getenv("OPENAI_API_KEY")
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

# question = input("Write your question here \n")
# response = llm.invoke(question)
# print(response.content)
