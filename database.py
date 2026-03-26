import sqlite3

def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE Uniformes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR (30) NOT NULL,
    valor FLOAT NOT NULL,
    quantidade INT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def cadastrar_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO usuarios (username, password)
        VALUES (?, ?)
    ''', (username, password))

    conn.commit()
    conn.close()


def buscar_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM usuarios
        WHERE username = ? AND password = ?
    ''', (username, password))

    usuario = cursor.fetchone()

    conn.close()
    return usuario

def cadastar_uniforme(descricao, valor, quantidade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Uniformes (descricao, valor, quantidade)
    values(?, ?, ?)
''', (descricao, valor, quantidade))