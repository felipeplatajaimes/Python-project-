# data_loader.py
"""
Módulo para descargar datos económicos desde la API del Banco Mundial
"""

import requests
import pandas as pd
from utils import mostrar_mensaje

def descargar_datos(indicador="NY.GDP.PCAP.CD", paises=["CO", "MX", "BR"], anio_inicio=2010, anio_fin=2022):
    """
    Descarga datos del Banco Mundial para un indicador y lista de países.
    Parámetros:
        indicador (str): código del indicador (ej. PIB per cápita)
        paises (list): códigos ISO de países
        anio_inicio (int): año inicial
        anio_fin (int): año final
    Retorna:
        DataFrame con los datos descargados
    """
    mostrar_mensaje("info", f"Descargando datos de {indicador} para países: {', '.join(paises)}")

    base_url = "http://api.worldbank.org/v2/country/{}/indicator/{}?date={}:{}&format=json&per_page=1000"
    datos = []

    for pais in paises:
        url = base_url.format(pais, indicador, anio_inicio, anio_fin)
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            json_data = respuesta.json()

            if len(json_data) < 2:
                mostrar_mensaje("error", f"No se encontraron datos para {pais}")
                continue

            for entrada in json_data[1]:
                datos.append({
                    "país": entrada["country"]["value"],
                    "año": entrada["date"],
                    "valor": entrada["value"]
                })

        except Exception as e:
            mostrar_mensaje("error", f"Error al descargar datos de {pais}: {e}")

    df = pd.DataFrame(datos)
    mostrar_mensaje("exito", f"Datos descargados correctamente: {len(df)} registros")
    return df