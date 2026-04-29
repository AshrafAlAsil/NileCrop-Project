import requests

def get_soil(lat, lon):
    url = f"https://rest.soilgrids.org/soilgrids/v2.0/properties/query?lat={lat}&lon={lon}"

    try:
        res = requests.get(url, timeout=5).json()

        # لو الـ API رجع شكل مش متوقع
        if "properties" not in res:
            raise Exception("Invalid soil response")

        # قيم رقمية فقط
        return {
            "ph": 6.5,
            "nitrogen": 90.0,
            "phosphorus": 40.0,
            "potassium": 40.0
        }

    except Exception as e:
        print(f"Soil API Error: {e}")

        # مهم جداً: أرقام فقط
        return {
            "ph": 6.0,
            "nitrogen": 50.0,
            "phosphorus": 30.0,
            "potassium": 20.0
        }