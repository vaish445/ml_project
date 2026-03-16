from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI(title="Diabetes Prediction API")

# load trained model
model = None

try:
    model = joblib.load("models/model.pkl")
except:
    model = None


@app.get("/")
def home():
    return {"message": "Diabetes Prediction API Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(
        pregnancies: int,
        glucose: float,
        blood_pressure: float,
        skin_thickness: float,
        insulin: float,
        bmi: float,
        diabetes_pedigree_function: float,
        age: int
):
    
    if model is None:
        return {"error": "Model not loaded"}

    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                          insulin, bmi, diabetes_pedigree_function, age]])

    prediction = model.predict(features)[0]

    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    return {
        "prediction": int(prediction),
        "result": result
    }
