from fastapi import APIRouter, Depends, Request, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import shutil
import os

# --- إضافة مكتبات الـ Limiter ---
from slowapi import Limiter # type: ignore
from slowapi.util import get_remote_address # type: ignore

from models.disease_info import DiseaseInfo
from models.disease_request import DiseaseRequest
from schemas.disease import DiseaseRequestSchema
from routers.city import get_db
from services.logger import log_request

# --- تعريف الـ Limiter هنا مباشرة بدل الملف الخارجي ---
limiter = Limiter(key_func=get_remote_address)

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================
# Upload Image Endpoint
# =========================
@router.post("/image")
@limiter.limit("10/minute") # كدة هيشتغل بدون مشاكل
def upload_image(
    request: Request,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.lower().endswith((".jpg", ".png", ".jpeg")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    safe_filename = file.filename.replace(" ", "_")
    file_path = os.path.join(UPLOAD_FOLDER, safe_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = "Septoria Leaf Spot"
    confidence = 0.92

    new_request = DiseaseRequest(
        image_url=safe_filename,
        prediction=prediction,
        confidence=confidence
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    log_request(
        request_type="upload_image",
        input_data={"filename": safe_filename},
        result=prediction
    )

    disease = (
        db.query(DiseaseInfo)
        .filter(DiseaseInfo.name == prediction)
        .first()
    )

    response = {
        "filename": safe_filename,
        "prediction": prediction,
        "confidence": confidence
    }

    if disease:
        response.update({
            "description": disease.description,
            "treatment": disease.treatment
        })
    else:
        response["message"] = "No disease info found"

    return response


# =========================
# Create Disease Request (NEW)
# =========================
@router.post("/disease-request")
def create_disease_request(
    data: DiseaseRequestSchema,
    db: Session = Depends(get_db)
):
    # استخدام model_dump لنسخ البيانات
    new_request = DiseaseRequest(**data.model_dump()) 

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


# =========================
# Get All Requests
# =========================
@router.get("/disease-requests")
def get_all_requests(db: Session = Depends(get_db)):
    return db.query(DiseaseRequest).all()