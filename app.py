import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/extra_trees_credit_model.pkl")

st.set_page_config(page_title="Credit Risk Prediction")

st.title("💳 Credit Risk Prediction System")

st.write("Enter applicant details below:")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

sex = st.selectbox(
    "Sex",
    ["female", "male"]
)

job = st.selectbox(
    "Job",
    [0, 1, 2, 3]
)

housing = st.selectbox(
    "Housing",
    ["own", "free", "rent"]
)

saving = st.selectbox(
    "Saving Accounts",
    ["little", "moderate", "quite rich", "rich"]
)

checking = st.selectbox(
    "Checking Account",
    ["moderate", "little", "rich"]
)

credit_amount = st.number_input(
    "Credit Amount",
    min_value=0,
    value=1000
)

duration = st.number_input(
    "Duration (Months)",
    min_value=1,
    value=12
)

# Manual encoding
sex_map = {
    "female": 0,
    "male": 1
}

housing_map = {
    "free": 0,
    "own": 1,
    "rent": 2
}

saving_map = {
    "little": 0,
    "moderate": 1,
    "quite rich": 2,
    "rich": 3
}

checking_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2
}

if st.button("Predict Risk"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_map[sex]],
        "Job": [job],
        "Housing": [housing_map[housing]],
        "Saving accounts": [saving_map[saving]],
        "Checking account": [checking_map[checking]],
        "Credit amount": [credit_amount],
        "Duration": [duration]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ GOOD Credit Risk")
    else:
        st.error("❌ BAD Credit Risk")