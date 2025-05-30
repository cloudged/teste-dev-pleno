from fastapi import APIRouter

from app.api.v1.routes import balance, fuel, order

api_router = APIRouter()
api_router.include_router(balance.router)
api_router.include_router(fuel.router)
api_router.include_router(order.router)