from pydantic import BaseModel, Field
from typing import Optional


class GenerateRequest(BaseModel):
    content_type: str = Field(..., example="blog")
    topic: str = Field(..., example="The benefits of remote work")
    tone: str = Field(default="professional", example="professional")
    length: Optional[int] = Field(default=None, example=600)

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
    content_type: str
    generated_text: str