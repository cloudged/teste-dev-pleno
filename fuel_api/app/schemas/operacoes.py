from pydantic import BaseModel, Field
from datetime import date
from typing import Literal


class OperacaoCreate(BaseModel):
    combustivel_id: int = Field(..., description="ID do combustível")
    tipo: Literal["compra", "venda"] = Field(..., description="Tipo da operação: compra ou venda")
    data: date = Field(..., description="Data da operação")
    litros: float = Field(..., gt=0, description="Quantidade de litros")
    selic: float = Field(..., gt=0, description="Valor do selic aplicado")

    class Config:
        from_attributes = True


class OperacaoResponse(BaseModel):
    id: int
    combustivel_id: int
    tipo: str
    data: date
    ref_id: int
    litros: float
    valor: float
    selic: float

    class Config:
        from_attributes = True
