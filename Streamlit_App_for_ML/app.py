import streamlit as st
from predictor import predict

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

    prediction = predict(input_data= input_data)

    st.divider()

    if prediction == 1:
        st.error("The patient has diabetes.**(+ve)**")
    else:
        st.success("The patient does not have diabetes.**(-ve)**")