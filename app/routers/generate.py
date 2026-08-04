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
        error_message = str(e)
        if "rate_limit" in error_message.lower() or "429" in error_message:
            raise HTTPException(
                status_code=503,
                detail="The AI service is temporarily busy (rate limit). Please try again in a moment."
            )
        raise HTTPException(
            status_code=502,
            detail=f"Content generation failed: {error_message}"
        )

    return GenerateResponse(
        content_type=request.content_type,
        generated_text=text
    )