from fastapi import APIRouter
from app.api.v1.routes.combustiveis import router as combustiveis_router
from app.api.v1.routes.preco_compra import router as ref_compra_router
from app.api.v1.routes.preco_venda import router as ref_venda_router
# from app.api.v1.routes.operacoes import router as operacoes_router
# from app.api.v1.routes.preco_operacoes import router as preco_operacoes_router

api_router = APIRouter()
api_router.include_router(combustiveis_router, prefix="/combustiveis", tags=["combustiveis"])
api_router.include_router(ref_compra_router, prefix="/ref_compra", tags=["ref_compra"])
api_router.include_router(ref_venda_router, prefix="/ref_venda", tags=["ref_venda"])
# api_router.include_router(operacoes_router, prefix="/operacoes", tags=["operacoes"])
# api_router.include_router(preco_operacoes_router, prefix="/preco_operacoes", tags=["preco_operacoes"])
