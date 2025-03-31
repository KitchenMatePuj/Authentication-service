import requests
from fastapi import HTTPException
from applicationProperties import ApplicationProperties

def reset_password_service(user_id: str):
    url = f"{ApplicationProperties.KEYCLOAK_URL}/auth/admin/realms/{ApplicationProperties.REALM_NAME}/users/{user_id}/execute-actions-email"

    headers = {
        "Authorization": f"Bearer {ApplicationProperties.TOKEN_ADMIN}",
        "Content-Type": "application/json"
    }

    data = ["UPDATE_PASSWORD"]

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 204:
        return {"message": "Correo de restablecimiento enviado"}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())
