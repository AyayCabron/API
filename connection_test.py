from db_connection import get_connection

conn = get_connection()
if conn:
    print("Conexão bem-sucedida com o PostgreSQL!")
    conn.close()
else:
    print("Falha na conexão.")
