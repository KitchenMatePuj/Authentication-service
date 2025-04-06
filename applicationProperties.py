import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationProperties:
    KEYCLOAK_ADMIN_PASSWORD = os.getenv("KEYCLOAK_ADMIN_PASSWORD")
    KEYCLOAK_ADMIN_USERNAME = os.getenv("KEYCLOAK_ADMIN_USERNAME")
    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
    REALM_NAME = os.getenv("REALM_NAME")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
    CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

    APP_PORT = int(os.getenv("APP_PORT", 8008))