from sqlalchemy.orm import Session
from .models import Pedido
from .schemas import PedidoCreate, PedidoBase

def criar_pedido(db: Session, pedido: PedidoCreate):
    db_pedido = Pedido(**pedido.model_dump())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def listar_pedidos(db: Session):
    return db.query(Pedido).all()

def obter_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def atualizar_pedido(db: Session, pedido_id: int, pedido_update: PedidoBase):
    db_pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if db_pedido:
        for key, value in pedido_update.model_dump().items():
            setattr(db_pedido, key, value)
        db.commit()
        db.refresh(db_pedido)
    return db_pedido

def deletar_pedido(db: Session, pedido_id: int):
    db_pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
    return db_pedido
