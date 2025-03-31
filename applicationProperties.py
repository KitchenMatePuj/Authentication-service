import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationProperties:
    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://localhost:8081 ")
    REALM_NAME = os.getenv("REALM_NAME", "fast-api-realm")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "fastapi-client")
    CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "boVOjotkxFcPoTS0tot2uV0UnwWnBYeJ")
    TOKEN_ADMIN = os.getenv("TOKEN_ADMIN", "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJJbXBCNkt2Nkh6WUh6dlA2czlNci1LS3gzY25DNjB5MVZfWWxqMms4NWlNIn0.eyJleHAiOjE3NDMzODk0ODMsImlhdCI6MTc0MzM4OTE4MywianRpIjoiODJkOTE4ZDYtMmFhNy00OGFlLTk2NGUtNGQxY2E1OGI2NWU5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgxL3JlYWxtcy9mYXN0LWFwaS1yZWFsbSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLWNsaSIsInNpZCI6ImU1YjkyMWMyLTAyY2QtNDUxNi05NzMyLWRlOGRhZWY1ZDhjNCIsInNjb3BlIjoiZW1haWwgcHJvZmlsZSJ9.HPWd9ZT0d7SdiEEn8utV3vsV3LkQjb2OhuWIqZOLmjhFmgZE2VRCSJH2JQ6hVfTn1sxtw9VL8eZZIJvyBgdDSH0IyEgOi3g2MfSptQ-EcvMe9ss4ifctVLTWEp8bnGZt6v9RVMP8p4YXs3OQnprdbyIKQprccPDklzjQ175JFIRgQsxVN1p03kIK-T7oheJsNr8v8N-RCNe-DYPClWMO0y9P9Sbq60SlOSStW0ETqZquXu4nMWlOc_iAigXIuyGi_W1p8BZVwfCbkS8xBieiKFdensA255_1lvTU35uD-YNAtHWNaJP_UYXHiZ7Ixx6_WccE5tGKhvl_v-FnWdQJeA")

    APP_PORT = int(os.getenv("APP_PORT", 8008))