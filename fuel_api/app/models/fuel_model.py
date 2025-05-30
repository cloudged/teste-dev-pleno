from sqlalchemy import Column, Integer, String
from app.db.session import Base
from sqlalchemy.orm import relationship

class Fuel(Base):
    __tablename__ = "fuel"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)

    # Relacionamentos opcionais para compras e vendas
    compras = relationship("PurchasePrice", back_populates="fuel")
    vendas = relationship("SalePrice", back_populates="fuel")
