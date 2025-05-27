from pydantic import BaseModel


class PrecoCompraBase(BaseModel):
    combustivel_id: int
    mes: int
    preco: float
    tributo: float


class PrecoCompra(PrecoCompraBase):
    id: int

    class Config:
        from_attributes = True
