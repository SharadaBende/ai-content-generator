from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import generate

app = FastAPI(title="AI Content Generator")

from app.config import settings

allowed_origins = ["*"] if not settings.is_production else [
    "https://your-production-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate.router)

@app.get("/")
def read_root():
    return {"message": "AI Content Generator API is running 🚀"}