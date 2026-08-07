from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.schemas import GenerateRequest, GenerateResponse
from app.services.llm_service import generate_content
from app.content_types.registry import get_content_type
from app.database import get_db
from app.models.db_models import Generation
from app.logger import logger

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest, db: Session = Depends(get_db)):
    logger.info(f"Generate request received: type={request.content_type}, topic='{request.topic}'")

    config = get_content_type(request.content_type)
    if not config:
        logger.warning(f"Unsupported content_type requested: {request.content_type}")
        raise HTTPException(status_code=400, detail=f"Unsupported content_type: {request.content_type}")

    length = request.length or config["default_length"]

    try:
        text = generate_content(
            content_type=request.content_type,
            topic=request.topic,
            tone=request.tone,
            length=length
        )
        logger.info(f"Generation succeeded: type={request.content_type}, length={len(text)} chars")
    except Exception as e:
        error_message = str(e)
        logger.error(f"Generation failed: type={request.content_type}, error={error_message}")
        if "rate_limit" in error_message.lower() or "429" in error_message:
            raise HTTPException(
                status_code=503,
                detail="The AI service is temporarily busy (rate limit). Please try again in a moment."
            )
        raise HTTPException(
            status_code=502,
            detail=f"Content generation failed: {error_message}"
        )

    new_generation = Generation(
        content_type=request.content_type,
        topic=request.topic,
        tone=request.tone,
        length=length,
        generated_text=text
    )
    db.add(new_generation)
    db.commit()
    logger.info(f"Generation saved to database: id={new_generation.id}")

    return new_generation


   


@router.get("/history")
def get_history(limit: int = 20, db: Session = Depends(get_db)):
    generations = (
        db.query(Generation)
        .order_by(Generation.created_at.desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "id": g.id,
            "content_type": g.content_type,
            "topic": g.topic,
            "tone": g.tone,
            "length": g.length,
            "generated_text": g.generated_text,
            "created_at": g.created_at
        }
        for g in generations
    ]