from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models.crop_request import CropRequest
from models.disease_request import DiseaseRequest

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_analytics(db: Session = Depends(get_db)):

    # إجمالي الطلبات
    total_crop_requests = db.query(CropRequest).count()
    total_disease_requests = db.query(DiseaseRequest).count()

    # أكتر محصول تم التوصية به
    top_crop = (
        db.query(
            CropRequest.recommended_crop,
            func.count(CropRequest.recommended_crop).label("count")
        )
        .group_by(CropRequest.recommended_crop)
        .order_by(func.count().desc())
        .first()
    )

    # أكتر مرض تم اكتشافه
    top_disease = (
        db.query(
            DiseaseRequest.prediction,
            func.count(DiseaseRequest.prediction).label("count")
        )
        .group_by(DiseaseRequest.prediction)
        .order_by(func.count().desc())
        .first()
    )

    return {
        "total_crop_requests": total_crop_requests,
        "total_disease_requests": total_disease_requests,
        "most_recommended_crop": top_crop[0] if top_crop else None,
        "most_detected_disease": top_disease[0] if top_disease else None,
    }
    