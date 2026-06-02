from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.RAG_service import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

class ChatRequest(BaseModel):
    question: str


@router.post("/ask")
def chat(data: ChatRequest):

    response = ask_question(
        data.question
    )

    return {
        "answer": response
    }