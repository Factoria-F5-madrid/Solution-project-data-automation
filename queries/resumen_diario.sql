-- queries/resumen_diario.sql
-- Genera: output/resumen_diario.csv
-- Columnas: Fecha, Ingresos, Clientes, Rentas
-- Ejecutada directamente por src/sakila_etl.py → extraer_datos()

SELECT
    DATE(r.rental_date)                     AS Fecha,
    SUM(p.amount)                           AS Ingresos,
    COUNT(DISTINCT r.customer_id)           AS Clientes,
    COUNT(r.rental_id)                      AS Rentas
FROM rental r
JOIN payment p  ON r.rental_id   = p.rental_id
JOIN customer c ON r.customer_id = c.customer_id
GROUP BY DATE(r.rental_date)
ORDER BY Fecha ASC;
