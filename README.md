# Análisis de ventas y rentabilidad

## 1. Descripción del proyecto

Este proyecto analiza el rendimiento de ventas y la rentabilidad de un conjunto de datos comerciales. El objetivo es identificar tendencias mensuales, comparar categorías y subcategorías de productos y evaluar cómo se relacionan los descuentos con los beneficios obtenidos.

Se utilizaron Python, PostgreSQL y Power BI para inspeccionar, procesar, consultar y visualizar los datos, transformándolos en información útil para la toma de decisiones empresariales.

## 2. Objetivos

- Analizar la evolución mensual de las ventas y los beneficios.
- Comparar el rendimiento comercial de las categorías y subcategorías.
- Evaluar la rentabilidad según los rangos de descuento.
- Identificar productos y categorías con beneficios negativos.
- Diseñar un dashboard interactivo con indicadores clave de rendimiento (KPI).
- Formular recomendaciones basadas en los resultados obtenidos.

## 3. Herramientas utilizadas

| Herramienta | Aplicación |
|---|---|
| Google Sheets | Revisión y exportación inicial de los datos |
| Python | Inspección, procesamiento y análisis de datos |
| Pandas | Manipulación y transformación de datos |
| Matplotlib y Seaborn | Generación de visualizaciones |
| PostgreSQL | Almacenamiento y consultas SQL |
| Power BI | Dashboard interactivo e indicadores de negocio |
| Git y GitHub | Control de versiones y publicación del proyecto |

## 4. Estructura del proyecto

```text
sales-performance-analysis/
├── data/
│   ├── raw/
│   │   └── Orders.csv
│   └── processed/
│       ├── Orders_clean.csv
│       └── Monthly_insights.csv
├── notebooks/
│   ├── 01_data_inspection.py
│   ├── 02_sales_analysis.py
│   ├── 03_discount_analysis.py
│   ├── 04_monthly_sales.py
│   └── 05_monthly_insights.py
├── sql/
│   └── 01_sales_performance.sql
├── powerbi/
│   └── Sales_Performance_Analysis.pbix
├── reports/
│   └── figures/
└── README.md
```

## 5. Datos y preparación

El conjunto de datos original contiene **10.194 registros y 21 columnas**, entre ellas fechas de pedido y envío, información de clientes, categorías de productos, ventas, cantidades, descuentos y beneficios.

La inspección inicial incluyó:

- Revisión de tipos de datos y valores nulos.
- Comprobación de filas duplicadas.
- Validación de fechas de pedido y envío.
- Identificación de beneficios negativos y descuentos elevados.
- Conversión de las fechas a formatos apropiados para el análisis.

No se encontraron valores nulos ni filas exactamente duplicadas durante la inspección inicial.

Se conservaron los registros originales. Para el análisis se excluyeron los pedidos con fechas posteriores al 14 de octubre de 2026, con el propósito de evitar que registros futuros distorsionaran los resultados históricos.

## 6. Análisis realizado

### Análisis exploratorio con Python

Se examinaron la distribución de las ventas, los beneficios, las cantidades y los descuentos. También se identificaron registros con pérdidas y valores extremos que requieren interpretación comercial.

### Consultas SQL con PostgreSQL

Se realizaron consultas para calcular indicadores generales, comparar categorías y subcategorías y analizar la rentabilidad por rangos de descuento.

### Análisis temporal

Se agruparon los resultados por mes para identificar periodos con mayores y menores ventas y beneficios.

### Visualización con Power BI

Se construyó un dashboard con dos páginas:

**Página 1: Resumen ejecutivo**
- Ventas totales.
- Beneficio total.
- Pedidos totales.
- Clientes totales.
- Margen de beneficio.
- Evolución mensual de ventas.
- Ventas y beneficios por categoría.
- Margen de beneficio por categoría.

**Página 2: Análisis de rentabilidad**
- Evolución mensual de beneficios.
- Beneficio por rango de descuento.
- Beneficio por subcategoría de producto.

El informe incorpora filtros para explorar los resultados por categoría.

## 7. Principales hallazgos

- **Rendimiento por categoría:** Tecnología obtuvo el mayor beneficio total en el conjunto de datos original.
- **Rentabilidad de Furniture:** la categoría Furniture presentó un margen de beneficio considerablemente menor que Technology y Office Supplies.
- **Descuentos elevados:** los rangos de descuento superiores al 20 % estuvieron asociados con pérdidas agregadas en el conjunto original.
- **Subcategorías problemáticas:** Tables, Bookcases y Supplies destacaron por sus resultados de rentabilidad negativos.
- **Rendimiento mensual:** diciembre de 2025 registró las mayores ventas y el mayor beneficio mensual dentro del periodo analizado.

Los resultados representan asociaciones agregadas. No demuestran, por sí solos, que los descuentos sean la causa directa de las pérdidas.

## 8. Recomendaciones de negocio

1. Revisar los precios, costos y márgenes de las subcategorías con beneficios negativos.
2. Evaluar las políticas de descuentos elevados antes de aplicarlas de forma generalizada.
3. Supervisar conjuntamente las ventas, los beneficios y el margen de rentabilidad.
4. Investigar los meses con caídas o cambios significativos en el rendimiento.
5. Utilizar el dashboard para comparar categorías y detectar oportunidades de mejora.

## 9. Competencias demostradas

- Inspección y preparación de datos.
- Análisis exploratorio de datos.
- Manipulación de datos con Pandas.
- Consultas y agregaciones SQL.
- Análisis de ventas y rentabilidad.
- Creación de indicadores KPI.
- Visualización de datos.
- Diseño de dashboards en Power BI.
- Comunicación de hallazgos y recomendaciones de negocio.

## 10. Consideraciones

La moneda y el contexto comercial del conjunto de datos deben confirmarse antes de interpretar los importes como una moneda específica. Los resultados y conclusiones deben contrastarse con las consultas y los filtros aplicados en cada herramienta.

Este proyecto tiene fines de aprendizaje.
