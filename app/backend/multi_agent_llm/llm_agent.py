from .communication_agent import CommunicationAgent
from .data_ingestion_agent import DataIngestionAgent
from .inference_agent import InferenceAgent
from .model_training_agent import ModelTrainingAgent

class LLMAgent:
    def __init__(self):
        self.communication_agent = CommunicationAgent()
        self.data_ingestion_agent = DataIngestionAgent()
        self.inference_agent = InferenceAgent()
        self.model_training_agent = ModelTrainingAgent()

    def run(self):
        # Example workflow
        self.data_ingestion_agent.ingest_data()
        self.model_training_agent.train_model()
        self.inference_agent.run_inference()
        self.communication_agent.communicate_results()

if __name__ == "__main__":
    llm_agent = LLMAgent()
    llm_agent.run()
