# Spam Message Detector — ML Mini Project

A simple, complete machine learning project: it classifies text messages as
**Spam** or **Not Spam** using TF-IDF feature extraction + a Multinomial
Naive Bayes classifier, served through a small Flask web app.

## Project Structure
```
spam_detector/
├── data/
│   └── spam.csv          # Labeled dataset (message, label)
├── model/                # Created after training (saved .pkl files)
├── templates/
│   └── index.html        # Web UI
├── train_model.py        # Trains and saves the model
├── app.py                # Flask app to test messages in the browser
├── requirements.txt
└── README.md
```

## How to Run

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Train the model**
   ```
   python train_model.py
   ```
   This reads `data/spam.csv`, trains a TF-IDF + Naive Bayes classifier,
   prints accuracy/classification report, and saves the model to `model/`.

3. **Run the web app**
   ```
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser, type a message, and click
   "Check Message" to see the prediction with a confidence score.

## How It Works (for your report / viva)

1. **Data**: Each row is a message labeled `spam` or `ham` (not spam).
2. **Text → Numbers (TF-IDF)**: `TfidfVectorizer` converts each message into
   a vector of word importance scores, ignoring common English stop words.
3. **Model (Naive Bayes)**: `MultinomialNB` is a probabilistic classifier
   well suited to text/word-count data — fast to train and a standard
   baseline for spam filtering (this is close to how early email spam
   filters worked).
4. **Train/Test Split**: 80% of data trains the model, 20% evaluates it, so
   accuracy is measured on messages the model hasn't seen.
5. **Serving**: Flask loads the saved model + vectorizer once, then predicts
   on-demand for whatever message the user submits through the form.

## Improving It Further (optional extensions to mention in viva)
- Swap in a larger real-world dataset — e.g. the **SMS Spam Collection**
  dataset from Kaggle/UCI (5,500+ messages) — for much higher accuracy.
  Just replace `data/spam.csv` with the same two columns (`label`, `message`).
- Try other models: Logistic Regression, SVM, or a simple LSTM.
- Add a REST API endpoint (`/predict`) returning JSON, so it can be called
  from a mobile app or another service.
- Deploy it: Render/Railway/PythonAnywhere all support Flask apps directly.
- Add a confusion-matrix / accuracy chart to the UI using matplotlib.

## Notes
- The included `data/spam.csv` has ~70 sample messages so the project runs
  instantly end-to-end. For a stronger reported accuracy, replace it with a
  larger dataset (same 2-column format) before your final submission.
