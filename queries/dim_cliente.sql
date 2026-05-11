-- queries/dim_cliente.sql
-- DIMENSIÓN: Clientes
-- Genera: output/dim_cliente.csv
-- PK: customer_id
-- Relacionada con fact_rentas.customer_id

SELECT
    c.customer_id,
    c.first_name            AS nombre,
    c.last_name             AS apellido,
    c.email,
    ci.city                 AS ciudad,
    co.country              AS pais
FROM customer c
JOIN address a   ON c.address_id  = a.address_id
JOIN city    ci  ON a.city_id     = ci.city_id
JOIN country co  ON ci.country_id = co.country_id
ORDER BY c.customer_id ASC;
