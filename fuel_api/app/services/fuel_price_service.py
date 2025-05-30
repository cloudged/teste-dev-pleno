from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.fuel_price_model import PurchasePrice, SalePrice


def get_purchase_price(db: Session, fuel_id: int, mes: int):
    return db.query(PurchasePrice).filter(
        PurchasePrice.fuel_id == fuel_id,
        PurchasePrice.mes == mes
    ).first()


def get_sale_price(db: Session, fuel_id: int, mes: int):
    return db.query(SalePrice).filter(
        SalePrice.fuel_id == fuel_id,
        SalePrice.mes == mes
    ).first()