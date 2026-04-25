from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from src.database import SessionLocal
from src.models.order import Order
from src.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_orders(sede_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(
        Order.sede_id == sede_id
    ).order_by(Order.id).all()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT rol, sede_id FROM usuarios WHERE id = :id AND activo = true"),
        {"id": order.usuario_id}
    ).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="User not found or inactive")

    rol, sede_id_usuario = result

    if rol not in ["mesero", "administrador"]:
        raise HTTPException(status_code=403, detail="Not authorized to create orders")

    if rol == "mesero" and sede_id_usuario != order.sede_id:
        raise HTTPException(status_code=403, detail="You can only create orders in your assigned location")

    new_order = Order(
        usuario_id=order.usuario_id,
        sede_id=order.sede_id,
        status="ABIERTO",
        nombre_cliente=order.nombre_cliente,
        cedula_cliente=order.cedula_cliente,
        nombre_usuario=order.nombre_usuario
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order