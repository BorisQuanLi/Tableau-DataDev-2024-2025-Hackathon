import pytest
from backend.multi_agent_llm.communication_agent import CommunicationAgent

def test_communicate_results():
    agent = CommunicationAgent()
    assert agent.communicate_results() is None
