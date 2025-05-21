import psycopg2
import os
from dotenv import load_dotenv

# Carrega o arquivo .env automaticamente
load_dotenv()

# Pega o valor da variável DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
