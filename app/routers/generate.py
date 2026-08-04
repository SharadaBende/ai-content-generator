from fastapi import APIRouter, HTTPException
from app.models.schemas import GenerateRequest, GenerateResponse
from app.services.llm_service import generate_content
from app.content_types.registry import get_content_type

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    config = get_content_type(request.content_type)
    if not config:
        raise HTTPException(status_code=400, detail=f"Unsupported content_type: {request.content_type}")

    length = request.length or config["default_length"]

    try:
        text = generate_content(
            content_type=request.content_type,
            topic=request.topic,
            tone=request.tone,
            length=length
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return GenerateResponse(
        content_type=request.content_type,
        generated_text=text
    )