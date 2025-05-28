from pydantic import BaseModel
from datetime import datetime


class BalancoResponse(BaseModel):
    id: int
    tipo: str
    ano: int
    total: float
    updated_at: datetime

    class Config:
        from_attributes = True


class BalancoConsultaResponse(BaseModel):
    ano: int
    total_compra: float
    total_venda: float
    diferenca: float
