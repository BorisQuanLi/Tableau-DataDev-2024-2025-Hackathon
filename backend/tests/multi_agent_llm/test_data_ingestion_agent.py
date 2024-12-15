import pytest
from backend.multi_agent_llm.data_ingestion_agent import DataIngestionAgent

def test_ingest_data():
    agent = DataIngestionAgent()
    assert agent.ingest_data() is None
