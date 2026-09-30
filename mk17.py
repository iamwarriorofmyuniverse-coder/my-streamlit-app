import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_annual_marks_model.pkl")

st.set_page_config(page_title="Annual Marks Predictor", page_icon="🎓")
st.title("🎓 Annual Exam Marks Predictor")
st.write(
    "Predict annual exam marks based on Quarterly marks, "
    "Half-Yearly marks, and Extra Classes hours."
)

# User inputs
subject = st.selectbox(
    "Subject",
    ["Math", "Science", "English", "Social", "Computer"]
)

quarterly = st.number_input(
    "Quarterly Marks",
    min_value=0,
    max_value=100,
    value=50
)
half_yearly = st.number_input(
    "Half Yearly Marks",
    min_value=0,
    max_value=100,
    value=50
)

extra_classes = st.number_input(
    "Extra Classes Hours",
    min_value=0,
    max_value=50,
    value=10
)

# Prediction
if st.button("Predict Annual Marks"):
    input_df = pd.DataFrame([{
        "Subject": subject,
        "Quarterly": quarterly,
        "Half_Yearly": half_yearly,
        "Extra_Classes": extra_classes
    }])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Annual Marks: {prediction:.2f}")
    