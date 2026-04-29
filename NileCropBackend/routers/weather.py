from fastapi import APIRouter, HTTPException, Query
from services.weather import get_weather

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/weather-test")
def weather_test(
    lat: float = Query(...),
    lon: float = Query(...)
):
    try:
        data = get_weather(lat, lon)

        if not data:
            raise HTTPException(status_code=404, detail="Weather data not found")

        return data

    except Exception:
        raise HTTPException(status_code=500, detail="Weather service failed")