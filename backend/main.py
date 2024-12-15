from fastapi import FastAPI
from backend.multi_agent_llm.llm_agent import LLMAgent
from backend.multi_agent_llm.data_ingestion_agent import ingest_data
from backend.multi_agent_llm.model_training_agent import train_model
from backend.multi_agent_llm.inference_agent import generate_predictions
from backend.multi_agent_llm.communication_agent import communicate

app = FastAPI()
messages_list: dict[int, str] = {}

@app.get("/")
def read_main() -> dict[str, str]:
    return {"message": "Hello"}

@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}

@app.post("/messages/{msg_name}/")
def add_msg(msg_name: str) -> dict[str, str]:
    msg_id = max(messages_list.keys()) + 1 if messages_list else 0
    messages_list[msg_id] = msg_name
    return {"message": messages_list[msg_id]}

@app.get("/messages")
def message_items() -> dict[str, dict[int, str]]:
    return {"messages": messages_list}

@app.post("/ingest_data/")
def ingest_data_route() -> dict[str, str]:
    ingest_data()
    return {"message": "Data ingestion completed"}

@app.post("/train_model/")
def train_model_route() -> dict[str, str]:
    train_model()
    return {"message": "Model training completed"}

@app.post("/generate_predictions/")
def generate_predictions_route() -> dict[str, str]:
    generate_predictions()
    return {"message": "Predictions generated"}

@app.post("/communicate/")
def communicate_route() -> dict[str, str]:
    communicate()
    return {"message": "Communication completed"}

def main():
    llm_agent = LLMAgent()
    llm_agent.run()

if __name__ == "__main__":
    main()
