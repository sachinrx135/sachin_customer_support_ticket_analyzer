from datetime import datetime

def log_chat(agent_name: str, prompt: str, response: str, ticket_id: str = None):
    ts = datetime.utcnow().isoformat()
    header = f"\n--- {agent_name} | {ts}"
    if ticket_id:
        header += f" | Ticket ID: {ticket_id}"
    header += " ---\n"
    with open("ai_chat_history.txt", "a", encoding="utf-8") as f:
        f.write(header)
        f.write("Prompt:\n" + prompt + "\n")
        f.write("Response:\n" + response + "\n")
