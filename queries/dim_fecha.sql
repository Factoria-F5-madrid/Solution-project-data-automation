-- queries/dim_fecha.sql
-- DIMENSIÓN: Fechas (calendar table derivada de rentals)
-- Genera: output/dim_fecha.csv
-- PK: fecha
-- Relacionada con fact_rentas.fecha

SELECT DISTINCT
    DATE(r.rental_date)                     AS fecha,
    YEAR(r.rental_date)                     AS anio,
    QUARTER(r.rental_date)                  AS trimestre,
    MONTH(r.rental_date)                    AS mes_num,
    MONTHNAME(r.rental_date)               AS mes_nombre,
    DAY(r.rental_date)                      AS dia,
    DAYNAME(r.rental_date)                  AS dia_semana,
    WEEK(r.rental_date, 1)                  AS semana_anio
FROM rental r
ORDER BY fecha ASC;
