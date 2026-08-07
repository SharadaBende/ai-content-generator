from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class GenerateRequest(BaseModel):
    content_type: str = Field(..., example="blog")
    topic: str = Field(..., example="The benefits of remote work")
    tone: str = Field(default="professional", example="professional")
    length: Optional[int] = Field(default=None, example=600)

    @field_validator("topic")
    @classmethod
    def topic_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("topic cannot be empty")
        return v.strip()

    class Config:
        json_schema_extra = {
            "example": {
                "content_type": "blog",
                "topic": "The benefits of remote work",
                "tone": "professional",
                "length": 600
            }
        }


class GenerateResponse(BaseModel):
    id: int
    content_type: str
    topic: str
    tone: str
    length: int
    generated_text: str
    created_at: datetime

    class Config:
        from_attributes = True