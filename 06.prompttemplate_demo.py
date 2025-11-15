import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st


#from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
#llm=ChatOllama(model="mistral:latest")
prompt_template = PromptTemplate(
    input_variables=["country"],
    template="""
       You are an expert in traditional cuisines.
        You provide information about a specific dish from a specific country.
        Avoid giving information about fictional places. If the country is fictional
        or non-existent answer: I don't know.
        Answer the question: What is the traditional cuisine of {country}? 
    """
    )
st.title("Cuisine Info")

country = st.text_input("Enter the country:")

if country:
    response = llm.invoke(prompt_template.format(country=country))
    st.write(response.content)