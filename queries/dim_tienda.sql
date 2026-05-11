-- queries/dim_tienda.sql
-- DIMENSIÓN: Tiendas
-- Genera: output/dim_tienda.csv
-- PK: store_id
-- Relacionada con fact_rentas.store_id

SELECT
    s.store_id,
    ci.city                 AS ciudad,
    co.country              AS pais
FROM store s
JOIN address a   ON s.address_id  = a.address_id
JOIN city    ci  ON a.city_id     = ci.city_id
JOIN country co  ON ci.country_id = co.country_id
ORDER BY s.store_id ASC;
