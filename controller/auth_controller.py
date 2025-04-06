from fastapi import APIRouter, Depends
from fastapi import APIRouter, Form
from fastapi.security import OAuth2PasswordRequestForm
from service.auth_service import authenticate_user

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await authenticate_user(form_data)
