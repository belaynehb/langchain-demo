from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st


llm = ChatOllama(model="gemma3:270m")

st.title("Couisine app")
country = st.text_input("Enter the country")
prompt_template = PromptTemplate(
    input_variables=["country"],
    template="""
        You are an expert in traditional cuisines. You provid information about a specific dish from a specific country.
        Answer the question: What is the traditinal cuisine of {country}?
        """,
)

if country:
    response = llm.invoke(prompt_template.format(country=country))
    st.write(response.content)
