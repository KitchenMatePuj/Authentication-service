import requests
from fastapi import HTTPException
from applicationProperties import ApplicationProperties


def get_admin_token():
    token_url = f"{ApplicationProperties.KEYCLOAK_URL}/realms/master/protocol/openid-connect/token"

    data = {
        "grant_type": "password",
        "client_id": "admin-cli",
        "username": ApplicationProperties.KEYCLOAK_ADMIN_USERNAME,
        "password": ApplicationProperties.KEYCLOAK_ADMIN_PASSWORD
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print(headers)
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise HTTPException(status_code=500, detail={"error": "No se pudo obtener el token de administrador"})

def reset_password_service(email: str):
    token = get_admin_token()

    search_url = f"{ApplicationProperties.KEYCLOAK_URL}/admin/realms/{ApplicationProperties.REALM_NAME}/users"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    params = {"email": email}

    search_response = requests.get(search_url, headers=headers, params=params)

    if search_response.status_code != 200:
        raise HTTPException(status_code=search_response.status_code, detail={"error": "Error al buscar el usuario"})

    users = search_response.json()

    if not users:
        raise HTTPException(status_code=404, detail={"error": "Usuario no encontrado"})

    user_id = users[0]["id"]

    reset_url = f"{ApplicationProperties.KEYCLOAK_URL}/admin/realms/{ApplicationProperties.REALM_NAME}/users/{user_id}/execute-actions-email"

    data = ["UPDATE_PASSWORD"]

    reset_response = requests.put(reset_url, headers=headers, json=data)

    if reset_response.status_code == 204:
        return {"message": "Correo de restablecimiento enviado"}
    else:
        raise HTTPException(status_code=reset_response.status_code, detail={"error": reset_response.text})
