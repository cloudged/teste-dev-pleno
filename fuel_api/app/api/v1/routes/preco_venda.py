from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.preco_venda import RefVenda

router = APIRouter()

@router.get("/ref_venda")
def listar_ref_venda(db: Session = Depends(get_db)):
    resultados = db.query(RefVenda).all()
    return resultados
