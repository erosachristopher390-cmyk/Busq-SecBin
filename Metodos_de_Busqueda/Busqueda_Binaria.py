"""
Ejercicio 2: BÚSQUEDA BINARIA
La lista de alumnos está ORDENADA por matrícula. El programa busca una matrícula
comparándola con el elemento del centro y descartando en cada paso la mitad de
la lista donde ya no puede estar.
"""

ALUMNOS = [
    (21080012, "Ana Cetina"),
    (21080037, "Luis Pech"),
    (21080055, "Marta Canul"),
    (21080064, "Diego Chan"),
    (21080081, "Carla Euán"),
    (21080093, "Jorge May"),
    (21080110, "Lucía Tun"),
    (21080126, "Pedro Uc"),
    (21080142, "Sofía Be"),
    (21080158, "Raúl Dzul"),
    (21080171, "Elena Cob"),
    (21080189, "Mateo Poot"),
]


def buscar_binaria(lista, matricula, mostrar_pasos=True):
    """Regresa (posicion, comparaciones). La lista debe estar ordenada."""
    bajo = 0
    alto = len(lista) - 1
    comparaciones = 0
    while bajo <= alto:
        medio = (bajo + alto) // 2
        comparaciones += 1
        actual = lista[medio][0]
        if mostrar_pasos:
            print(f"  Paso {comparaciones}: bajo={bajo}, alto={alto}, medio={medio} -> {actual}")
        if actual == matricula:
            return medio, comparaciones
        if matricula < actual:
            alto = medio - 1   # se descarta la mitad derecha
        else:
            bajo = medio + 1   # se descarta la mitad izquierda
    return -1, comparaciones


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Escribe un número entero válido.")


def ejecutar():
    print("\n=== BÚSQUEDA BINARIA ===")
    print("Alumnos (ordenados por matrícula):")
    for i, (mat, nombre) in enumerate(ALUMNOS):
        print(f"  [{i:2}] {mat}  {nombre}")
    while True:
        matricula = pedir_entero("\nMatrícula a buscar: ")
        posicion, comparaciones = buscar_binaria(ALUMNOS, matricula)
        if posicion == -1:
            print(f"Resultado: la matrícula {matricula} NO está en la lista.")
        else:
            print(f"Resultado: {ALUMNOS[posicion][1]} (posición {posicion}).")
        print(f"Comparaciones realizadas: {comparaciones} de {len(ALUMNOS)} posibles en una búsqueda secuencial")
        if input("¿Buscar otra? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    ejecutar()
