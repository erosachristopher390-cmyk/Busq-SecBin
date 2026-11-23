"""
Ejercicio 1: BÚSQUEDA SECUENCIAL
Una papelería tiene su inventario en una lista SIN ordenar (código, producto).
El programa busca un producto por su código revisando uno por uno desde el
principio, hasta encontrarlo o llegar al final de la lista.
"""

INVENTARIO = [
    (1042, "Cuaderno profesional"),
    (2305, "Lápiz del número 2"),
    (1177, "Calculadora científica"),
    (3410, "Memoria USB 32 GB"),
    (2288, "Juego de marcadores"),
    (1890, "Carpeta de argollas"),
    (4021, "Regla de 30 cm"),
    (3099, "Tijeras escolares"),
]


def buscar_secuencial(lista, codigo, mostrar_pasos=True):
    """Regresa (posicion, comparaciones). La posición es -1 si no se encuentra."""
    comparaciones = 0
    for i, (cod, producto) in enumerate(lista):
        comparaciones += 1
        if mostrar_pasos:
            print(f"  Comparación {comparaciones}: posición {i} -> {cod} ({producto})")
        if cod == codigo:
            return i, comparaciones
    return -1, comparaciones


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Escribe un número entero válido.")


def ejecutar():
    print("\n=== BÚSQUEDA SECUENCIAL ===")
    print("Inventario (sin ordenar):")
    for cod, producto in INVENTARIO:
        print(f"  {cod}  {producto}")
    while True:
        codigo = pedir_entero("\nCódigo del producto a buscar: ")
        posicion, comparaciones = buscar_secuencial(INVENTARIO, codigo)
        if posicion == -1:
            print(f"Resultado: el código {codigo} NO está en el inventario.")
        else:
            print(f"Resultado: {INVENTARIO[posicion][1]} (posición {posicion}).")
        print(f"Comparaciones realizadas: {comparaciones} de {len(INVENTARIO)}")
        if input("¿Buscar otro? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    ejecutar()
