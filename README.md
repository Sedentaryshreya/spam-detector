# 🛡️ SpamShield — AI-Powered Spam Message Detector

SpamShield is a Machine Learning-based web application that detects whether a text message is **Spam** or **Not Spam**.

The application uses **TF-IDF (Term Frequency–Inverse Document Frequency)** for text feature extraction and a **Naive Bayes classifier** for prediction. A simple and interactive **Flask web interface** allows users to enter a message and instantly receive a prediction along with the model's confidence score.


## ✨ Features

- 🔍 Detects whether a message is **Spam** or **Not Spam**
- 🧠 Machine Learning-based text classification
- 🔤 TF-IDF feature extraction
- ⚡ Fast prediction
- 📊 Displays prediction confidence
- 🌐 Flask-based web application
- 🎨 Modern and responsive user interface
- 💡 Built-in example messages for testing
- 📱 Responsive design for different screen sizes

---

## 🧠 How It Works

The application follows a simple Machine Learning pipeline:

```text
User Message
     ↓
Text Processing
     ↓
TF-IDF Vectorization
     ↓
Naive Bayes Classifier
     ↓
Prediction
     ↓
Spam / Not Spam
     ↓
Confidence Score1. User Input

The user enters or pastes a message into the web application.

2. TF-IDF Vectorization

The text is converted into numerical features using a trained TF-IDF vectorizer.

3. Machine Learning Prediction

The transformed message is passed to the trained Naive Bayes model.

4. Result

The application returns:

SPAM — if the message is classified as spam
NOT SPAM — if the message is classified as a normal message

The application also displays the prediction confidence percentage.

🛠️ Tech Stack
Programming Language
Python
Machine Learning
Scikit-learn
Naive Bayes
TF-IDF Vectorization
Web Development
Flask
HTML
CSS
JavaScript
Data & Model Handling
Pandas
NumPy
Pickle
📂 Project Structure
spam-detector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── dataset files
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
└── templates/
    └── index.html
⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/spam-detector.git

Move into the project directory:

cd spam-detector
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
Windows Command Prompt
venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Flask application:

python app.py

The application will run locally at:

http://127.0.0.1:5000

Open the address in your web browser.

🧪 Example
Spam Message
Congratulations! You have won a free iPhone.
Click here to claim your prize now!

Expected result:

🚨 SPAM DETECTED
Normal Message
Hey, are we still meeting for lunch today?

Expected result:

✅ NOT SPAM
📊 Prediction Confidence

Along with the classification result, SpamShield displays a confidence score.

For example:

🚨 SPAM DETECTED

Confidence: 96.8%

The confidence represents the model's predicted probability for the selected class.

🧹 Machine Learning Pipeline

The project uses the following NLP/ML workflow:

Raw Message
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Feature Representation
    ↓
Naive Bayes Classification
    ↓
Prediction
TF-IDF

TF-IDF converts text into numerical features by considering how important words are within the messages.

Naive Bayes

Naive Bayes is a probabilistic classification algorithm that works well for many text classification tasks.

🌐 Web Application

The Flask backend connects the trained Machine Learning model with the web interface.

The application:

Accepts a message from the user.
Converts the message using the trained vectorizer.
Sends the transformed data to the trained model.
Generates a prediction.
Calculates the prediction confidence.
Displays the result on the webpage.
🎨 User Interface

The application provides a simple and interactive interface where users can:

Enter a message
Try example messages
Analyze the message
View Spam/Not Spam prediction
View confidence percentage
🔮 Future Improvements

Some possible improvements for future versions include:

📜 Prediction history
📈 Analytics dashboard
📁 Bulk CSV message classification
🔍 Suspicious keyword highlighting
🔗 Suspicious URL detection
🤖 Comparison of multiple ML algorithms
📊 Confusion matrix and model performance dashboard
👤 User authentication
☁️ Cloud deployment
📱 Progressive Web App support
🎯 Learning Outcomes

This project helped in understanding and implementing:

Machine Learning classification
Natural Language Processing
Text preprocessing
TF-IDF vectorization
Naive Bayes classification
Model serialization
Flask web development
Connecting ML models with web applications
Basic frontend development
Git and GitHub project management
📌 Project Status

Current Status: 🚧 Active Development

The basic spam detection system is functional, and additional features and improvements can be added in future versions.

👩‍💻 Author

Your Name

B.Tech — Computer Science & Engineering
⭐ If You Like This Project
If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub!

