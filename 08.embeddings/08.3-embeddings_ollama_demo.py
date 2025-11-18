from dotenv import load_dotenv

from langchain_ollama import OllamaEmbeddings


load_dotenv()

llm = OllamaEmbeddings(model="llama3.2")

text = input("Enter the text: \n")
response = llm.embed_query(text)
print(response)
