from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class DiseaseRequest(Base):
    __tablename__ = "disease_requests"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    prediction = Column(String, index=True)  # ⭐ اسم المرض
    confidence = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow, index=True)  # ⭐