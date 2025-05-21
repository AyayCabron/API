-- p Listar tickets com status 'aberto'
SELECT * FROM tickets WHERE status = 'aberto';

-- Histórico de interações de um ticket
SELECT * FROM interacoes WHERE ticket_id = 1 ORDER BY criado_em;

-- Atribur atendente a ticket
UPDATE tickets SET atendente_id = 2 WHERE id = 1;
