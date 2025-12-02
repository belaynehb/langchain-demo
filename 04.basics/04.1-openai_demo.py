# import os

# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# load_dotenv()

# API_KEY = os.getenv("OPENAI_API_KEY")
# llm = ChatOpenAI(model="gpt-4o", api_key=API_KEY)

# question = input("Enter the question: \n")
# response = llm.invoke(question)
# print(response.content)

# import os
# from dotenv import load_dotenv

# load_dotenv()
# from langchain_openai import ChatOpenAI

# api_key = os.getenv("OPENAI_API_KEY")
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

# question = input("Write your question here \n")
# response = llm.invoke(question)
# print(response.content)

## USING GOOGLE GEMINI
import os
import getpass

from dotenv import load_dotenv

# from langchain_google_vertexai import ChatVertexAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

# API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

question = input("Enter the question: \n")
response = llm.invoke(question)
print(response.content)
