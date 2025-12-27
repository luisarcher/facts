from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Ninja API Wrapper",
    description="A FastAPI wrapper for API Ninjas endpoints",
    version="1.0.0"
)

NINJA_API_BASE_URL = "https://api.api-ninjas.com/v1"
NINJA_API_KEY = os.getenv("NINJA_API_KEY")


async def fetch_from_ninja(endpoint: str):
    """Helper function to fetch data from Ninja API"""
    if not NINJA_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="NINJA_API_KEY not configured in environment variables"
        )
    
    url = f"{NINJA_API_BASE_URL}/{endpoint}"
    headers = {"X-Api-Key": NINJA_API_KEY}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"Error from Ninja API: {e.response.text}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error connecting to Ninja API: {str(e)}"
            )


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Ninja API Wrapper",
        "endpoints": [
            "/v1/trivia",
            "/v1/triviaoftheday",
            "/v1/facts",
            "/v1/factoftheday"
        ]
    }


@app.get("/v1/trivia")
async def get_trivia():
    """Get random trivia question and answer"""
    return await fetch_from_ninja("trivia")


@app.get("/v1/triviaoftheday")
async def get_trivia_of_the_day():
    """Get today's trivia question"""
    return await fetch_from_ninja("trivia")


@app.get("/v1/facts")
async def get_facts():
    """Get random fact"""
    return await fetch_from_ninja("facts")


@app.get("/v1/factoftheday")
async def get_fact_of_the_day():
    """Get today's fact"""
    return await fetch_from_ninja("facts")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
