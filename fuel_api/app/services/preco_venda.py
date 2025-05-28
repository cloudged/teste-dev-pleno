from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.models.preco_venda import RefVenda


def get_precos_venda(
    db: Session, combustivel_id: Optional[int] = None, mes: Optional[int] = None
) -> List[RefVenda]:
    query = db.query(RefVenda)
    
    if combustivel_id is not None:
        query = query.filter(RefVenda.combustivel_id == combustivel_id)
    
    if mes is not None:
        query = query.filter(RefVenda.mes == mes)
    
    return query.all()

def buscar_referencia(db: Session, combustivel_id: int, mes: int):
    return db.query(RefVenda).filter(
        RefVenda.combustivel_id == combustivel_id,
        RefVenda.mes == mes
    ).first()