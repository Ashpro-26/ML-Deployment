from fastapi import FastAPI
from pydantic import BaseModel

from predictor import predict

app = FastAPI(title= "ML Prediction API")

class PredictionData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int 
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    pass

@app.post("/predict_diabetes")
def predict_diabetes(input_data: PredictionData):
    prediction=predict(input_data.model_dump())
    return {
        "Prediction": int(prediction)
    }