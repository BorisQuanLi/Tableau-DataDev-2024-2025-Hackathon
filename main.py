from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    logging.info("Starting server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    logging.info("Server started.")
