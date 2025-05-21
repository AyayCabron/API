import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_connection

app = Flask(__name__)

app.secret_key = 'f6a3d31f6b1a8b7c4a508b73e91d72c3'

SENHA_ADM = 'senha123'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clientes')
def listar_clientes():
    conn = get_connection()
    clientes = []
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, nome, email FROM clientes;")
            clientes = cur.fetchall()
            cur.close()
        except Exception as e:
            print("Erro ao buscar clientes:", e)
        finally:
            conn.close()
    
    return render_template('clientes.html', clientes=clientes)

@app.route('/clientes/adicionar', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        senha = request.form['senha']
        if senha == SENHA_ADM:
            nome = request.form['nome']
            email = request.form['email']
            
            conn = get_connection()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
                    conn.commit()
                    cur.close()
                    return redirect(url_for('listar_clientes'))
                except Exception as e:
                    print("Erro ao adicionar cliente:", e)
                finally:
                    conn.close()
            else:
                print("Erro de conexão com o banco.")
        else:
            return render_template('erro_senha.html', erro="Senha incorreta.")
    
    return render_template('formulario.html')  # Alterado de 'adicionar_cliente.html' para 'formulario.html'

if __name__ == '__main__':
    app.run(debug=True)
