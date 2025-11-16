# Example of more than two place holder
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm_open_ai=ChatOpenAI(model="gpt-4o", api_key=api_key)
llm_mistral=ChatOllama(model="mistral:latest")

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
       You are an experienced speech writer.
    You need to craft an impactful title for a speech
    on the following topic: {topic}
    Answer exactly with one title.
 
    """
    )

speech_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
       You need to write a powerful speech of 350 words
        for the following title: {title}
 
    """
    )

first_chain = title_prompt | llm_open_ai | StrOutputParser() | (lambda title:(st.write(title), title)[1])
second_chain = speech_prompt | llm_mistral
final_chain = first_chain | second_chain

st.title("Speech Generator")

topic = st.text_input("Enter the Topic:")


if topic:
    response = final_chain.invoke({"topic":topic})
    st.write(response.content)