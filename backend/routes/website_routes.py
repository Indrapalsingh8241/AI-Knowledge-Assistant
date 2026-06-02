from fastapi import APIRouter


from backend.services.website_service import get_website_text
from backend.services.vector_store_services import create_vector_db


router = APIRouter()
from pydantic import BaseModel

class WebsiteRequest(BaseModel):
    url: str

@router.post("/webload")

async def load_website(data: WebsiteRequest):

    text = get_website_text(data.url)

    create_vector_db(text)

    return {
        "message": "Website loaded successfully"
    }