from fastapi import FastAPI
from app.routes import pedidos # Importa a rota de pedido

app = FastAPI()

app.include_router(pedidos.router) # Adiciona a rota

@app.get("/")
def read_root():
    return {"Mensagem": "API Gerenciamento de Pedidos"}