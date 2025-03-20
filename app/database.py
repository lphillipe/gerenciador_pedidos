from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Configuração do banco de dados SQLite(pode ser alterado no futuro)
DATABASE_URL = "sqlite:///./pedidos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Criar a tabela de pedidos
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, index=True)
    quantidade = Column(Integer)

# Criar a tabela no banco de dados
Base.metadata.create_all(bind=engine)
