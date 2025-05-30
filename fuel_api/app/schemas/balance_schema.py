from pydantic import BaseModel


class BalanceResponse(BaseModel):
    ano: int
    total_compra: float
    total_venda: float
    diferenca: float
