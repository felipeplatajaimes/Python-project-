# utils.py
"""
Funciones auxiliares para validación y retroalimentación
"""

def validar_opcion(opcion, opciones_validas):
    """
    Verifica si la opción ingresada es válida.
    Parámetros:
        opcion (str): entrada del usuario
        opciones_validas (list): lista de opciones permitidas (int)
    Retorna:
        bool: True si es válida, False si no
    """
    try:
        valor = int(opcion)
        return valor in opciones_validas
    except ValueError:
        return False

def validar_numero(valor, minimo=None, maximo=None):
    """
    Valida si el valor es un número dentro de un rango opcional.
    """
    try:
        numero = float(valor)
        if minimo is not None and numero < minimo:
            return False
        if maximo is not None and numero > maximo:
            return False
        return True
    except ValueError:
        return False

def mostrar_mensaje(tipo, texto):
    """
    Muestra mensajes estandarizados según el tipo.
    """
    tipos = {
        "error": "❌ ERROR:",
        "exito": "✅ ÉXITO:",
        "info": "ℹ️ INFO:"
    }
    encabezado = tipos.get(tipo, "🔔")
    print(f"{encabezado} {texto}")