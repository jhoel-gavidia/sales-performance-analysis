
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "Orders_clean.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Cargar datos
df = pd.read_csv(DATA_PATH)

# Agrupar los descuentos por rangos
conditions = [
    df["Discount"] == 0,
    df["Discount"] <= 0.10,
    df["Discount"] <= 0.20,
    df["Discount"] <= 0.30,
    df["Discount"] <= 0.50,
    df["Discount"] > 0.50,
]

labels = [
    "0% - Sin descuento",
    "1% - 10%",
    "11% - 20%",
    "21% - 30%",
    "31% - 50%",
    "Más de 50%",
]

df["Discount Range"] = pd.cut(
    df["Discount"],
    bins=[-0.001, 0, 0.10, 0.20, 0.30, 0.50, 1.0],
    labels=labels,
    include_lowest=True,
)

# Resumen de rentabilidad
summary = (
    df.groupby("Discount Range", observed=False)
    .agg(
        Records=("Sales", "size"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
    )
    .reset_index()
)

summary["Margin (%)"] = summary["Profit"] / summary["Sales"] * 100

print("=== RENTABILIDAD POR DESCUENTO ===")
print(summary.round(2).to_string(index=False))

# Gráfico de margen
plt.figure(figsize=(10, 6))
plt.bar(summary["Discount Range"].astype(str), summary["Margin (%)"])
plt.axhline(0, linewidth=1)
plt.title("Margen de beneficio por rango de descuento")
plt.xlabel("Rango de descuento")
plt.ylabel("Margen (%)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "margin_by_discount.png", dpi=150)
plt.show()

print(f"\nGráfico guardado en: {OUTPUT_DIR / 'margin_by_discount.png'}")
