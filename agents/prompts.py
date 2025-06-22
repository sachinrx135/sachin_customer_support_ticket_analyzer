PROMPTS = {
    "ticket_classifier": "Given this ticket (subject: {subject}, message: {message}), classify it into [Billing, Technical, Account, Feature Request, Other]:",
    "sentiment_analysis": "Analyze the sentiment of this message: {message}. Return one word: Positive, Neutral, or Negative.",
    "router": "Route a ticket with category: {category}, sentiment: {sentiment}, and tier: {customer_tier} to the best department: [Tech Support, Billing Team, Customer Success, Escalations, Product Team]."
}
