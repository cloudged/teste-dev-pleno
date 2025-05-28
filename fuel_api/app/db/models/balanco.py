from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.db.base import Base


class Balanco(Base):
    __tablename__ = "balanco"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # compra ou venda
    ano = Column(Integer, nullable=False)
    total = Column(Float, nullable=False, default=0.0)
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
