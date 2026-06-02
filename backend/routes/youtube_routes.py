from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

from backend.services.youtube_service import YouTubeTranscriptApi,get_transcript
from backend.services.vector_store_services import create_vector_db, get_db


router = APIRouter(
    prefix="/youtube",
    tags=["YouTube"]
)

class VideoRequest(BaseModel):
    video_url: str

@router.post("/load-video")
async def load_video(data: VideoRequest):
    try:
        transcript = get_transcript(data.video_url)

        if not transcript:
            return {"error": "Transcript not found"}

        create_vector_db(transcript)

        return {
            "status": "success",
            "message": "Video loaded successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@router.delete("/reset")
def reset_chat():

    # Optional
    return {
        "message": "Vector database cleared"
    }