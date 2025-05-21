CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE atendentes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    atendente_id INT REFERENCES atendentes(id),
    titulo TEXT NOT NULL,
    descricao TEXT,
    status VARCHAR(20) DEFAULT 'aberto',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE interacoes (
    id SERIAL PRIMARY KEY,
    ticket_id INT REFERENCES tickets(id),
    mensagem TEXT,
    autor VARCHAR(50), -- 'cliente' ou 'atendente'
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
