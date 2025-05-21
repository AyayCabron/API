import requests

def buscar_cliente_info(cliente_id):
    url = f"http://localhost:5001/api/cliente_info/{cliente_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    info = buscar_cliente_info(1)
    print("Dados recebidos da API externa:", info)
