# tools/faq_bot/faq_bot.py

import json
import os

FAQ_PATH = os.path.join(os.path.dirname(__file__), 'faq_data.json')

def load_faq_data():
    try:
        with open(FAQ_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[FAQBot] Failed to load FAQ data: {e}")
        return []

def get_faq_response(query):
    faq_data = load_faq_data()

    query = query.lower()
    for item in faq_data:
        if query in item["question"].lower():
            return item["answer"]
    return "Sorry, I couldn't find an answer to that question."