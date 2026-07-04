# Import required libraries

import os

import numpy as np
import pandas as pd
import pickle

from flask import Flask, render_template, request

# Create Flask application

app = Flask(__name__)

# Load the trained model and scaler

model = pickle.load(open("rdf.pkl", "rb"))
scaler = pickle.load(open("scale1.pkl", "rb"))

# Home page

@app.route("/")
def home():
    return render_template("home.html")

# Prediction page

@app.route("/predict")
def predict():
    return render_template("predict.html")

# Prediction logic

@app.route("/submit", methods=["POST"])
def submit():

    gender = int(request.form["Gender"])
    married = int(request.form["Married"])
    dependents = int(request.form["Dependents"])
    education = int(request.form["Education"])
    self_employed = int(request.form["Self_Employed"])
    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_amount_term = float(request.form["Loan_Amount_Term"])
    credit_history = float(request.form["Credit_History"])
    property_area = int(request.form["Property_Area"])

    input_data = [[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]]

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Loan Will be Approved"
    else:
        result = "Loan Will Not be Approved"

    return render_template("submit.html", result=result)

# Run the application  
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)