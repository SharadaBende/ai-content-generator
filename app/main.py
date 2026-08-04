from fastapi import FastAPI
from app.routers import generate

app = FastAPI(title="AI Content Generator")

app.include_router(generate.router)

@app.get("/")
def read_root():
    return {"message": "AI Content Generator API is running 🚀"}