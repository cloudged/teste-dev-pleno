from sqlalchemy import Column, Integer, Float, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class RefCompra(Base):
    __tablename__ = "ref_compra"

    id = Column(Integer, primary_key=True, index=True)
    combustivel_id = Column(Integer, ForeignKey("combustivel.id"), nullable=False)  # corrigido para singular
    preco = Column(Float, nullable=False)
    mes = Column(Integer, nullable=False)
    tributo = Column(Numeric(5, 2), nullable=False)

    combustivel = relationship("Combustivel", back_populates="compras")
