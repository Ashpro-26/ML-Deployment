import requests
API_URL = "http://127.0.0.1:8000/predict_diabetes"

payload = {
    "Pregnancies": 2,
    "Glucose": 140,
    "BloodPressure": 120,
    "SkinThickness": 15,
    "Insulin": 80,
    "BMI": 20,
    "DiabetesPedigreeFunction": 0.355,
    "Age": 28
}

#Send POST Request to the API
response = requests.post(API_URL, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())