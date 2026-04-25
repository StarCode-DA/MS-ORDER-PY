from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderCreate(BaseModel):
    usuario_id: int
    sede_id: int
    nombre_cliente: str
    cedula_cliente: str
    nombre_usuario: str

class OrderResponse(BaseModel):
    id: int
    usuario_id: int
    sede_id: int
    status: str
    created_at: Optional[datetime] = None
    nombre_cliente: Optional[str] = None
    cedula_cliente: Optional[str] = None
    nombre_usuario: Optional[str] = None

    model_config = {"from_attributes": True}