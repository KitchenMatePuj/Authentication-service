import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.register_controller import router as register_router
from controller.auth_controller import router as auth_router
from controller.password_controller import router as password_reset_router
from applicationProperties import ApplicationProperties

app = FastAPI(
    title="Auth Application API",
    description="Fast API application for authentication handling using KeyCloak",
    version="1.0.0",
)

origins = [
    ApplicationProperties.WEB_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register_router)
app.include_router(auth_router)
app.include_router(password_reset_router)




