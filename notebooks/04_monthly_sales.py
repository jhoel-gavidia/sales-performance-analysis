import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "processed" / "Orders_clean.csv"
FIGURES_DIR = BASE_DIR / "reports" / "figures"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Cargar datos
df = pd.read_csv(FILE_PATH)

# Convertir fecha
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Excluir fechas futuras
today = pd.Timestamp.today().normalize()
df = df[df["Order Date"] <= today].copy()

# Agrupar por mes
df["Month"] = df["Order Date"].dt.to_period("M")

monthly = (
    df.groupby("Month")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

# Convertir período a texto para los gráficos
monthly["Month"] = monthly["Month"].astype(str)

print("Registros analizados:", len(df))
print("Último mes analizado:", monthly["Month"].max())

# Gráfico de ventas mensuales
plt.figure(figsize=(12, 6))
plt.plot(monthly["Month"], monthly["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "monthly_sales.png", dpi=300)
plt.close()

# Gráfico de beneficios mensuales
plt.figure(figsize=(12, 6))
plt.plot(monthly["Month"], monthly["Profit"], marker="o")
plt.axhline(y=0, linestyle="--")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "monthly_profit.png", dpi=300)
plt.close()

print("Gráficos mensuales actualizados correctamente.")

