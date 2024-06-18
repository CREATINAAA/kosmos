from fastapi import APIRouter
from .views import logic
from ..db.schemas import SkorozvonAdd


router = APIRouter()

@router.post("/webhook")
def webhook_handler(request: SkorozvonAdd):
    return logic(request)
