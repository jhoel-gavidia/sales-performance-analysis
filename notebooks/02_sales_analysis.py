
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "Orders_clean.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Cargar los datos
df = pd.read_csv(DATA_PATH, parse_dates=["Order Date", "Ship Date"])

# 1. Ventas y beneficio por categoría
category_summary = (
    df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

print("=== RENDIMIENTO POR CATEGORÍA ===")
print(category_summary.round(2).to_string(index=False))

# 2. Gráfico de ventas por categoría
plt.figure(figsize=(9, 5))
plt.bar(category_summary["Category"], category_summary["Sales"])
plt.title("Ventas por categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
plt.show()

# 3. Gráfico de beneficio por categoría
plt.figure(figsize=(9, 5))
plt.bar(category_summary["Category"], category_summary["Profit"])
plt.axhline(0, linewidth=1)
plt.title("Beneficio por categoría")
plt.xlabel("Categoría")
plt.ylabel("Beneficio")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "profit_by_category.png", dpi=150)
plt.show()

print(f"\nGráficos guardados en: {OUTPUT_DIR}")
