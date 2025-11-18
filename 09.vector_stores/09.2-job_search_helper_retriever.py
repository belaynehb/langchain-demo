import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAIEmbeddings(api_key=api_key)


document = TextLoader("job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=15)
chunks = text_splitter.split_documents(document)
db = Chroma.from_documents(chunks, llm)
retriever = db.as_retriever()

text = input("Enter the query: \n")


docs = retriever.invoke(text)

for doc in docs:
    print(doc.page_content)
