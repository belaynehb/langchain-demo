# #from langchain_openai import ChatOpenAI
# import streamlit as st
# import logging
# from langchain_community.chat_models import ChatOllama

# from langchain.tools import set_debug

# logging.getLogger("langchain").setLevel(logging.DEBUG)


# #load_dotenv()

# #api_key = os.getenv("OPENAI_API_KEY")
# #llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
# llm=ChatOllama(model="mistral:latest")

# st.title("Ask Anything")

# question = st.text_input("Enter the question:")

# if question:
#     response = llm.invoke(question)
#     st.write(response.content)

## STREAMLIT EXAMPLE WITH OPENAI

# import os
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()


# api_key = os.getenv("OPENAI_API_KEY")
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

# st.title("AI chat")

# question = st.text_input("Enter your question here:")
# response = llm.invoke(question)

# if question:
#     st.write(response.content)


## STEAMLIT EXAMPLE WITH OPEN SOURCE
import streamlit as st
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="gemma:2b")

st.title("Your gemma chat app")
question = st.text_input("Enter your question:")


if question:
    response = llm.invoke(question)
    st.write(response.content)
