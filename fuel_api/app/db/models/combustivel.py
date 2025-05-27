from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Combustivel(Base):
    __tablename__ = "combustiveis"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
