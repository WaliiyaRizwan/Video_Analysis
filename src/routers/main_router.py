from fastapi import APIRouter

# main router
router = APIRouter(prefix="/api")


@router.get("/test")
def index1():
    return "Hello"
