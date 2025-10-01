# analysis.py
"""
Funciones para analizar datos económicos descargados
"""

import pandas as pd
from utils import mostrar_mensaje

def analizar_datos(df=None):
    """
    Realiza análisis básico sobre el DataFrame recibido.
    Si no se pasa un DataFrame, se genera uno de ejemplo.
    """
    if df is None or df.empty:
        mostrar_mensaje("error", "No se proporcionaron datos para analizar.")
        return

    mostrar_mensaje("info", "Iniciando análisis de datos...")

    # Limpieza básica
    df = df.dropna(subset=["valor"])
    df["año"] = df["año"].astype(int)
    df["valor"] = df["valor"].astype(float)

    # Estadísticas por país
    resumen = df.groupby("país")["valor"].agg(["mean", "min", "max"]).reset_index()
    resumen.columns = ["País", "Promedio", "Mínimo", "Máximo"]

    mostrar_mensaje("exito", "Análisis completado. Resumen por país:")
    print(resumen.to_string(index=False))

    # Visualización opcional
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        for pais in df["país"].unique():
            datos_pais = df[df["país"] == pais]
            plt.plot(datos_pais["año"], datos_pais["valor"], label=pais)

        plt.title("Evolución del indicador económico")
        plt.xlabel("Año")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except ImportError:
        mostrar_mensaje("info", "matplotlib no está instalado. Visualización omitida.")