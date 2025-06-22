from pydantic_ai import Agent
from utils.logger import log_chat

class BaseAgent:
    def __init__(self, name: str, prompt_template: str, model: str = "openai:gpt-4o-mini"):
        self.agent = Agent(
            model,
            name=name,
            system_prompt="You are " + name
        )
        self.prompt_template = prompt_template

    def run(self, ticket: dict, **kwargs) -> str:
        prompt = self.prompt_template.format(**ticket, **kwargs)
        res = self.agent.run_sync(prompt)
        output = res.output.strip()
        log_chat(self.agent.name, prompt, output, ticket_id=ticket.get("ticket_id"))
        return output
