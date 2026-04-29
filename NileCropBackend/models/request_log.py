from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime 
from database import Base

class RequestLog(Base):
    __tablename__ = "request_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    request_type = Column(String)
    endpoint = Column(String) 
    method = Column(String)
    input_data = Column(Text)
    result = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)