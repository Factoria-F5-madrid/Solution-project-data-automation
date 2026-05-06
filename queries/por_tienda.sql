-- queries/por_tienda.sql
-- Genera: output/por_tienda.csv
-- Columnas: Tienda, Ciudad, Ingresos, Total_Rentas, Total_Clientes
-- Ejecutada directamente por src/sakila_etl.py → extraer_datos()

SELECT
    s.store_id                      AS Tienda,
    ci.city                         AS Ciudad,
    SUM(p.amount)                   AS Ingresos,
    COUNT(r.rental_id)              AS Total_Rentas,
    COUNT(DISTINCT r.customer_id)   AS Total_Clientes
FROM rental r
JOIN payment  p   ON r.rental_id    = p.rental_id
JOIN inventory i  ON r.inventory_id = i.inventory_id
JOIN store    s   ON i.store_id     = s.store_id
JOIN address  a   ON s.address_id   = a.address_id
JOIN city     ci  ON a.city_id      = ci.city_id
GROUP BY s.store_id, ci.city
ORDER BY Ingresos DESC;
