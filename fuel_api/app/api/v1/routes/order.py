from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.order_schema import OrderResponse, OrderCreate
from app.services.order_service import create_order

router = APIRouter(prefix="/order", tags=["orders"])


@router.post("", response_model=OrderResponse)
def create_new_order(
    order_in: OrderCreate,
    db: Session = Depends(get_db)
):
    try:
        order = create_order(db, order_in)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
