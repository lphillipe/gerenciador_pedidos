from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import PedidoCreate, PedidoResponse, PedidoBase
from . import crud
from typing import List

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# Criar um pedido
@router.post("/", response_model=PedidoResponse, status_code=201)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return crud.criar_pedido(db, pedido)

@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return crud.listar_pedidos(db)

@router.put("/{pedido_id}", response_model=PedidoResponse)
def atualizar_pedido(pedido_id: int, pedido_update: PedidoBase, db: Session = Depends(get_db)):
    pedido = crud.atualizar_pedido(db, pedido_id, pedido_update)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.delete("/{pedido_id}", status_code=204)
def deletar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = crud.deletar_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return {"message": "Pedido deletado com sucesso!"}