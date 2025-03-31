from fastapi import APIRouter
from service.password_service import reset_password_service

router = APIRouter()

@router.post("/reset-password/{user_id}")
def reset_password(user_id: str):
    return reset_password_service(user_id)
