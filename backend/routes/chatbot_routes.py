from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.llm_services import simple_chat

router = APIRouter(
   prefix="/chatbot",
   tags=["Chatbot"]
)

class ChatRequest(BaseModel):
    question: str


@router.post("/simple_chat")
def chat(data: ChatRequest):

    response = simple_chat(
        data.question
    )

    return {
        "answer": response
    }