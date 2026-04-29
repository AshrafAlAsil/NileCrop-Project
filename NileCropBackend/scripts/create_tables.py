from database import engine, Base
from models import City, CropRequest, DiseaseRequest, DiseaseInfo, RequestLog

Base.metadata.create_all(bind=engine)
print("Tables created successfully")