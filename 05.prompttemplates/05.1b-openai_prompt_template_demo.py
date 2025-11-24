import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
prompt_template = PromptTemplate(
    input_variables=["Country"],
    template='''
        You are an expert in traditional cuisines. You provid information about a specific dish from a specific country.
        Answer the question: What is the traditinal cuisine of {country}?
    '''
)

st.title("Cuisine app")
country = st.text_input("Enter a country")

if country:
    response = llm.invoke(prompt_template.format(country=country))
    st.write(response.content)
