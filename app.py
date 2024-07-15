import streamlit as st
from joblib import load
import pandas as pd
import numpy as np

# Load the trained model
model_path = 'trained_model.joblib'
loaded_model = load(model_path)

# Define the prediction function
def predict_loan_eligibility(features):
    prediction = loaded_model.predict([features])
    return prediction[0]

# Streamlit app layout
st.title("Loan Eligibility Prediction")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term")
credit_history = st.selectbox("Credit History", ["0", "1"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Button to predict
if st.button("Predict"):
    features = [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        int(dependents.replace('3+', '3')),
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        int(credit_history),
        1 if property_area == "Urban" else 2 if property_area == "Semiurban" else 0
    ]
    prediction = predict_loan_eligibility(features)
    if prediction == 1:
        st.success("Congratulations! You are eligible for the loan.")
    else:
        st.error("Sorry, you are not eligible for the loan.")
