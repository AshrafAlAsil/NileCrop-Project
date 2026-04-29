from database import SessionLocal
from models.request_log import RequestLog
import json

def log_request(request_type: str, input_data, result: str):
    db = SessionLocal()

    log = RequestLog(
        request_type=request_type,
        input_data=json.dumps(input_data),
        result=result
    )

    db.add(log)
    db.commit()
    db.close()