import pandas as pd
from pathlib import Path

file_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "Orders.csv"

# Verificar que el archivo exista
if not file_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

# Cargar los datos sin modificar el archivo original
df = pd.read_csv(file_path)

# 1. Dimensiones
print("=== DIMENSIONES ===")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")

# 2. Columnas y tipos de datos
print("\n=== TIPOS DE DATOS ===")
print(df.dtypes)

# 3. Valores faltantes
print("\n=== VALORES FALTANTES ===")
print(df.isnull().sum())

# 4. Filas duplicadas completas
print("\n=== DUPLICADOS ===")
print(f"Filas duplicadas: {df.duplicated().sum()}")

# 5. Estadísticas de las métricas comerciales
print("\n=== RESUMEN ESTADÍSTICO ===")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())


# 6. Validación de fechas
print("\n=== VALIDACIÓN DE FECHAS ===")

df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], errors="coerce"
)

print("Fechas de pedido inválidas:", df["Order Date"].isna().sum())
print("Fechas de envío inválidas:", df["Ship Date"].isna().sum())

fechas_invertidas = df["Ship Date"] < df["Order Date"]
print("Envíos anteriores al pedido:", fechas_invertidas.sum())

# 7. Validación de identificadores
print("\n=== VALIDACIÓN DE IDENTIFICADORES ===")

print("Row ID únicos:", df["Row ID"].nunique())
print("Order ID únicos:", df["Order ID"].nunique())
print("Product ID únicos:", df["Product ID"].nunique())
print("Customer ID únicos:", df["Customer ID"].nunique())

# 8. Valores extremos
print("\n=== VALORES EXTREMOS ===")

print("Ventas superiores a 10 000:", (df["Sales"] > 10000).sum())
print("Beneficios inferiores a -1 000:", (df["Profit"] < -1000).sum())
print("Descuentos superiores al 50 %:", (df["Discount"] > 0.5).sum())



# 9. Exportar datos procesados
from pathlib import Path

output_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "Orders_clean.csv"
)

output_path.parent.mkdir(parents=True, exist_ok=True)

# Copiar el DataFrame para separar la preparación del original
df_clean = df.copy()

# Asegurar que las fechas estén en formato datetime
df_clean["Order Date"] = pd.to_datetime(
    df_clean["Order Date"], errors="raise"
)

df_clean["Ship Date"] = pd.to_datetime(
    df_clean["Ship Date"], errors="raise"
)

# Exportar sin el índice de pandas
df_clean.to_csv(output_path, index=False, date_format="%Y-%m-%d")

print("\n=== EXPORTACIÓN ===")
print(f"Archivo guardado en: {output_path}")
print(f"Filas exportadas: {len(df_clean)}")
