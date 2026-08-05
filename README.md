# AI Content Generator

A full-stack web application that generates AI-powered content (blog posts, social media captions, and ad copy) using Groq's Llama 3.3 model. Built with FastAPI, SQLite, and vanilla JavaScript.

## Features

- **Multi-type content generation** — Blog posts, social media captions, and ad copy, powered by an extensible content-type registry
- **AI-powered** — Uses Groq's Llama 3.3 70B model for fast, high-quality generation
- **Generation history** — All generations are saved to a SQLite database and viewable in the UI
- **Input validation** — Both frontend and backend validation to prevent bad requests
- **Clean error handling** — Graceful handling of rate limits and API failures
- **Simple, dependency-free frontend** — No build tools required

## Tech Stack

**Backend**
- FastAPI — REST API framework
- SQLAlchemy — ORM for database access
- SQLite — Lightweight local database
- Groq API (Llama 3.3 70B) — AI content generation
- Pydantic — Request/response validation

**Frontend**
- HTML, CSS, JavaScript (no frameworks)

## Project Structure

ai-content-generator/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── config.py # Environment variable loading
│ ├── database.py # Database connection setup
│ ├── models/
│ │ ├── schemas.py # Pydantic request/response models
│ │ └── db_models.py # SQLAlchemy database models
│ ├── content_types/
│ │ └── registry.py # Content type configs (blog, caption, ad_copy)
│ ├── services/
│ │ └── llm_service.py # Groq API integration
│ └── routers/
│ └── generate.py # /generate and /history endpoints
├── frontend/
│ └── index.html # Frontend UI
├── requirements.txt
└── README.md


## How It Works

1. User fills out a form (content type, topic, tone, length) in the frontend
2. Frontend sends a `POST` request to the `/generate` endpoint
3. Backend looks up the content type's prompt template from the registry
4. Backend calls the Groq API with the filled-in prompt
5. Generated content is saved to the database and returned to the frontend
6. Frontend displays the result and refreshes the history list

## Getting Started

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com)

### Installation

1. Clone the repository
```bash
git clone https://github.com/SharadaBende/ai-content-generator.git
cd ai-content-generator
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\Activate      # Windows
source venv/bin/activate   # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a `.env` file in the project root:



GROQ_API_KEY=your_groq_api_key_here


5. Create the database tables
```bash
python create_tables.py
```

6. Run the server
```bash
uvicorn app.main:app --reload
```

7. Open the frontend

Open `frontend/index.html` directly in your browser.

## API Endpoints

| Method | Endpoint    | Description                          |
|--------|-------------|---------------------------------------|
| POST   | `/generate` | Generate content for a given type/topic |
| GET    | `/history`  | Retrieve past generations (default limit: 20) |
| GET    | `/docs`     | Interactive API documentation (Swagger UI) |

### Example Request
```json
POST /generate
{
  "content_type": "blog",
  "topic": "benefits of remote work",
  "tone": "professional",
  "length": 600
}
```

## Supported Content Types

| Type      | Description                    |
|-----------|---------------------------------|
| `blog`    | Long-form blog posts with headings |
| `caption` | Short social media captions with hashtags |
| `ad_copy` | Persuasive ad copy with a call-to-action |

New content types can be added by extending `app/content_types/registry.py` — no other code changes required.

## Future Improvements

- Deploy to a live hosting platform
- Add user authentication
- Delete/favorite past generations
- Support for additional content types (email subject lines, product descriptions)

## License

MIT

A few things I built in here on purpose:

Screenshots section is missing intentionally — I'd suggest taking 1-2 screenshots of your working frontend and adding them near the top (![screenshot](path/to/image.png)) — visuals massively boost how professional a README feels
The API table and example request show you understand documenting an interface, not just building one
"Future Improvements" section signals to anyone reading that you know what's next, which reads as intentional rather than incomplete
