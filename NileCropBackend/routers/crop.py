from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.crop_request import CropRequest
from schemas.crop import CropRequestSchema

from services.geocoding import get_coordinates
from services.weather import get_weather
from services.soil_service import get_soil
from services.crop_logic import recommend_crop


router = APIRouter(prefix="/crop", tags=["Crop"])


# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/crop-request")
def create_crop_request(
    data: CropRequestSchema,
    db: Session = Depends(get_db)
):
    
    # 1) تحويل اسم المدينة لإحداثيات
    lat, lon = get_coordinates(data.city)

    if lat is None:
        raise HTTPException(status_code=404, detail="City not found")

    # 2) جلب بيانات الطقس
    weather = get_weather(lat, lon)

    # 3) جلب بيانات التربة
    soil = get_soil(lat, lon)
    print("Weather Data:", weather)

    # 4) استدعاء الموديل بالقيم الصحيحة
    recommended = recommend_crop(
        weather["temperature"],
        weather["humidity"],
        weather.get("rainfall", 0.0),
        soil["nitrogen"],
        soil["phosphorus"],
        soil["potassium"],
        soil["ph"]
    )

    # 5) حفظ الطلب في قاعدة البيانات
    crop = CropRequest(
        city=data.city,
        latitude=lat,
        longitude=lon,
        temperature=weather["temperature"],
        humidity=weather["humidity"],
        soil_type="NPK+pH",
        recommended_crop=recommended
    )

    db.add(crop)
    db.commit()
    db.refresh(crop)

    # 6) إرجاع النتيجة للفرونت
    return {
        "status": "success",
        "city": data.city,
        "recommended_crop": recommended,
        "details": {
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "nitrogen": soil["nitrogen"],
            "phosphorus": soil["phosphorus"],
            "potassium": soil["potassium"],
            "ph": soil["ph"]
        }
    }
