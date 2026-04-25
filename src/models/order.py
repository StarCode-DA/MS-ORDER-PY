from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from src.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    sede_id = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default="ABIERTO")
    created_at = Column(TIMESTAMP, server_default=func.now())
    nombre_cliente = Column(String(100), nullable=True)
    cedula_cliente = Column(String(20), nullable=True)
    nombre_usuario = Column(String(100), nullable=True)