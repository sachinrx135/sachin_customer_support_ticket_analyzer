import json
from agents.classifier_agent import TicketClassifier
from agents.sentiment_agent import SentimentAnalyzer
from agents.router_agent import RouterAgent

def analyze_ticket(ticket: dict, classifier, sentiment, router) -> dict:
    category = classifier.classify(ticket)
    mood = sentiment.analyze(ticket)
    department = router.route(ticket, category, mood)
    return {
        "ticket_id": ticket.get("ticket_id"),
        "category": category,
        "sentiment": mood,
        "department": department
    }

def evaluate(file_path="evaluation/test_cases.json"):
    classifier = TicketClassifier()
    sentiment = SentimentAnalyzer()
    router = RouterAgent()

    with open(file_path) as f:
        tickets = json.load(f)

    results = [analyze_ticket(t, classifier, sentiment, router) for t in tickets]
    with open("evaluation/results.json", "w") as out:
        json.dump(results, out, indent=2)
    print("✅ Evaluation complete. Results written to evaluation/results.json")
