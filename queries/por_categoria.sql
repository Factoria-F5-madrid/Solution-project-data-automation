-- queries/por_categoria.sql
-- Genera: output/por_categoria.csv
-- Columnas: Categoria, Ingresos, Total_Rentas
-- Ejecutada directamente por src/sakila_etl.py → extraer_datos()

SELECT
    cat.name                    AS Categoria,
    SUM(p.amount)               AS Ingresos,
    COUNT(r.rental_id)          AS Total_Rentas
FROM rental r
JOIN payment p        ON r.rental_id    = p.rental_id
JOIN inventory i      ON r.inventory_id = i.inventory_id
JOIN film f           ON i.film_id      = f.film_id
JOIN film_category fc ON f.film_id      = fc.film_id
JOIN category cat     ON fc.category_id = cat.category_id
GROUP BY cat.name
ORDER BY Ingresos DESC;
