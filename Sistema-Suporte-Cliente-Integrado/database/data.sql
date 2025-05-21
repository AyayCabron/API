INSERT INTO clientes (nome, email) VALUES
('João da Silva', 'joao@example.com'),
('Maria Oliveira', 'maria@example.com');

INSERT INTO atendentes (nome, email) VALUES
('Carlos Souza', 'carlos@suporte.com'),
('Ana Lima', 'ana@suporte.com');

INSERT INTO tickets (cliente_id, atendente_id, titulo, descricao)
VALUES
(1, 1, 'Erro ao logar', 'Não consigo acessar minha conta.'),
(2, 2, 'Cobrança indevida', 'Recebi uma cobrança que não reconheço.');
