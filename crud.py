from database import get_connection

def cadastrar_produto(nome,qtd,marca):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM produtos WHERE nome_valvula = %s AND marca = %s',(nome,marca))
        row = cur.fetchone()
        if row is not None:
            return{"sistema" : "Produto já existe"}
        cur.execute('INSERT INTO produtos (nome_valvula,qtd,marca) VALUES (%s,%s,%s) RETURNING id',(nome,qtd,marca))
        row_2 = cur.fetchone()
        conn.commit()
        return{"sistema" : row_2}
    except Exception as e:
        conn.rollback()
        return{e}
    finally:
        cur.close()
        conn.close()

def listar_valvulas():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM produtos')
        rows = cur.fetchall()
        return{"sistema" : rows}
    except Exception as e:
        conn.rollback()
        return{"erro": e}
    finally:
        cur.close()
        conn.close()
        