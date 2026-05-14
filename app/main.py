import logging

from fastapi import FastAPI

from app.api.routes import router

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="GitHub Profile Analyzer",
    description="Analyze GitHub developer profiles",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "GitHub Profile Analyzer API is running"
    }