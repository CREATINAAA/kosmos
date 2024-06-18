from datetime import datetime
import json
import logging
from ..db.schemas import SkorozvonAdd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent / 'logs'

BASE_DIR.mkdir(parents=True, exist_ok=True)

request_logger = logging.getLogger('request')
request_logger.setLevel(logging.INFO)
request_handler = logging.FileHandler(BASE_DIR / "WebhookData.log")
request_handler.setLevel(logging.INFO)
request_logger.addHandler(request_handler)

response_logger = logging.getLogger('response')
response_logger.setLevel(logging.INFO)
response_handler = logging.FileHandler(BASE_DIR / "ResponseData.log")
response_handler.setLevel(logging.INFO)
response_logger.addHandler(response_handler)


def log_request(request_data: dict, validated_deal: SkorozvonAdd):
    request_logger.info(
        f"request time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        f"request data: {json.dumps(request_data)}\n"
        f"deal: {validated_deal}\n"
    )


def log_response(response_status: str, response_text: str):
    response_logger.info(
        f"response status: {response_status}\n"
        f"response time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        f"response text: {response_text}\n"
    )
