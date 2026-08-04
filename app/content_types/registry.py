CONTENT_TYPES = {
    "blog": {
        "name": "Blog Post",
        "prompt_template": (
            "Write a well-structured blog post about '{topic}'. "
            "Tone: {tone}. Target length: approximately {length} words. "
            "Include a catchy title, an introduction, 2-4 body sections with subheadings, "
            "and a short conclusion."
        ),
        "required_fields": ["topic", "tone", "length"],
        "default_length": 600,
    },
    "caption": {
        "name": "Social Media Caption",
        "prompt_template": (
            "Write a {tone} social media caption about '{topic}'. "
            "Keep it under {length} words. Include 3-5 relevant hashtags at the end."
        ),
        "required_fields": ["topic", "tone", "length"],
        "default_length": 40,
    },
    "ad_copy": {
        "name": "Ad Copy",
        "prompt_template": (
            "Write persuasive ad copy for '{topic}'. "
            "Tone: {tone}. Keep it under {length} words. "
            "Focus on a strong hook and a clear call-to-action."
        ),
        "required_fields": ["topic", "tone", "length"],
        "default_length": 50,
    },
}


def get_content_type(content_type: str):
    """Fetch config for a content type, or None if unsupported."""
    return CONTENT_TYPES.get(content_type)


def list_content_types():
    """Return list of supported content type keys."""
    return list(CONTENT_TYPES.keys())