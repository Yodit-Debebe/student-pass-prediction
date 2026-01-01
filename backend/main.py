from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os

# --------------------------------------------------
# Load trained models
# --------------------------------------------------

logistic_model = joblib.load("models/logistic_model.pkl")
decision_tree_model = joblib.load("models/decision_tree_model.pkl")

# --------------------------------------------------
# Initialize FastAPI app
# --------------------------------------------------

app = FastAPI(
    title="Student Pass/Fail Prediction API",
    description="Predict student performance using Logistic Regression and Decision Tree",
    version="1.0"
)

# --------------------------------------------------
# Enable CORS (for frontend connection)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend from anywhere
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Input Data Schema
# --------------------------------------------------

class StudentData(BaseModel):
    school: str
    sex: str
    age: int
    address: str
    famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    traveltime: int
    studytime: int
    failures: int
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int

# --------------------------------------------------
# Prediction Helper Function
# --------------------------------------------------

def predict(model, data: StudentData):
    df = pd.DataFrame([data.dict()])
    result = model.predict(df)[0]
    return "Pass" if result == 1 else "Fail"

# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "Student Pass/Fail Prediction API is running"}

@app.post("/predict/logistic")
def predict_logistic(data: StudentData):
    return {
        "model": "Logistic Regression",
        "prediction": predict(logistic_model, data)
    }

@app.post("/predict/tree")
def predict_tree(data: StudentData):
    return {
        "model": "Decision Tree",
        "prediction": predict(decision_tree_model, data)
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
