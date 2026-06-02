import os

print("===== APP STARTING =====")
print("GROQ_API_KEY exists:", bool(os.getenv("GROQ_API_KEY")))
import sys
import ssl

print("Python:", sys.version)
print("Executable:", sys.executable)
print("SSL:", ssl.OPENSSL_VERSION)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.youtube_routes import router as youtube_router
from backend.routes.chat_routes import router as chat_router
from backend.routes.pdf_routes import router as pdf_router
from backend.routes.website_routes import router as website_router
from backend.routes.chatbot_routes import router as chatbot_router

app = FastAPI(title="YouTube RAG Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(youtube_router)
app.include_router(chat_router)
app.include_router(pdf_router)
app.include_router(website_router)
app.include_router(chatbot_router)

@app.get("/")
def home():
    return {"message": "YouTube RAG Chatbot API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}