from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.preco_compra import RefCompra

router = APIRouter()

@router.get("/ref_compra")
def listar_ref_compra(db: Session = Depends(get_db)):
    resultados = db.query(RefCompra).all()
    return resultados
