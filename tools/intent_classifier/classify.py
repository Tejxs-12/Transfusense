# --- classify.py ---
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Load the model and vectorizer
try:
    with open(MODEL_PATH, 'rb') as f:
        vectorizer, classifier = pickle.load(f)
except Exception as e:
    print(f"[IntentClassifier] Failed to load model: {e}")
    vectorizer, classifier = None, None

def classify_intent(text):
    if not vectorizer or not classifier:
        return "unknown"

    try:
        X = vectorizer.transform([text])
        intent = classifier.predict(X)[0]
        return intent
    except Exception as e:
        print(f"[IntentClassifier] Error during prediction: {e}")
        return "error"