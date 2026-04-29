from os import name

from database import SessionLocal
from models import City

def seed_data():
    db = SessionLocal()
    print("📡 جاري بدء عملية إدخال البيانات...")
    
    # قائمة بـ 60 مدينة ومنطقة زراعية في مصر
    cities_data = [
        # القاهرة والدلتا (مركز الثقل الزراعي القديم)
        {"name": "Cairo", "latitude": 30.0444, "longitude": 31.2357},
        {"name": "Giza", "latitude": 30.0131, "longitude": 31.2089},
        {"name": "Banha", "latitude": 30.4591, "longitude": 31.1786},
        {"name": "Shibin El Kom", "latitude": 30.5503, "longitude": 31.0106},
        {"name": "Tanta", "latitude": 30.7865, "longitude": 31.0004},
        {"name": "Damanhur", "latitude": 31.0364, "longitude": 30.4694},
        {"name": "Mansoura", "latitude": 31.0409, "longitude": 31.3785},
        {"name": "Zagazig", "latitude": 30.5877, "longitude": 31.5020},
        {"name": "Damietta", "latitude": 31.4175, "longitude": 31.8144},
        {"name": "Kafr El Sheikh", "latitude": 31.1042, "longitude": 30.9402},
        {"name": "Desouk", "latitude": 31.1300, "longitude": 30.6400},
        {"name": "Bilbeis", "latitude": 30.4100, "longitude": 31.5600},
        {"name": "Mit Ghamr", "latitude": 30.7100, "longitude": 31.2600},
        {"name": "Abu Kabir", "latitude": 30.7200, "longitude": 31.6700},
        {"name": "Qalyub", "latitude": 30.1800, "longitude": 31.2000},
        {"name": "Kafr El Dawwar", "latitude": 31.1300, "longitude": 30.1200},
        {"name": "Talkha", "latitude": 31.0500, "longitude": 31.3800},
        {"name": "Hihya", "latitude": 30.6700, "longitude": 31.5800},
        {"name": "Senbellawein", "latitude": 30.8800, "longitude": 31.4600},
        {"name": "Zifta", "latitude": 30.7100, "longitude": 31.2300},

        # مدن القناة وسيناء (مناطق التوسع)
        {"name": "Ismailia", "latitude": 30.5965, "longitude": 32.2715},
        {"name": "Port Said", "latitude": 31.2653, "longitude": 32.3019},
        {"name": "Suez", "latitude": 29.9668, "longitude": 32.5498},
        {"name": "Arish", "latitude": 31.1316, "longitude": 33.8032},
        {"name": "El Tor", "latitude": 28.2358, "longitude": 33.6254},
        {"name": "Kantara", "latitude": 30.8500, "longitude": 32.3100},
        {"name": "Ras Sudr", "latitude": 29.5900, "longitude": 32.7100},
        {"name": "Nuweiba", "latitude": 28.9971, "longitude": 34.6534},
        {"name": "Fayid", "latitude": 30.3300, "longitude": 32.3100},
        {"name": "Bir al-Abed", "latitude": 31.0100, "longitude": 33.0100},

        # مصر الوسطى (الفيوم والمنيا وبني سويف)
        {"name": "Fayoum", "latitude": 29.3084, "longitude": 30.8428},
        {"name": "Beni Suef", "latitude": 29.0744, "longitude": 31.0979},
        {"name": "Minya", "latitude": 28.0991, "longitude": 30.7503},
        {"name": "Mallawi", "latitude": 27.7300, "longitude": 30.8400},
        {"name": "Maghagha", "latitude": 28.6500, "longitude": 30.8400},
        {"name": "Samalut", "latitude": 28.3100, "longitude": 30.7100},
        {"name": "Wasta", "latitude": 29.3400, "longitude": 31.2100},
        {"name": "Itsa", "latitude": 29.2300, "longitude": 30.7800},
        {"name": "Biba", "latitude": 28.9200, "longitude": 30.9700},
        {"name": "Abu Qurqas", "latitude": 27.9300, "longitude": 30.8400},

        # الصعيد ومصر العليا
        {"name": "Asyut", "latitude": 27.1783, "longitude": 31.1859},
        {"name": "Sohag", "latitude": 26.5570, "longitude": 31.6948},
        {"name": "Qena", "latitude": 26.1551, "longitude": 32.7160},
        {"name": "Luxor", "latitude": 25.6872, "longitude": 32.6396},
        {"name": "Aswan", "latitude": 24.0889, "longitude": 32.8998},
        {"name": "Idfu", "latitude": 24.9781, "longitude": 32.8794},
        {"name": "Kom Ombo", "latitude": 24.4700, "longitude": 32.9400},
        {"name": "Esna", "latitude": 25.2900, "longitude": 32.5500},{"name": "Nag Hammadi", "latitude": 26.0500, "longitude": 32.2400},
        {"name": "Tahta", "latitude": 26.7600, "longitude": 31.5000},
        {"name": "Girga", "latitude": 26.3300, "longitude": 31.8900},
        {"name": "Manfalut", "latitude": 27.3100, "longitude": 30.9700},

        # الوادي الجديد والمناطق المستصلحة (أهمية كبرى للمشروع)
        {"name": "Kharga", "latitude": 25.4400, "longitude": 30.5500},
        {"name": "Dakhla", "latitude": 25.5100, "longitude": 28.9800},
        {"name": "Farafra", "latitude": 27.0600, "longitude": 27.9700},
        {"name": "Siwa", "latitude": 29.2000, "longitude": 25.5200},
        {"name": "Wadi Natrun", "latitude": 30.4100, "longitude": 30.3700},
        {"name": "Sadat City", "latitude": 30.3800, "longitude": 30.5200},
        {"name": "Nubariyah", "latitude": 30.6600, "longitude": 30.0600},
        {"name": "Toshka", "latitude": 22.5100, "longitude": 31.5100},
    ]

    

    try:
        count = 0
        for city_info in cities_data:
            exists = db.query(City).filter(City.name == city_info["name"]).first()
            if not exists:
                db_city = City(**city_info)
                db.add(db_city)
                count += 1
        
        db.commit()
        # هذه هي الجملة التي تقصدينها، يمكنك تخصيصها كما تحبين
        print("---------------------------------------")
        print(f"✅ Done! {count} cities added successfully.")
        print("---------------------------------------")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error occurred: {e}")
    finally:
        db.close()
if __name__ == "__main__":
    seed_data()

        