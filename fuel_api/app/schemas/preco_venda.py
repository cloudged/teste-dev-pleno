from pydantic import BaseModel


class PrecoVendaBase(BaseModel):
    combustivel_id: int
    mes: int
    preco: float
    tributo: float


class PrecoVenda(PrecoVendaBase):
    id: int

    class Config:
        from_attributes = True
