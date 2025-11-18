from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

llm = OllamaEmbeddings(model="llama3.2")


document = TextLoader("job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=15)
chunks = text_splitter.split_documents(document)
db = FAISS.from_documents(chunks, llm)
retriever = db.as_retriever()

text = input("Enter the query: \n")


docs = retriever.invoke(text)

for doc in docs:
    print(doc.page_content)
