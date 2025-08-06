# --- train_classifier.py (for tools/intent_classifier) ---
import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load your dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sample_queries.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

def train_model():
    df = pd.read_csv(DATA_PATH)

    if 'text' not in df.columns or 'intent' not in df.columns:
        raise ValueError("CSV must have 'text' and 'intent' columns")

    X = df['text']
    y = df['intent']

    # Split for evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorizer + Classifier
    vectorizer = TfidfVectorizer()
    classifier = MultinomialNB()

    X_train_vec = vectorizer.fit_transform(X_train)
    classifier.fit(X_train_vec, y_train)

    # Evaluation
    X_test_vec = vectorizer.transform(X_test)
    predictions = classifier.predict(X_test_vec)
    print("[Evaluation]")
    print(classification_report(y_test, predictions))

    # Save vectorizer and classifier as a tuple
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump((vectorizer, classifier), f)
    print(f"[Model Saved] -> {MODEL_PATH}")

if __name__ == "__main__":
    train_model()