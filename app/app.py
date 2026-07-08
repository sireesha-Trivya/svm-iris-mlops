from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("model/svm_model.joblib")

app = FastAPI(
    title="Iris SVM Prediction API",
    version="1.0.0",
    description="Machine Learning API using Support Vector Machine"
)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

classes = [
    "Setosa",
    "Versicolor",
    "Virginica"
]

@app.get("/")
def home():
    return {
        "status": "Running",
        "model": "Support Vector Machine",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

@app.post("/predict")
def predict(data: IrisInput):

    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    return {
        "class_id": int(prediction[0]),
        "prediction": classes[prediction[0]]
    }
