from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/cliente_info/<int:cliente_id>', methods=['GET'])
def get_cliente_info(cliente_id):
    # Simula um retorno externo
    return jsonify({
        "cliente_id": cliente_id,
        "nome": "Cliente Externo",
        "email": "externo@example.com",
        "status": "ativo"
    })

if __name__ == '__main__':
    app.run(port=5001)
