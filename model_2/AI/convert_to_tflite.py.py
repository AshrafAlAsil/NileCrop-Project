import tensorflow as tf
import logging
from pathlib import Path

# إعداد الـ Logging لإظهار مخرجات احترافية في التيرمينال
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def convert_h5_to_tflite(h5_model_path: str, tflite_output_path: str) -> None:
    """
    Converts a Keras H5 model to a compressed TFLite version.
    
    Args:
        h5_model_path (str): Path to the source .h5 model file.
        tflite_output_path (str): Path where the .tflite file will be saved.
    """
    try:
        if not Path(h5_model_path).exists():
            raise FileNotFoundError(f"Model file not found at: {h5_model_path}")

        logging.info(f"Loading Keras model from {h5_model_path}...")
        model = tf.keras.models.load_model(h5_model_path)

        logging.info("Starting TFLite conversion with optimization...")
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        
        # تفعيل الـ Optimization لتقليل الحجم دون فقدان ملحوظ في الدقة
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        
        tflite_model = converter.convert()

        logging.info(f"Saving TFLite model to {tflite_output_path}...")
        with open(tflite_output_path, 'wb') as f:
            f.write(tflite_model)
            
        logging.info("✅ Conversion successful!")

    except Exception as e:
        logging.error(f"❌ An error occurred during conversion: {e}")

if __name__ == "__main__":
    # مسارات الملفات
    H5_PATH = 'disease_model.h5'
    TFLITE_PATH = 'disease_model.tflite'
    
    convert_h5_to_tflite(H5_PATH, TFLITE_PATH)