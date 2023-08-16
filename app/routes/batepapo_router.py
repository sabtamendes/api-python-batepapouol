from fastapi import APIRouter

batepapo_router = APIRouter()

@batepapo_router.get("/health")
def read_health():
    return {"message": "Hello World"}