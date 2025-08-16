# kpis_ventas.py
from consultas import obtener_ventas_por_region, obtener_pedidos_categoria, obtener_productos_mayor_margen
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generar_graficos():
    """
    Genera gráficos de ventas por región y número de pedidos por categoría.
    """
    # Obtener datos desde consultas.py
    ventas_por_region = obtener_ventas_por_region()
    pedidos_categoria = obtener_pedidos_categoria()
    productos_mayor_margen= obtener_productos_mayor_margen()

    # Crear carpeta images si no existe
    os.makedirs('images', exist_ok=True)


    # Gráfico: Ventas por región
    fig1 = plt.figure()
    sns.barplot(data=ventas_por_region, x="Region", y="Total_Ventas")
    plt.title("Ventas Totales por Región")
    plt.savefig('images/ventas_por_region.png', dpi=300, bbox_inches='tight')

    # Gráfico: Número de pedidos por categoría
    fig2 = plt.figure()
    sns.barplot(data=pedidos_categoria, x="Category", y="Numero_Pedidos")
    plt.title("Número de Pedidos por Categoría")
    plt.savefig('images/numero_pedidos_categorias.png', dpi=300, bbox_inches='tight')

    # Gráfico: Número de pedidos por categorías
    fig3 = plt.figure(figsize=(6,4))
    sns.barplot(
        data=productos_mayor_margen,
        x="Total_Profit",
        y="Product Name"
    )
    plt.title("Top 5 productos con mayor margen")
    plt.xlabel("Margen total ($)")
    plt.ylabel("Producto")
    plt.tight_layout()
    plt.savefig('images/productos_mayor_margen.png', dpi=300, bbox_inches='tight')

    plt.show(block=True)

if __name__ == "__main__":
    generar_graficos()