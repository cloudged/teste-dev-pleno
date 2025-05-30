from sqlalchemy import Column, Integer, Float, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class PurchasePrice(Base):
    __tablename__ = "ref_compra"

    id = Column(Integer, primary_key=True, index=True)
    fuel_id = Column(Integer, ForeignKey("fuel.id"), nullable=False)  # corrigido para singular
    preco = Column(Float, nullable=False)
    mes = Column(Integer, nullable=False)
    tributo = Column(Numeric(5, 2), nullable=False)

    fuel = relationship("Fuel", back_populates="compras")

class SalePrice(Base):
    __tablename__ = "ref_venda"

    id = Column(Integer, primary_key=True, index=True)
    fuel_id = Column(Integer, ForeignKey("fuel.id"), nullable=False)  # corrigido para singular
    preco = Column(Float, nullable=False)
    mes = Column(Integer, nullable=False)
    tributo = Column(Numeric(5, 2), nullable=False)

    fuel = relationship("Fuel", back_populates="vendas")
