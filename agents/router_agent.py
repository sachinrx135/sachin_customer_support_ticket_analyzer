from .base_agent import BaseAgent
from .prompts import PROMPTS

class RouterAgent(BaseAgent):
    def __init__(self, model="openai:gpt-4o-mini"):
        super().__init__("RouterAgent", PROMPTS["router"], model)

    def route(self, ticket: dict, category: str, sentiment: str) -> str:
        return self.run(ticket, category=category, sentiment=sentiment)
