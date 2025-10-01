#  Proyecto de Análisis Económico con Python

**Segundo corte – Curso de programación**  
**Autor:** Edgar Felipe Plata Jaimes  
**Fecha de entrega:** 3 de Octubre de 2025  
**Tema:** Análisis del PIB per cápita en América Latina (Colombia, México y Brasil)  
**Fuente de datos:** API del Banco Mundial

---

##  Objetivo del proyecto

Desarrollar un programa en Python que permita descargar, procesar y analizar datos económicos reales, aplicando los conceptos vistos en clase. El análisis se enfoca en la evolución del PIB per cápita en tres países latinoamericanos entre 2010 y 2022.

---

## Estructura del proyecto
economic_analysis_project/
│
├── main.py           # Menú interactivo y flujo principal
├── utils.py          # Validaciones y mensajes
├── data_loader.py    # Descarga de datos desde la API del Banco Mundial
├── analysis.py       # Procesamiento y visualización de datos
├── config.py         # Parámetros globales del análisis
└── README.md         # Documentación del proyecto


---

## Tecnologías utilizadas

- Librerías: `requests`, `pandas`, `matplotlib`
- API del Banco Mundial (World Bank Open Data)

---

##  Qué se implementó y para qué

| Componente                           | Implementación                     | Propósito                                         |
| Menú interactivo (`main.py`)         | Uso de `input()` y validación      | Guiar al usuario paso a paso                      |
| Validación (`utils.py`)              | Funciones como `validar_opcion()`  | Evitar errores por entradas incorrectas           |
| Descarga de datos (`data_loader.py`) | Conexión a API + manejo de errores | Obtener datos reales y confiables                 |
| Análisis (`analysis.py`)             | Agrupación, estadísticas, gráficos | Interpretar los datos y visualizar tendencias     |
| Configuración (`config.py`)          | Parámetros globales                | Facilitar cambios sin modificar el código         |
| Documentación (`README.md`)          | Explicación clara del proyecto     | Cumplir criterios de presentación y planificación |

---

## Criterios cumplidos según la rúbrica

### Interfaz de Usuario

- **IU1 – Uso apropiado de comentarios y formatos**  
  El código incluye comentarios explicativos en cada módulo y función, facilitando su comprensión.

- **IU2 – Interfaz intuitiva e instrucciones claras**  
  El programa presenta un menú interactivo con instrucciones visibles y opciones claras para el usuario.

- **IU3 – La entrada del usuario es validada**  
  Se implementan funciones específicas para validar las entradas del usuario, evitando errores comunes.

---

### Funcionalidad

- **F1 – El programa resuelve todos los aspectos del problema**  
  El programa descarga datos reales desde la API del Banco Mundial, los procesa y genera un análisis económico útil.

- **F2 – El programa no tiene errores**  
  El código se ejecuta correctamente, con manejo de errores y estructura modular que facilita su mantenimiento.

---

###  Entrega Final

- **EF1 – Planificación**  
  El proyecto está organizado en módulos funcionales y cuenta con un archivo de configuración que centraliza los parámetros del análisis.

- **EF2 – Presentación**  
  Se incluye un archivo `README.md` que documenta el propósito, la estructura y el uso del programa de forma clara y completa.

- **EF3 – Respuesta a preguntas**  
  El código está diseñado para ser explicable en el quiz, con funciones bien nombradas, lógica sencilla y trazabilidad entre módulos.

---

##  Referencias

- [World Bank API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- Documentación oficial de `pandas` y `matplotlib`
## Instalación de dependencias
Para que el proyecto funcione correctamente, necesitas instalar las siguientes librerías de Python:
en gitbash 
pip install pandas requests matplotlib
luego 
pip install -r requirements.txt
