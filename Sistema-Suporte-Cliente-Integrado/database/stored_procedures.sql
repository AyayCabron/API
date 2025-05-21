CREATE OR REPLACE FUNCTION contar_tickets_por_cliente(cliente_id INT)
RETURNS INT AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM tickets WHERE tickets.cliente_id = cliente_id);
END;
$$ LANGUAGE plpgsql;
