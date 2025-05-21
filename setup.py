from db_connection import get_connection
import os

def executar_sql_de_arquivo(caminho_arquivo):
    """Lê e executa um arquivo SQL no banco de dados"""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                sql = f.read()
                cur.execute(sql)
                conn.commit()
                print(f"Arquivo {caminho_arquivo} executado com sucesso!")
            cur.close()
        except Exception as e:
            print(f"Erro ao executar {caminho_arquivo}:", e)
        finally:
            conn.close()
    else:
        print("Falha na conexão com o banco.")

# Caminho correto dos arquivos SQL, considerando que estão em Sistema-Suporte-Cliente-Integrado/database/
caminho_base = os.path.dirname(os.path.abspath(__file__))  # Diretório onde o script 'setup.py' está
caminho_schema = os.path.join(caminho_base, 'Sistema-Suporte-Cliente-Integrado', 'database', 'schema.sql')
caminho_data = os.path.join(caminho_base, 'Sistema-Suporte-Cliente-Integrado', 'database', 'data.sql')

# Verifique se os arquivos existem no caminho esperado
if not os.path.exists(caminho_schema):
    print(f"Arquivo schema.sql não encontrado em: {caminho_schema}")
if not os.path.exists(caminho_data):
    print(f"Arquivo data.sql não encontrado em: {caminho_data}")

# Executar os arquivos SQL para criar as tabelas e inserir os dados
if __name__ == "__main__":
    print("Iniciando configuração do banco de dados...")
    executar_sql_de_arquivo(caminho_schema)
    executar_sql_de_arquivo(caminho_data)
    print("Configuração do banco de dados concluída.")
