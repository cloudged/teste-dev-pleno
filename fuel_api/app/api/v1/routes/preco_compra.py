from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import Optional, List

from app.db.models.preco_compra import RefCompra
from app.schemas.preco_compra import PrecoCompra
from app.services.preco_compra import get_precos_compra

router = APIRouter()

@router.get("/ref_compra", response_model=List[PrecoCompra])
def listar_ref_compra( combustivel_id: Optional[int] = Query(None),
    mes: Optional[int] = Query(None), db: Session = Depends(get_db)):
    resultados = db.query(RefCompra).all()
    return get_precos_compra(db, combustivel_id=combustivel_id, mes=mes)
