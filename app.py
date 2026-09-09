"""
app.py
------
A simple Flask web app that loads the trained spam classifier and
lets the user check whether a message is Spam or Not Spam via a web form.

Run (after training the model):
    python app.py

Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "spam_model.pkl")
VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")

# Load model and vectorizer once at startup
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        if message.strip():
            vec = vectorizer.transform([message])
            prediction = model.predict(vec)[0]
            proba = model.predict_proba(vec)[0]

            result = "SPAM" if prediction == 1 else "NOT SPAM"
            confidence = round(max(proba) * 100, 2)

    return render_template("index.html", result=result, confidence=confidence, message=message)


if __name__ == "__main__":
    app.run(debug=True)
