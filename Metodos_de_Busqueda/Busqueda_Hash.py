"""
Ejercicio 3: BÚSQUEDA HASH
Directorio telefónico guardado en una tabla hash. La posición de cada contacto
se calcula a partir de su nombre con una función hash (suma de códigos ASCII
módulo el tamaño de la tabla). Cuando dos nombres caen en la misma posición
(colisión) se guardan en una lista dentro de esa posición (encadenamiento).
"""


class TablaHash:
    def __init__(self, tamano=7):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        clave = clave.strip().lower()
        return sum(ord(letra) for letra in clave) % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        clave = clave.strip().lower()
        for par in self.tabla[indice]:
            if par[0] == clave:      # si ya existe, solo se actualiza
                par[1] = valor
                return
        self.tabla[indice].append([clave, valor])

    def buscar(self, clave):
        """Regresa (valor, indice, comparaciones). El valor es None si no existe."""
        indice = self.funcion_hash(clave)
        clave = clave.strip().lower()
        comparaciones = 0
        for par in self.tabla[indice]:
            comparaciones += 1
            if par[0] == clave:
                return par[1], indice, comparaciones
        return None, indice, comparaciones

    def mostrar(self):
        for i, cadena in enumerate(self.tabla):
            contenido = " -> ".join(f"{c.title()} ({v})" for c, v in cadena) if cadena else "vacía"
            print(f"  [{i}] {contenido}")


CONTACTOS = [
    ("Ana", "999-111-2201"),
    ("Luis", "999-222-3302"),
    ("Marta", "999-333-4403"),
    ("Diego", "999-444-5504"),
    ("Carla", "999-555-6605"),
    ("Jorge", "999-666-7706"),
    ("Lucía", "999-777-8807"),
    ("Pedro", "999-888-9908"),
]


def crear_directorio():
    directorio = TablaHash(7)
    for nombre, telefono in CONTACTOS:
        directorio.insertar(nombre, telefono)
    return directorio


def ejecutar():
    print("\n=== BÚSQUEDA HASH ===")
    directorio = crear_directorio()
    print(f"Tabla hash (tamaño {directorio.tamano}, función: suma ASCII mod {directorio.tamano}):")
    directorio.mostrar()
    while True:
        nombre = input("\nNombre del contacto a buscar: ")
        telefono, indice, comparaciones = directorio.buscar(nombre)
        print(f"Posición calculada por la función hash: {indice}")
        if telefono is None:
            print(f"Resultado: '{nombre.strip()}' NO está en el directorio.")
        else:
            print(f"Resultado: teléfono de {nombre.strip().title()}: {telefono}")
        print(f"Comparaciones realizadas dentro de la posición: {comparaciones}")
        if input("¿Buscar otro? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    ejecutar()
