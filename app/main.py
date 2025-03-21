from fastapi import FastAPI
from .database import Base, engine
from .routes import router # Importa a rota de pedido

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Gerenciador de Pedidos API")

app.include_router(router) # Adiciona a rota

@app.get("/", tags=["Status"])
def root():
    return {"Mensagem": "API Gerenciamento de Pedidos"}