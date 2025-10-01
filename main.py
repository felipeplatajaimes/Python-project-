# main.py

from data_loader import descargar_datos
from analysis import analizar_datos
from utils import validar_opcion

def mostrar_menu():
    print("\n📊 Bienvenido al Analizador Económico")
    print("1. Descargar datos")
    print("2. Analizar datos")
    print("3. Salir")

def main():
    datos = None  # Variable para guardar el DataFrame

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if not validar_opcion(opcion, [1, 2, 3]):
            print("❌ Opción inválida. Intente de nuevo.")
            continue

        opcion = int(opcion)
        if opcion == 1:
            datos = descargar_datos()  # Guardar los datos descargados
        elif opcion == 2:
            analizar_datos(datos)  # Pasar los datos al análisis
        elif opcion == 3:
            print("👋 Gracias por usar el programa. Hasta pronto.")
            break

if __name__ == "__main__":
    main()