import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NileCrop Recommendation API", version="1.0")

try:
    model = joblib.load('crop_model.pkl')
    scaler = joblib.load('scaler.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
except Exception as e:
    print(f"Error loading model artifacts: {e}")

class PredictionInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.post("/predict")
def predict_crop(data: PredictionInput):
    """
    Predicts the optimal crop based on soil and weather parameters.
    """
    features = [[
        data.N, data.P, data.K, 
        data.temperature, data.humidity, 
        data.ph, data.rainfall
    ]]
    
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    crop_name = label_encoder.inverse_transform(prediction)[0]
    
    return {
        "recommended_crop": crop_name,
        "status": "success"
    }

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "Crop Recommendation API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)