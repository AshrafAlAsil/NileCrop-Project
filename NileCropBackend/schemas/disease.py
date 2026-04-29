from pydantic import BaseModel, Field

class DiseaseRequestSchema(BaseModel):
    image_url: str
    prediction: str = Field(..., min_length=3)
    confidence: float = Field(..., ge=0, le=1)