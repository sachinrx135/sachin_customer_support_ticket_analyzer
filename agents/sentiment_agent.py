from .base_agent import BaseAgent
from .prompts import PROMPTS

class SentimentAnalyzer(BaseAgent):
    def __init__(self, model="openai:gpt-4o-mini"):
        super().__init__("SentimentAgent", PROMPTS["sentiment_analysis"], model)

    def analyze(self, ticket: dict) -> str:
        return self.run(ticket)
