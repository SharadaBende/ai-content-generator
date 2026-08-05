import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"

settings = Settings()