# Documentação da API

## GET /api/cliente_info/{cliente_id}

Retorna dados simulados de um cliente via API.

### Request
- Method: `GET`
- URL Params: `cliente_id`

### Response
```json
{
  "cliente_id": 1,
  "nome": "Cliente Externo",
  "email": "externo@example.com",
  "status": "ativo"
}
