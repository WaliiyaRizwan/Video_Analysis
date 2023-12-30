from fastapi import FastAPI, Request, status
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(
    title = "Exercise",
    version="1.0",
    docs_url=None
    if os.environ.get("DOCS_URL") == "None"
    else os.environ.get("DOCS_URL"),
    redoc_url=None
    if os.environ.get("RE_DOC_URL") == "None"
    else os.environ.get("RE_DOC_URL"),
)



from src.config.cors_config import CorsConfig

CorsConfig()

origins = [
    "http://localhost:5500",  # Replace with your front end's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routers import(
    main_router,
    video_router
)

main_router.router.include_router(router=video_router.router)

app.include_router(router=main_router.router)