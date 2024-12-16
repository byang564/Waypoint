from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import path

ALLOWED_ORIGINS = ["http://localhost:5173"]

def initialize_application() -> FastAPI:
    app = FastAPI()

    app.include_router(path.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app