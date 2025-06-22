# 🧠 Customer Support Ticket Analyzer

This project implements a multi-agent AI system that classifies, analyzes sentiment, and routes customer support tickets using OpenAI models and the `pydantic-ai` framework.

## 📌 Objective

Automatically process customer support tickets to determine:
1. 🎯 Issue Category
2. 📊 Customer Sentiment
3. 🧭 Appropriate Department Routing

This supports intelligent prioritization and faster resolution in real-world customer support workflows.

---

## 🛠️ Tech Stack

| Component      | Tool/Library                                             |
|----------------|----------------------------------------------------------|
| Language       | Python 3.10+                                             |
| LLM API        | OpenAI (`gpt-4o`, `gpt-4o-mini`)                         |
| Orchestration  | [`pydantic-ai`](https://github.com/pydantic/pydantic-ai) |
| Config         | `python-dotenv`                                          |
| Logs           | Text file (`ai_chat_history.txt`)                        |

---

## 🧩 Agent Architecture
Ticket
├──> 🎯 ClassifierAgent → [Billing, Technical, Account, Feature Request, Other]
├──> 📊 SentimentAgent → [Positive, Neutral, Negative]
└──> 🧭 RouterAgent → [Tech Support, Escalations, Product Team, etc.]

Each agent uses a prompt template defined in `agents/prompts.py`.

---

1. Set OpenAI API Key
Create a .env file:
OPENAI_API_KEY=sk-...

2. Run Evaluation
python main.py

3. All results will be stored in ai_chat_history.txt
