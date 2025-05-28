from pydantic import BaseModel

class CombustivelSchema(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

class CombustivelResponse(BaseModel):
    id: int
    nome: str