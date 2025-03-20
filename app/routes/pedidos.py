from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import criar_pedido, listar_pedidos, get_db
from app.database import Pedido

router = APIRouter()

# Criar um pedido
@router.post("/pedidos/")
def criar_pedido_endpoint(item: str, quantidade: int, db: Session = Depends(get_db)):
    pedido = criar_pedido(db, item, quantidade)
    return {"messagem": "Pedido criado com sucesso!", "pedido": pedido.__dict__}

# Listar todos os pedidos
@router.get("/pedidos/")
def listar_pedidos_endpoint(db: Session = Depends(get_db)):
    pedidos = listar_pedidos(db)
    return pedidos