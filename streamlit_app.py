import streamlit as st
import pickle
import os

# Page settings
st.set_page_config(
    page_title="SpamShield",
    page_icon="📩",
    layout="centered"
)

# Model paths
MODEL_PATH = os.path.join("model", "spam_model.pkl")
VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)


# Title
st.title("📩 SpamShield")
st.subheader("Spam Message Detector")

st.write(
    "Enter a message below to check whether it is "
    "Spam or Not Spam."
)

# Message input
message = st.text_area(
    "Enter your message:",
    height=150,
    placeholder="Type or paste your message here..."
)

# Analyze
if st.button("🔍 Analyze Message", use_container_width=True):

    if not message.strip():
        st.warning("⚠️ Please enter a message first.")

    else:
        # TF-IDF transformation
        message_vector = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_vector)[0]

        # Confidence
        probabilities = model.predict_proba(message_vector)[0]
        confidence = max(probabilities) * 100

        # Result
        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")
        else:
            st.success("✅ NOT SPAM")

        st.write(f"Confidence: **{confidence:.2f}%**")


# Examples
st.divider()

st.subheader("Try an example")

if st.button("🎁 Show Spam Example"):
    st.code(
        "Congratulations! You have won a free iPhone. "
        "Click here to claim your prize now!"
    )

if st.button("💬 Show Normal Example"):
    st.code(
        "Hey, are we still meeting for the project discussion tomorrow?"
    )