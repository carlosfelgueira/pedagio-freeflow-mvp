from fastapi import FastAPI
import sqlite3
from datetime import datetime

app = FastAPI()
DATABASE_NAME = "db.sqlite3"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row # Permite acessar colunas por nome
    return conn

def create_table():
    # Função para garantir que a tabela existe no primeiro acesso
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS debitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT NOT NULL,
            hora TEXT NOT NULL,
            valor REAL NOT NULL,
            status TEXT NOT NULL -- PENDENTE ou PAGO
        );
    """)
    conn.commit()
    conn.close()

create_table() # Roda a criação da tabela na inicialização

@app.get("/")
def read_root():
    return {"Olá": "API de Pedágio Free Flow MVP está no ar!"}

# Próximos passos vão incluir os endpoints /passagem, /consulta e /pagar