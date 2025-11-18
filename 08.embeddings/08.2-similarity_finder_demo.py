import os
from dotenv import load_dotenv
import numpy as np

from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAIEmbeddings(api_key=api_key)

text1 = input("Enter the text: \n")
text2 = input("Enter the text: \n")
response1 = llm.embed_query(text1)
response2 = llm.embed_query(text2)

similarity_score = np.dot(response1, response2)

print(similarity_score)
