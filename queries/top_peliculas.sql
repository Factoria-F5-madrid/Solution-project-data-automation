-- queries/top_peliculas.sql
-- Genera: output/top_peliculas.csv
-- Columnas: Pelicula, Ingresos, Total_Rentas
-- Top 20 películas por ingresos
-- Ejecutada directamente por src/sakila_etl.py → extraer_datos()

SELECT
    f.title                     AS Pelicula,
    SUM(p.amount)               AS Ingresos,
    COUNT(r.rental_id)          AS Total_Rentas
FROM rental r
JOIN payment p    ON r.rental_id    = p.rental_id
JOIN inventory i  ON r.inventory_id = i.inventory_id
JOIN film f       ON i.film_id      = f.film_id
GROUP BY f.title
ORDER BY Ingresos DESC
LIMIT 20;
