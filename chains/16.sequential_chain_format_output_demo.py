# Example of more than two place holder
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

#from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
#llm=ChatOllama(model="mistral:latest")

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
    input_variables=["topic", "emotion"],
    template="""
       You need to write a powerful {emotion} speech of 350 words
        for the following title: {title}
        Format the output with keys: 'title', 'emotion','speech' and fill them with the respective values.
 
    """
    )

first_chain = title_prompt | llm | StrOutputParser() | (lambda title:(st.write(title), title)[1])
second_chain = speech_prompt | llm | JsonOutputParser()
final_chain = first_chain | (lambda title: {"title": title, "emotion": emotion}) | second_chain

st.title("Speech Generator")

topic = st.text_input("Enter the Topic:")
emotion = st.text_input("Enter the emotion")


if topic and emotion:
    response = final_chain.invoke({"topic":topic})
    st.write(response)