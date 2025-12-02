import os
from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
llm = ChatOllama(model="gemma:2b")

question = input("Enter the question: \n")
response = llm.invoke(question)
print(response.content)

# from langchain_community.chat_models import ChatOllama

# llm = ChatOllama(model="gemma:2b")

# question = input("Write your question here \n")
# response = llm.invoke(question)
# print(response.content)
