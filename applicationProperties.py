import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationProperties:
    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "https://keycloak-production-864b.up.railway.app")
    REALM_NAME = os.getenv("REALM_NAME", "fast-api-realm")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "fastapi-client")
    CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "boVOjotkxFcPoTS0tot2uV0UnwWnBYeJ")
    TOKEN_ADMIN = os.getenv("TOKEN_ADMIN", "")

    APP_PORT = int(os.getenv("APP_PORT", 8008))