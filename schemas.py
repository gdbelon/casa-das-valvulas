from pydantic import BaseModel

class addProduto(BaseModel):
    nome : str
    qtd : int
    marca : str