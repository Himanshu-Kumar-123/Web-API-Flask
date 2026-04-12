from loan_app import app
import pytest

# Proxy to a live server
@pytest.fixture
def client():
    return app.test_client()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "<h1>Loan Approval Application</h1>"

def test_predict_page(client):
    test_data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 400,
        "Credit_History": 1
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Approved"}

def test_predict_page_negative(client):
    test_data = {
        "Gender": "Female",
        "Married": "Yes",
        "ApplicantIncome": 5000,
        "LoanAmount": 10000,
        "Credit_History": 0
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Rejected"}
