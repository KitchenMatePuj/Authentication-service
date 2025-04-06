from fastapi import APIRouter, Body
from service.password_service import reset_password_service

router = APIRouter()

@router.post("/reset-password")
def reset_password(payload: dict = Body(...)):
    email = payload.get("email")
    if not email:
        return {"error": "El campo 'email' es obligatorio."}
    return reset_password_service(email)
