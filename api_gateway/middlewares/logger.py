import logging
from datetime import datetime
from flask import request

logger = logging.getLogger("library_management_system")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

def log_middleware(response):
    request_data = request.get_json(silent=True)

    log_data = {
        "time": datetime.now().isoformat(),
        "method": request.method,
        "path": request.path,
        "request_data": request_data,
        "status_code": response.status_code,
        "response": response.get_json()
    }

    logger.info(log_data)
    return response