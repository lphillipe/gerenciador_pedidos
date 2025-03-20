from sqlalchemy.orm import Session
from app.database import Pedido, SessionLocal

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar um pedido no banco de dados
def criar_pedido(db: Session, item: str, quantidade: int):
    pedido = Pedido(item=item, quantidade=quantidade)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido

# Listar todos os pedidos
def listar_pedidos(db: Session):
    return db.query(Pedido).all()