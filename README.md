# Ninja API Wrapper

A FastAPI wrapper for API Ninjas endpoints providing trivia and facts.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

3. Add your API Ninjas API key to the `.env` file

## Running the Application

```bash
python facts/app.py
```

Or using uvicorn:
```bash
uvicorn facts.app:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /v1/trivia` - Get random trivia questions and answers
- `GET /v1/triviaoftheday` - Get today's trivia question (updated every day)
- `GET /v1/facts` - Get random facts
- `GET /v1/factoftheday` - Get today's fact (updated every day)


## Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
