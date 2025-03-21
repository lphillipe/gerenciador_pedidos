from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Pedido(Base):
    __tablename__= "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    status = Column(String, default="pendente")
    