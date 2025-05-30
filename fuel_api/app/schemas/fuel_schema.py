from pydantic import BaseModel

class FuelSchema(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

class FuelResponse(BaseModel):
    id: int
    nome: str