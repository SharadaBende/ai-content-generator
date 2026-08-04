from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Generation(Base):
    __tablename__ = "generations"

    id = Column(Integer, primary_key=True, index=True)
    content_type = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    tone = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    generated_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())