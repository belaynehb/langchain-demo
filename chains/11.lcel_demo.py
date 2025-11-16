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
    input_variables=["city", "month", "language", "budget"],
    template="""
       Welcome to the {city} travel guide!
        If you're visiting in {month}, here's what you can do:
        1. Must-visit attractions.
        2. Local cuisine you must try.
        3. Useful phrases in {language}.
        4. Tips for traveling on a {budget} budget.
        Enjoy your trip!
 
    """
    )
st.title("Travel Guide")

city = st.text_input("Enter the City:")
month = st.text_input("Enter the Month of travel")
language = st.text_input("Enter the Language")
budget = st.selectbox("Travel Budget", ["Low", "Medium", "High"])

chain = prompt_template | llm

if city and month and language and budget:
    response = chain.invoke({"city":city,
                            "month":month,
                            "language":language,
                            "budget":budget})
    st.write(response.content)