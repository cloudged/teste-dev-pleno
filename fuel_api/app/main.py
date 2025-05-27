from fastapi import FastAPI
from app.api.v1.routes import combustiveis

app = FastAPI(
    title="Fuel API",
    version="1.0.0",
    description="API para gerenciamento de combustíveis",
)

app.include_router(
    combustiveis.router,
    prefix="/api/v1",
    tags=["Combustíveis"]
)
