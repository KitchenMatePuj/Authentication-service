import httpx
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from applicationProperties import ApplicationProperties

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str

async def register_user_service(user: RegisterRequest):
    admin_token_url = f"{ApplicationProperties.KEYCLOAK_URL}/realms/{ApplicationProperties.REALM_NAME}/protocol/openid-connect/token"
    users_url = f"{ApplicationProperties.KEYCLOAK_URL}/admin/realms/{ApplicationProperties.REALM_NAME}/users"

    admin_data = {
        "grant_type": "client_credentials",
        "client_id": ApplicationProperties.KEYCLOAK_CLIENT_ID,
        "client_secret": ApplicationProperties.CLIENT_SECRET
    }

    async with httpx.AsyncClient() as client:
        # Obtener token de administrador
        admin_response = await client.post(admin_token_url, data=admin_data)
        if admin_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al obtener el token de administrador")

        admin_token = admin_response.json().get("access_token")

        # Crear usuario en Keycloak
        user_data = {
            "username": user.username,
            "email": user.email,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "enabled": True,
            "credentials": [{"type": "password", "value": user.password, "temporary": False}]
        }

        headers = {"Authorization": f"Bearer {admin_token}", "Content-Type": "application/json"}
        user_response = await client.post(users_url, json=user_data, headers=headers)

        if user_response.status_code not in [200, 201]:
            error_detail = user_response.text
            raise HTTPException(status_code=400, detail=f"Error al registrar el usuario: {error_detail}")

        # Obtener JWT del usuario recién registrado
        token_data = {
            "grant_type": "password",
            "client_id": ApplicationProperties.KEYCLOAK_CLIENT_ID,
            "client_secret": ApplicationProperties.CLIENT_SECRET,
            "username": user.username,
            "password": user.password
        }

        token_response = await client.post(admin_token_url, data=token_data)
        if token_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Usuario creado, pero error al obtener el token")

        return token_response.json()

