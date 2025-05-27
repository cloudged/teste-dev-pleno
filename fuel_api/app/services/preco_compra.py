from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.models.preco_compra import RefCompra


def get_precos_compra(
    db: Session, combustivel_id: Optional[int] = None, mes: Optional[int] = None
) -> List[RefCompra]:
    query = db.query(RefCompra)
    
    if combustivel_id is not None:
        query = query.filter(RefCompra.combustivel_id == combustivel_id)
    
    if mes is not None:
        query = query.filter(RefCompra.mes == mes)
    
    return query.all()