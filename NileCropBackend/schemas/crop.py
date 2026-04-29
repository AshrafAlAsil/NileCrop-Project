from pydantic import BaseModel

class CropRequestSchema(BaseModel):
    city: str
    n: float # النيتروجين
    p: float # الفوسفور
    k: float # البوتاسيوم
    ph: float # حموضة التربة