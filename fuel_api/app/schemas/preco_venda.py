from pydantic import BaseModel
from typing import Optional


class PrecoVendaBase(BaseModel):
    combustivel_id: int
    mes: int
    preco: float
    tributo: float


class PrecoVenda(PrecoVendaBase):
    id: int

    class Config:
        from_attributes = True
