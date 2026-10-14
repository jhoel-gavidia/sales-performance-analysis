import pandas as pd
from pathlib import Path

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "processed" / "Orders_clean.csv"

# Cargar datos
df = pd.read_csv(FILE_PATH)

# Convertir fechas
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Control del rango de fechas
print("\n=== CONTROL DEL RANGO DE FECHAS ===")
print("Primera fecha original:", df["Order Date"].min().date())
print("Última fecha original:", df["Order Date"].max().date())

# Definir fecha de corte: fecha actual del sistema
today = pd.Timestamp.today().normalize()

# Identificar y excluir registros futuros
future_rows = (df["Order Date"] > today).sum()

print("Registros con fecha futura:", future_rows)

df = df[df["Order Date"] <= today].copy()

print("Registros analizados:", len(df))
print("Última fecha analizada:", df["Order Date"].max().date())

# Crear columna mensual
df["Month"] = df["Order Date"].dt.to_period("M")

# Resumen mensual
monthly = (
    df.groupby("Month")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Records=("Order ID", "count")
    )
    .reset_index()
)

# Calcular margen de beneficio
monthly["Margin (%)"] = (
    monthly["Profit"] / monthly["Sales"] * 100
).where(monthly["Sales"] != 0, 0)

# Mostrar resultados
print("\n=== RESUMEN MENSUAL ===")
print(
    monthly.assign(
        Sales=monthly["Sales"].round(2),
        Profit=monthly["Profit"].round(2),
        **{"Margin (%)": monthly["Margin (%)"].round(2)}
    ).to_string(index=False)
)

# Identificar mejores y peores meses
best_sales = monthly.loc[monthly["Sales"].idxmax()]
worst_sales = monthly.loc[monthly["Sales"].idxmin()]

best_profit = monthly.loc[monthly["Profit"].idxmax()]
worst_profit = monthly.loc[monthly["Profit"].idxmin()]

print("\n=== INSIGHTS MENSUALES ===")

print(
    f"Mayor venta: {best_sales['Month']} | "
    f"Ventas: {best_sales['Sales']:.2f} | "
    f"Beneficio: {best_sales['Profit']:.2f} | "
    f"Pedidos: {int(best_sales['Orders'])}"
)

print(
    f"Menor venta: {worst_sales['Month']} | "
    f"Ventas: {worst_sales['Sales']:.2f} | "
    f"Beneficio: {worst_sales['Profit']:.2f} | "
    f"Pedidos: {int(worst_sales['Orders'])}"
)

print(
    f"Mayor beneficio: {best_profit['Month']} | "
    f"Beneficio: {best_profit['Profit']:.2f} | "
    f"Ventas: {best_profit['Sales']:.2f} | "
    f"Margen: {best_profit['Margin (%)']:.2f}%"
)

print(
    f"Menor beneficio: {worst_profit['Month']} | "
    f"Beneficio: {worst_profit['Profit']:.2f} | "
    f"Ventas: {worst_profit['Sales']:.2f} | "
    f"Margen: {worst_profit['Margin (%)']:.2f}%"
)

# Exportar resumen mensual
output_path = BASE_DIR / "data" / "processed" / "Monthly_insights.csv"
monthly.to_csv(output_path, index=False)

print(f"\nResumen mensual exportado en: {output_path}")