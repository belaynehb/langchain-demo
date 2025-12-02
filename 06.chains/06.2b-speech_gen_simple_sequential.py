import os
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=API_KEY)
title_template = PromptTemplate(
    input_variables=["topic"],
    template="""
        You are an experienced speech writer.
        You need to craft an impactful title for a speech on the following tocpic: {topic}
        Answer exactly with one title.
    """,
)

speech_template = PromptTemplate(
    input_variables=["title"],
    template="""
        You need to write a powerful speech of 350 words for the following title: {title}.
    """,
)
st.title("Speech Generator")

first_chain = title_template | llm | StrOutputParser()
second_chain = speech_template | llm
final_chain = first_chain | second_chain

topic = st.text_input("Enter the topic:")


if topic:
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)
