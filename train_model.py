"""
train_model.py
----------------
Trains a Spam vs Ham (Not Spam) text classifier using TF-IDF + Naive Bayes
and saves the trained model + vectorizer to disk for use in the Flask app.

Run:
    python train_model.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os

DATA_PATH = os.path.join("data", "spam.csv")
MODEL_DIR = "model"

def main():
    # 1. Load dataset
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} messages -> {df['label'].value_counts().to_dict()}")

    X = df["message"]
    y = df["label"].map({"ham": 0, "spam": 1})  # 0 = Not Spam, 1 = Spam

    # 2. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Convert text to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 4. Train Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # 5. Evaluate
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nTest Accuracy: {acc * 100:.2f}%\n")
    print("Classification Report:\n", classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # 6. Save model + vectorizer
    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(os.path.join(MODEL_DIR, "spam_model.pkl"), "wb") as f:
        pickle.dump(model, f)
    with open(os.path.join(MODEL_DIR, "vectorizer.pkl"), "wb") as f:
        pickle.dump(vectorizer, f)

    print(f"\nModel and vectorizer saved in '{MODEL_DIR}/' directory.")

if __name__ == "__main__":
    main()
