## TURNING ON THE DEBUG ON CHATOLLAMA

# from langchain_community.chat_models import ChatOllama
# from langchain_core.globals import set_debug
# import streamlit as st

# set_debug(True)

# st.title("Ask your question")
# llm = ChatOllama(model="gemma3:270m")

# question = st.text_input("What is your question?")

# if question:
#     response = llm.invoke(question)
#     st.write(response.content)


## TURNING ON THE DEBUG ON OPENAI
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug

load_dotenv()
set_debug(True)

api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

st.title("Ask any question")

question = st.text_input("Enter your question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
