import os

import requests


def get_weather(lat: float, lon: float):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # تأكد إن المفتاح مش فاضي
    if not api_key:
        print("Error: API Key is missing! Check your .env file.")
        # حط مفتاحك هنا مؤقتاً للتجربة لو الـ .env مش شغال
        # api_key = "your_actual_api_key_here" 

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    )
    
    response = requests.get(url)
    res = response.json()
    
    # اطبع الرد عشان لو في مشكلة تظهر لك في الـ Terminal
    print("API Response:", res)
    
    if response.status_code != 200:
        return {"temperature": 0, "humidity": 0}

    return {
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"]
    }
    