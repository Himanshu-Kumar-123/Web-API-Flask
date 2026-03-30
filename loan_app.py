from flask import Flask
import pickle

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

#API Endpoint
@app.route("/")
def home():
    return "<h1>Loan Approval Application</h1>"

@app.route("/predict")
def predict():
    return "I will predict the loan approval status for you"