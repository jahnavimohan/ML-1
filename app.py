
import streamlit as st
import joblib

# Load the saved model
model = joblib.load("model.pkl")

st.title("🧠 Disease Prediction App")

# Replace these with your actual model input names
age = st.number_input("Enter Age")
symptom1 = st.number_input("Enter Symptom Level 1")
symptom2 = st.number_input("Enter Symptom Level 2")

# Predict button
if st.button("Predict"):
    prediction = model.predict([[age, symptom1, symptom2]])
    st.success(f"Predicted Disease: {prediction[0]}")
