import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(api_key=api_key)
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)


document = PyPDFLoader("academic_research_data.pdf").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(document)
vector_store = Chroma.from_documents(chunks, embeddings)
retriever = vector_store.as_retriever()

prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            """You are an assistant for answering questions.
         Use the provided context to respond. If the answer isn't clear, acknowledge
         that you don't know.
         Limit your response to three concise sentences.
         {context}""",
        ),
        ("human", "{input}"),
    ]
)

qa_chain = create_stuff_documents_chain(llm, prompt_template)
rag_chain = create_retrieval_chain(retriever, qa_chain)

print("Chat with Document")
question = input("Your Question")

if question:
    response = rag_chain.invoke({"input":question})
    print(response['answer'])

'''
1- What is the status of my order #98765?

2. Can you provide details about the features of the XYZ smartphone?

3. What is your return policy for electronics?

4. I received a damaged item in my order. How can I get a replacement?

5. Can you recomment a good smartphone for gaming under $500?

6. How do I apply for a job at your company?
'''