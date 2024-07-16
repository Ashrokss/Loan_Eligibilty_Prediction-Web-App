# Loan Eligibility Prediction Web App

This repository contains a web application for predicting loan eligibility using a logistic regression model. The application is built with Streamlit and provides an interactive interface for users to input their details and get predictions on their loan eligibility.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)

## Introduction

Loan eligibility prediction is a common task in the financial sector. This web application allows users to input various details required for assessing loan eligibility and provides a prediction based on a pre-trained logistic regression model. The goal is to assist financial institutions in making informed decisions quickly and accurately.

## Features

- User-friendly web interface built with Streamlit.
- Real-time loan eligibility predictions.
- Input fields for relevant loan application details.
- Displays prediction results immediately after submission.

## Usage

You can access the live application using the following link:

[Loan Eligibility Prediction Web App](https://loaneligibiltyprediction-web-app-gw723an5hcgxwqyuac9ppi.streamlit.app/)

1. Open the link in your web browser.
2. Enter the required details in the input fields.
3. Click on the "Predict" button to see the prediction result.
4. The application will display whether the applicant is eligible for the loan or not based on the input data.

## Model

The logistic regression model used in this application is Random Forest Classifier which is  trained on a dataset containing various features related to loan applications. The model is designed to predict the likelihood of loan approval based on these features. You can find the model training script and dataset in the `model` directory.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request. Please ensure that your contributions align with the project's goals and follow the existing coding style.
