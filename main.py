from fastapi import FastAPI
import logging
import uvicorn
from dotenv import load_dotenv
import os
from app.routes import router

logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routes from the app package
app.include_router(router)

if __name__ == "__main__":
    logging.info("Starting server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    logging.info("Server started.")
