# Example of more than two place holder
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
#llm=ChatOllama(model="mistral:latest")
prompt_template = ChatPromptTemplate(
    [
        ("system", "You are Agile Coach. Answer any questions related to the agile process"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human" , "{input}")
    ]
)

chain = prompt_template | llm

history_for_chain = ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id:history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

print("Agile Guide")

while True:
    question =input("Enter your agile question here:")
    if question:
        response = chain_with_history.invoke({"input":question}, config={"configurable":{"session_id":"abc123"}})
        print(response.content)