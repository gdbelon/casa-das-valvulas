from fastapi import FastAPI
from schemas import addProduto
from crud import cadastrar_produto,listar_valvulas,listar_uma_valvula
app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "Sistema Casa das Válvulas"}

@app.post('/produtos')
def cadastrar(novo_produto : addProduto):
    return cadastrar_produto(novo_produto.nome, novo_produto.qtd, novo_produto.marca)

@app.get('/produtos/listar-valvulas')
def buscar():
    return listar_valvulas()

@app.get('/produtos/busca-uma-valvula')
def buscar(nome : str):
    return listar_uma_valvula(nome)
