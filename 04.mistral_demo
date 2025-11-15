#import os
#from dotenv import load_dotenv

#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

#load_dotenv()

#api_key = os.getenv("OPENAI_API_KEY")
#llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
llm=ChatOllama(model="mistral:latest")

question=input("Enter the question: \n")
response = llm.invoke(question)
print(response.content)