import io
import json
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="NileCrop Disease Detection API", version="1.0")

try:
    model = tf.keras.models.load_model('disease_model.h5')
    with open('disease_classes.json', 'r', encoding='utf-8') as f:
        class_names = json.load(f)
    with open('disease_info_arabic.json', 'r', encoding='utf-8') as f:
        disease_info_ar = json.load(f)
except Exception as e:
    print(f"Error loading model artifacts: {e}")

def prepare_image(image_bytes: bytes) -> np.ndarray:
    """Decodes, resizes, and normalizes the uploaded image for MobileNetV2."""
    img = Image.open(io.BytesIO(image_bytes))
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict-disease")
async def predict_disease(file: UploadFile = File(...)):
    """
    Receives an image file, predicts the disease, 
    and returns Arabic details (name, description, treatment).
    """
    image_bytes = await file.read()
    processed_image = prepare_image(image_bytes)
    
    predictions = model.predict(processed_image)
    predicted_index = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]))
    
    class_name_en = class_names.get(str(predicted_index), "Unknown")
    arabic_details = disease_info_ar.get(class_name_en, {})
    
    return {
        "status": "success",
        "filename": file.filename,
        "confidence": round(confidence * 100, 2),
        "class_name_en": class_name_en,
        "arabic_details": arabic_details
    }

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "Disease Detection API"}