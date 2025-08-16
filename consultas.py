import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Cargar dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding='latin1')

# Crear motor SQLite (archivo local)
engine = create_engine("sqlite:///superstore.db")

# Guardar el DataFrame como tabla SQL
df.to_sql("ventas", con=engine, if_exists="replace", index=False)

print("Realizando consultas")

# Consulta 1: Ventas por región
def obtener_ventas_por_region():
    engine = create_engine("sqlite:///superstore.db")
    query = """
    SELECT Region, SUM(Sales) as Total_Ventas
    FROM ventas
    GROUP BY Region
    ORDER BY Total_Ventas DESC
    """
    return pd.read_sql(query, engine)


# Consulta 2: Producto con mayor margen
def obtener_productos_mayor_margen():
    query = """
    SELECT "Product Name", SUM(Profit) as Total_Profit
    FROM ventas
    GROUP BY "Product Name"
    ORDER BY Total_Profit DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# Consulta 3: Pedidos por categoría
def obtener_pedidos_categoria():
    query = """
    SELECT Category, COUNT("Order ID") as Numero_Pedidos
    FROM ventas
    GROUP BY Category
    """
    return pd.read_sql(query, engine)
