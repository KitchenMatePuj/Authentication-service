import httpx
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from applicationProperties import ApplicationProperties

async def authenticate_user(form_data: OAuth2PasswordRequestForm):
    print("Entro")
    token_url = f"{ApplicationProperties.KEYCLOAK_URL}/realms/{ApplicationProperties.REALM_NAME}/protocol/openid-connect/token"

    data = {
        "grant_type": "password",
        "client_id": ApplicationProperties.KEYCLOAK_CLIENT_ID,
        "client_secret": ApplicationProperties.CLIENT_SECRET,
        "username": form_data.username,
        "password": form_data.password,
    }

    print(form_data.username)
    print(form_data.password)

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return response.json()
