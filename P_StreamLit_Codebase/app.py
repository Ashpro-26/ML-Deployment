import os
import requests
from dotenv import load_dotenv
import streamlit as st

from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent / ".env"

print(env_path)
print(env_path.exists())

load_dotenv(env_path)

print(os.getenv("API_URL"))

# load .env values to env vars
load_dotenv()

API_URL = os.getenv("API_URL")

print(API_URL)

#set Page Configurations
st.set_page_config(
    page_title = "Diabetes Prediction App",
    page_icon = "🩺",
    layout = "centered"
)

st.title("🩺 Diabetes Prediction App")
st.write("Enter Patient Details and click **Predict**")

st.subheader("Patient Details")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 10, 2)
    glucose = st.number_input("Glucose", 0, 400, 120)
    bloodPressure = st.number_input("Blood Pressure", 0, 200, 70)
    skinThickness = st.number_input("Skin Thickness", 0, 100, 25)

with col2:
    insulin = st.number_input("Insulin", 0, 900, 80)
    bmi = st.number_input("BMI", 0.0, 70.0, 28.5)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.45)
    age = st.number_input("Age", 1, 100, 35)

if st.button("🔍Predict"):
    input_data = {
    "Pregnancies" : pregnancies,
    "Glucose" : glucose,
    "BloodPressure" : bloodPressure,
    "SkinThickness" : skinThickness,
    "Insulin" : insulin,
    "BMI" : bmi,
    "DiabetesPedigreeFunction" : dpf,
    "Age" : age
    }

    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        response_dictionary = response.json()
        print(response_dictionary)
        prediction = response_dictionary.get("Prediction")

        if prediction == 1:
            st.success("Diabetes Detected")
        else:
            st.success("No Diabetes Detected")
    else:
        st.error(f"API Error: {response.status_code}")
        st.write(response.text)