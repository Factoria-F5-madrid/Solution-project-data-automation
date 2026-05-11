-- queries/dim_pelicula.sql
-- DIMENSIÓN: Películas
-- Genera: output/dim_pelicula.csv
-- PK: film_id
-- Relacionada con fact_rentas.film_id

SELECT
    f.film_id,
    f.title                 AS titulo,
    f.rating,
    f.length                AS duracion_min,
    f.rental_rate           AS precio_renta,
    f.replacement_cost      AS costo_reposicion
FROM film f
ORDER BY f.film_id ASC;
