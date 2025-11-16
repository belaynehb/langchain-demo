# Example of more than two place holder
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
    input_variables=["position", "company", "strengths", "weaknesses"],
    template="""
       You are a career coach. Provide tailored interview tips for the
        position of {position} at {company}.
        Highlight your strengths in {strengths} and prepare for questions
        about your weaknesses such as {weaknesses}.

 
    """
    )
st.title("Interview Tig Generator")

company = st.text_input("Enter the Company")
position = st.text_input("Enter the Position:")
strengths = st.text_area("Strengths:", height=100)
weaknesses = st.text_area("Weaknesses", height=100)

if position and company and strengths and weaknesses:
    response = llm.invoke(prompt_template.format(position=position,
                                                 company=company,
                                                 weaknesses=weaknesses,
                                                 strengths=strengths))
    st.write(response.content)