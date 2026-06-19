# Credit Risk Prediction System

## Overview
This project predicts whether a loan applicant is a Good Credit Risk or Bad Credit Risk using Machine Learning.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

## Machine Learning Model
- Extra Trees Classifier

## Features
- User-friendly Streamlit interface
- Real-time credit risk prediction
- Trained on German Credit Dataset

## Run Locally

```bash
py -m streamlit run app.py
```

## Project Structure

```text
credit_risk_model/
│
├── models/
│   └── extra_trees_credit_model.pkl
│
├── notebook/
│   └── analysis_model.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```