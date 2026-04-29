from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.city import City

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cities/search")
def search_city(name: str, db: Session = Depends(get_db)):

    # ✅ Validation هنا
    if not name:
        raise HTTPException(status_code=400, detail="City name is required")

    cities = db.query(City).filter(
        City.name.ilike(f"%{name}%")
    ).all()

    return cities
