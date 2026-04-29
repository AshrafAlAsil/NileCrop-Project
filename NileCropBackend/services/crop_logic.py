import os
import joblib
import numpy as np

# تحديد المسارات بناءً على هيكل مشروعك
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml-models", "crop_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "ml-models", "label_encoder.pkl")

def recommend_crop(n, p, k, temperature, humidity, ph, rainfall):
    try:
        model = joblib.load(MODEL_PATH)
        encoder = joblib.load(ENCODER_PATH) # تحميل الأنكودر
        
        features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        prediction_numeric = model.predict(features)
        
        # تحويل الرقم (0) لاسم المحصول (مثلاً Rice)
        crop_name = encoder.inverse_transform(prediction_numeric)
        return str(crop_name[0])
    except Exception as e:
        return f"Error: {str(e)}"