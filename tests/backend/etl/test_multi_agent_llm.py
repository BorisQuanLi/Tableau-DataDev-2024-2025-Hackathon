import sys
# This file is intentionally left blank to make the directory a package.
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../app')))

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
