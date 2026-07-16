from fastapi import FastAPI
from pydantic import BaseModel

#create FastAPI Application
app= FastAPI(title= "FastAPI Basics Demo")

#GET Endpoint
@app.get("/greet")
def home():
    return {"message" : "Welcome to FastAPI"}

class User(BaseModel):
    name : str
    age :int

#POST Endpoint
@app.post("/user")
def create_user(user : User):
    return{
        "status" : "success",
        "message" : f"User {user.name} created",
        "age" : user.age
    }

#mock ML Prediction Endpoint

class PredictionInput(BaseModel):
    age : int
    bmi : float
    glucose : float

@app.post("/predict")
def predict(input_data : PredictionInput):
    if input_data.glucose > 140 or input_data.bmi > 35:
        prediction = "highRisk"
    else:
        prediction = "lowRisk"

    return {
        "prediction" : prediction,
        "model" : "mock-diabetes-model",
        "input" : input_data
    }