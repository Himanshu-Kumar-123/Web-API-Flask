from flask import Flask
import pickle

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

#API Endpoint
@app.route("/")
def home():
    return "<h1>Loan Approval Application</h1>"

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return "I will predict the loan approval status for you"
    else:
        # Post request along with the input data to predict the loan approval status
        return model.predict(inputs)