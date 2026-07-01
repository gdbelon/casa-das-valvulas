from fastapi import FastAPI
from schemas import addProduto
from crud import cadastrar_produto,listar_valvulas
app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "Sistema Casa das Válvulas"}

@app.post('/produtos')
def cadastrar(novo_produto : addProduto):
    cadastrar_produto(novo_produto.nome, novo_produto.qtd, novo_produto.marca)

@app.get('/produtos/busca')
def buscar():
    listar_valvulas()