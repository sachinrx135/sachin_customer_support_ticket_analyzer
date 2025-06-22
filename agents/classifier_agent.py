from .base_agent import BaseAgent
from .prompts import PROMPTS

class TicketClassifier(BaseAgent):
    def __init__(self, model="openai:gpt-4o-mini"):
        super().__init__("ClassifierAgent", PROMPTS["ticket_classifier"], model)

    def classify(self, ticket: dict) -> str:
        return self.run(ticket)
