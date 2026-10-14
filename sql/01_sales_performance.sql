-- 1. Indicadores generales
SELECT
    COUNT(*) AS total_registros,
    COUNT(DISTINCT order_id) AS total_pedidos,
    COUNT(DISTINCT customer_id) AS total_clientes,
    ROUND(SUM(sales), 2) AS ventas_totales,
    ROUND(SUM(profit), 2) AS beneficio_total,
    ROUND(AVG(discount) * 100, 2) AS descuento_promedio_pct,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0) * 100, 2)
        AS margen_beneficio_pct
FROM orders;

-- 2. Rendimiento por categoría
SELECT
    category,
    COUNT(*) AS total_registros,
    ROUND(SUM(sales), 2) AS ventas,
    ROUND(SUM(profit), 2) AS beneficio,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS margen_pct,
    ROUND(AVG(discount) * 100, 2) AS descuento_promedio_pct
FROM orders
GROUP BY category
ORDER BY beneficio DESC;


-- 3. Rendimiento por subcategoría
SELECT
    category,
    sub_category,
    COUNT(*) AS total_registros,
    ROUND(SUM(sales), 2) AS ventas,
    ROUND(SUM(profit), 2) AS beneficio,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS margen_pct,
    ROUND(AVG(discount) * 100, 2) AS descuento_promedio_pct
FROM orders
GROUP BY category, sub_category
ORDER BY beneficio ASC;

-- 4. Rentabilidad por descuento
SELECT
    CASE
        WHEN discount = 0 THEN '0% - Sin descuento'
        WHEN discount <= 0.10 THEN '1% - 10%'
        WHEN discount <= 0.20 THEN '11% - 20%'
        WHEN discount <= 0.30 THEN '21% - 30%'
        WHEN discount <= 0.50 THEN '31% - 50%'
        ELSE 'Más de 50%'
    END AS rango_descuento,
    COUNT(*) AS registros,
    ROUND(SUM(sales), 2) AS ventas,
    ROUND(SUM(profit), 2) AS beneficio,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS margen_pct
FROM orders
GROUP BY 1
ORDER BY MIN(discount);

-- 5. Descuento por categoría
SELECT
    category,
    CASE
        WHEN discount = 0 THEN 'Sin descuento'
        WHEN discount <= 0.20 THEN 'Hasta 20%'
        ELSE 'Más de 20%'
    END AS rango_descuento,
    COUNT(*) AS registros,
    ROUND(SUM(sales), 2) AS ventas,
    ROUND(SUM(profit), 2) AS beneficio,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS margen_pct
FROM orders
GROUP BY
    category,
    CASE
        WHEN discount = 0 THEN 'Sin descuento'
        WHEN discount <= 0.20 THEN 'Hasta 20%'
        ELSE 'Más de 20%'
    END
ORDER BY category, rango_descuento;

