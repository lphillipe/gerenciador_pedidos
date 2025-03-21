from pydantic import BaseModel, Field

class PedidoBase(BaseModel):
    descricao: str = Field(..., example="Pedido de teste")
    preco: float = Field(..., example=99.99)
    status: str = Field(default="pendente", example="concluido")

class PedidoCreate(PedidoBase):
    pass

class PedidoResponse(PedidoBase):
    id:int