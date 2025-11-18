# Example of more than two place holder
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st


#from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
#llm=ChatOllama(model="mistral:latest")
prompt_template = ChatPromptTemplate(
    [
        ("system", "You are Agile Coach. Answer any questions related to the agile process"),
        ("human" , "{input}")
    ]
)
st.title("Agile Guide")

input = st.text_input("Enter your agile question here:")

chain = prompt_template | llm

if input:
    response = chain.invoke({"input":input})
    st.write(response.content)