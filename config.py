# config.py
"""
Configuración global del proyecto de análisis económico
"""

# Indicador económico a analizar
# Ejemplo: PIB per cápita (World Bank code: NY.GDP.PCAP.CD)
INDICADOR = "NY.GDP.PCAP.CD"

# Lista de países por código ISO
# Ejemplo: Colombia (CO), México (MX), Brasil (BR)
PAISES = ["CO", "MX", "BR"]

# Rango de años para el análisis
ANIO_INICIO = 2010
ANIO_FIN = 2022

# Título del proyecto (para visualizaciones y presentación)
TITULO_PROYECTO = "Análisis del PIB per cápita en América Latina"

# Autor/es del proyecto
AUTORES = ["Nicolás Ardila Rosas"]