import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=500
    
)
question = "What is RAG in simple terms?"
def simple_chat(question):

    response = llm.invoke(question)

    return response.content
