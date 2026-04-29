from sqlalchemy import Column, Integer, String
from database import Base

class DiseaseInfo(Base):
    __tablename__ = "disease_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    treatment = Column(String)