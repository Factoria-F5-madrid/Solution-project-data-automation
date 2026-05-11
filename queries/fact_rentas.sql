-- queries/fact_rentas.sql
-- TABLA DE HECHOS del modelo estrella
-- Genera: output/fact_rentas.csv
-- Granularidad: una fila por renta
-- PK: rental_id
-- FK: customer_id → dim_cliente | film_id → dim_pelicula
--     category_id → dim_categoria | store_id → dim_tienda
--     fecha       → dim_fecha

SELECT
    r.rental_id,
    DATE(r.rental_date)     AS fecha,
    r.customer_id,
    i.film_id,
    fc.category_id,
    i.store_id,
    p.amount                AS monto
FROM rental r
JOIN payment       p  ON r.rental_id    = p.rental_id
JOIN inventory     i  ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id      = fc.film_id
ORDER BY r.rental_id ASC;
