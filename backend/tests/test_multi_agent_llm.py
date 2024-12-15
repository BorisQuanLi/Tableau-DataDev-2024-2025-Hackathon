import pytest
from backend.multi_agent_llm.communication_agent import CommunicationAgent
from backend.multi_agent_llm.data_ingestion_agent import DataIngestionAgent
from backend.multi_agent_llm.inference_agent import InferenceAgent
from backend.multi_agent_llm.model_training_agent import ModelTrainingAgent
from backend.multi_agent_llm.llm_agent import LLMAgent

def test_communicate_results():
    agent = CommunicationAgent()
    assert agent.communicate_results() is None

def test_ingest_data():
    agent = DataIngestionAgent()
    assert agent.ingest_data() is None

def test_run_inference():
    agent = InferenceAgent()
    assert agent.run_inference() is None

def test_train_model():
    agent = ModelTrainingAgent()
    assert agent.train_model() is None

def test_llm_agent_run():
    agent = LLMAgent()
    assert agent.run() is None
