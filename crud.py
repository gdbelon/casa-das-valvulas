from database import get_connection
from psycopg2.extras import RealDictCursor

def cadastrar_produto(nome,qtd,marca):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute('SELECT * FROM produtos WHERE nome_valvula = %s AND marca = %s',(nome,marca))
        row = cur.fetchone()
        if row is not None:
            return{"mensagem" : "Produto já existe"}
        cur.execute('INSERT INTO produtos (nome_valvula,qtd,marca) VALUES (%s,%s,%s)',(nome,qtd,marca))
        row_2 = cur.fetchone()
        conn.commit()
        return{"mensagem" : row_2 }
    except Exception as e:
        conn.rollback()
        return{e}
    finally:
        cur.close()
        conn.close()

def listar_valvulas():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute('SELECT * FROM produtos')
        rows = cur.fetchall()
        return{"mensagem" : rows}
    except Exception as e:
        conn.rollback()
        return{"erro": e}
    finally:
        cur.close()
        conn.close()

def listar_uma_valvula(nome):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM produtos WHERE nome_valvula ~* %s", (f"^{nome}",))
        row = cur.fetchone()
        if row is None:
            return{"mensagem" : "Nenhum Produto foi encontrado"}
        return{"mensagem" : row}
    except Exception as e:
        conn.rollback()
        return{"erro" : str(e)}
    finally:
        cur.close()
        conn.close()

def atualizar_nome_valvula(id,nome):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM produtos WHERE nome_valvula = %s AND id = %s',(nome,id))
        row = cur.fetchone()
        if row is True:
            return{"mensagem" : "Já existe um produto com esse nome"}
        cur.execute('UPDATE produtos SET nome_valvula = %s WHERE id = %s',(nome,id))
        row_2 = cur.fetchone()
        conn.commit()
        return{"mensagem" : row_2}
    except Exception as e:
        conn.rollback()
        return{"erro" : str(e)}
    finally:
        cur.close()
        conn.close()

def atualizar_qtd(id,qtd):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('UPDATE produtos SET qtd = %s WHERE id = %s',(qtd,id))
        row = cur.fetchone()
        conn.commit()
        return{"mensagem" : row}
    except Exception as e:
        conn.rollback()
        return{"erro" : str(e)}
    finally:
        cur.close()
        conn.close()
        
