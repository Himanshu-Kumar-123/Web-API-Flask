from flask import Flask, request
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
        loan_req = request.get_json()
        
        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1
        
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History= loan_req['Credit_History']           

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])
        
        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"loan_approval_status":pred}