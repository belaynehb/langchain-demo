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

subject_prompt = PromptTemplate(
    input_variables=["product_name", "features"],
    template="""
       You are an experienced marketing specialist.  
    Create a catchy subject line for a marketing  
    email promoting the following product: {product_name}.  
    Highlight these features: {features}.  
    Respond with only the subject line. 
 
    """
    )

email_prompt = PromptTemplate(
    input_variables=["product_name", "subject_line","target_audience"],
    template="""
       Write a marketing email of 300 words for the  
    product: {product_name}. Use the subject line: 
     {subject_line}. Tailor the message for the  
     following target audience: {target_audience}. 
      Format the output as a JSON object with three  
      keys: 'subject', 'audience', 'email' and fill  
      them with respective values. 
 
    """
    )

product_name = st.text_input("Enter the Product name:")
features = st.text_input("Input the product features (Comma-separated)")
target_audience = st.text_input("Enter the target audience")

first_chain = subject_prompt | llm | StrOutputParser() 
second_chain = email_prompt | llm | JsonOutputParser()
final_chain = first_chain | (lambda subject_line: {"product_name": product_name, "subject_line": subject_line, "target_audience": target_audience}) | second_chain

st.title("Marketing email Generator")




if product_name and features and target_audience:
    response = final_chain.invoke({"product_name": product_name, "features": features})
    st.write(response)