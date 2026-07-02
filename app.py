from fastapi import FastAPI
from schemas import addProduto
from crud import cadastrar_produto,listar_valvulas,listar_uma_valvula,atualizar_nome_valvula,atualizar_qtd
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

@app.patch('/produtos/atualizar-nome')
def atualizar(nome : str, id : int):
    return atualizar_nome_valvula(id,nome)

@app.patch('produtos/atualiza-qtd')
def atualizar(id : int, qtd : int):
    return atualizar_qtd(id,qtd)