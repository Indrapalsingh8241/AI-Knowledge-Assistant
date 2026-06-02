from fastapi import APIRouter
from fastapi import UploadFile

from backend.services.pdf_service import extract_pdf_text
from backend.services.vector_store_services import create_vector_db

router = APIRouter()

@router.post("/pdfload")

async def load_pdf(file: UploadFile):

    text = extract_pdf_text(file.file)

    create_vector_db(text)

    return {
        "message": "PDF loaded successfully"
    }