from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models.crop_request import CropRequest

router = APIRouter(prefix="/analysis", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📊 1. إحصائيات عامة
@router.get("/")
def get_analytics(db: Session = Depends(get_db)):

    total_requests = db.query(CropRequest).count()

    avg_temp = db.query(func.avg(CropRequest.temperature)).scalar() or 0
    avg_humidity = db.query(func.avg(CropRequest.humidity)).scalar() or 0

    return {
        "status": "success",
        "data": {
            "total_requests": total_requests,
            "average_temperature": round(avg_temp, 2),
            "average_humidity": round(avg_humidity, 2)
        }
    }


# 🌍 2. أكتر مدينة مستخدمة
@router.get("/top-city")
def top_city(db: Session = Depends(get_db)):

    result = (
        db.query(
            CropRequest.city,
            func.count(CropRequest.city).label("count")
        )
        .group_by(CropRequest.city)
        .order_by(func.count(CropRequest.city).desc())
        .first()
    )

    if not result:
        return {"message": "No data yet"}

    return {
        "status": "success",
        "data": {
            "city": result.city,
            "count": result.count
        }
    }


# 🌱 3. أكتر محصول متكرر
@router.get("/top-crop")
def top_crop(db: Session = Depends(get_db)):

    # ⚠ لازم يكون عندك column اسمه recommended_crop
    result = (
        db.query(
            CropRequest.recommended_crop,
            func.count(CropRequest.recommended_crop).label("count")
        )
        .group_by(CropRequest.recommended_crop)
        .order_by(func.count(CropRequest.recommended_crop).desc())
        .first()
    )

    if not result:
        return {"message": "No data yet"}

    return {
        "status": "success",
        "data": {
            "crop": result.recommended_crop,
            "count": result.count
        }
    }