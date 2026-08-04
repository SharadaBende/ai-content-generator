from groq import Groq
from app.config import settings
from app.content_types.registry import get_content_type

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_content(content_type: str, topic: str, tone: str, length: int) -> str:
    config = get_content_type(content_type)
    if not config:
        raise ValueError(f"Unsupported content type: {content_type}")

    prompt = config["prompt_template"].format(
        topic=topic,
        tone=tone,
        length=length
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content