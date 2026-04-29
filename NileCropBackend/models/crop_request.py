from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class CropRequest(Base):
    __tablename__ = "crop_requests"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    soil_type = Column(String)
    
    # ضيفي السطرين دول هنا ⭐
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    recommended_crop = Column(String, index=True) 
    created_at = Column(DateTime, default=datetime.utcnow, index=True)