-- queries/dim_categoria.sql
-- DIMENSIÓN: Categorías de películas
-- Genera: output/dim_categoria.csv
-- PK: category_id
-- Relacionada con fact_rentas.category_id

SELECT
    cat.category_id,
    cat.name                AS categoria
FROM category cat
ORDER BY cat.category_id ASC;
