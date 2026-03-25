import sqlite3

def conectar():
    return sqlite3.connect('banco.db')


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def inserir_usuario(username, password):
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