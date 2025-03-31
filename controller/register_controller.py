from fastapi import APIRouter
from service.register_service import register_user_service, RegisterRequest

router = APIRouter()

@router.post("/register")
async def register_user(user: RegisterRequest):
    return await register_user_service(user)
