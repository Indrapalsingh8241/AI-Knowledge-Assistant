import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate

from backend.services.vector_store_services import get_db

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=500
)

prompt = PromptTemplate(

    template="""
You are a helpful AI assistant.

Answer ONLY from the provided context.


defination give only when there is it some definition in the context otherwise leave it blank

give below key points always in this format of points 1 2 3 and so on, if there is no key point in the context  leave it blank:
Key Points:


Summary:

minimul 5 line output and maximum 10 line output if there is some information in the context then give it in character wise leave it blank
Rules:
- Translate the final answer into English before responding
- Never answer in Hindi
- Even if context is Hindi, output must be English only
- Use simple professional language
- Keep answers concise but informative
- Use bullet points only when useful
- Avoid unnecessary headings
- Do not repeat information
- Format answers cleanly

Context:
{context}

Question:
{question}

Answer:
""",

    input_variables=["context", "question"]
)
chat_history=[]
def ask_question(question):
    db = get_db()

    if db is None:
        return "Please load a file first."

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    answer=llm.invoke(prompt.format(context=context, question=question))
    result=(answer.content)
    

    return result