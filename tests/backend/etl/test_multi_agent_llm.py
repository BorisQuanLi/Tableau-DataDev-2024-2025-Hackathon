import sys
sys.path.insert(0, '/mnt/c/Users/Boris_Li/OneDrive/Job_search_2024/Software_Engineer_roles/Tableau-DataDev-2024-2025-Hackathon')
from backend.etl.multi_agent_llm import CommunicationAgent, DataIngestionAgent, InferenceAgent, LLMAgent, ModelTrainingAgent

def test_communication_agent():
    agent = CommunicationAgent()
    response = agent.communicate("Hello")
    assert response is not None

def test_data_ingestion_agent():
    agent = DataIngestionAgent()
    data = agent.ingest_data()
    assert data is not None

def test_inference_agent():
    agent = InferenceAgent()
    result = agent.infer("input data")
    assert result is not None

def test_llm_agent():
    agent = LLMAgent()
    model = agent.load_model()
    assert model is not None

def test_model_training_agent():
    agent = ModelTrainingAgent()
    model = agent.train_model()
    assert model is not None
