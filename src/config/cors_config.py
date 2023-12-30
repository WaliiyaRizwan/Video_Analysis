from src import app
from fastapi.middleware.cors import CORSMiddleware


class CorsConfig:
    def __init__(self):
        self.allowed_origins = [
            "http://localhost:3000",
        ]
        app.add_middleware(
            CORSMiddleware,
            allow_origins=self.allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
