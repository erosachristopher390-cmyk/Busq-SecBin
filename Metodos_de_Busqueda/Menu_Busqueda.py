"""
Programa con menú que permite ejecutar los 3 métodos de búsqueda:
Secuencial, Binaria y Hash. Los tres archivos de los ejercicios deben estar en
la misma carpeta que este programa.
"""

import Busqueda_Secuencial
import Busqueda_Binaria
import Busqueda_Hash


def mostrar_menu():
    print("\n==============================")
    print("      MÉTODOS DE BÚSQUEDA")
    print("==============================")
    print("  1. Búsqueda secuencial")
    print("  2. Búsqueda binaria")
    print("  3. Búsqueda hash")
    print("  4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            Busqueda_Secuencial.ejecutar()
        elif opcion == "2":
            Busqueda_Binaria.ejecutar()
        elif opcion == "3":
            Busqueda_Hash.ejecutar()
        elif opcion == "4":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida, elige un número del 1 al 4.")


if __name__ == "__main__":
    main()
