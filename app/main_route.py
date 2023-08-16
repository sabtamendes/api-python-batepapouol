from fastapi import APIRouter
from app.routes.batepapo_router import batepapo_router 

route = APIRouter()

route.include_router(batepapo_router, prefix="/api")
