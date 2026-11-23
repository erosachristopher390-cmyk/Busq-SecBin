# Métodos de Búsqueda

Tres ejercicios en Python que aplican los métodos de búsqueda **Secuencial**, **Binaria** y **Hash**, y un programa con menú que permite ejecutar los tres. Cada programa muestra paso a paso cómo se realiza la búsqueda y cuántas comparaciones hace.

Trabajo de la materia de **Estructura de datos**, grupo 3SA, Ingeniería en Sistemas Computacionales, Instituto Tecnológico de Mérida (TecNM).

## Contenido

| Archivo | Método | Ejercicio |
| --- | --- | --- |
| [`Busqueda_Secuencial.py`](Busqueda_Secuencial.py) | Búsqueda secuencial | Busca un producto por código en un inventario de 8 productos sin ordenar |
| [`Busqueda_Binaria.py`](Busqueda_Binaria.py) | Búsqueda binaria | Busca una matrícula en una lista ordenada de 12 alumnos |
| [`Busqueda_Hash.py`](Busqueda_Hash.py) | Búsqueda hash | Busca un contacto por nombre en un directorio telefónico guardado en una tabla hash |
| [`Menu_Busqueda.py`](Menu_Busqueda.py) | Menú | Ejecuta los tres métodos desde un solo programa |

## Requisitos

- Python 3.8 o superior
- No requiere instalar librerías externas

## Cómo ejecutarlos

Desde la carpeta del repositorio, el programa con menú:

```bash
python Menu_Busqueda.py
```

También se puede ejecutar cada ejercicio por separado:

```bash
python Busqueda_Secuencial.py
python Busqueda_Binaria.py
python Busqueda_Hash.py
```

En algunos sistemas el comando es `python3` en lugar de `python`.

> `Menu_Busqueda.py` importa los otros tres archivos, así que los cuatro deben estar en la misma carpeta y conservar su nombre.

## Descripción de cada método

### 1. Búsqueda secuencial

Revisa la lista elemento por elemento, desde el primero, hasta encontrar la clave buscada o llegar al final. No necesita que los datos estén ordenados.

- Complejidad: O(n) en el caso promedio y en el peor caso.
- Es la opción adecuada para listas pequeñas o sin orden.

### 2. Búsqueda binaria

Compara la clave con el elemento del centro de la lista y descarta la mitad donde ya no puede estar, repitiendo el proceso con la mitad restante. **Requiere que la lista esté ordenada.**

- Complejidad: O(log n). Con 12 elementos nunca hace más de 4 comparaciones.

### 3. Búsqueda hash

Guarda los datos en una tabla donde la posición de cada clave se calcula con una función hash (aquí, la suma de los códigos ASCII del nombre módulo el tamaño de la tabla, que es 7). Las colisiones se resuelven con encadenamiento: cada posición guarda una lista con las claves que le tocaron.

- Complejidad: O(1) en promedio; O(n) en el peor caso, si todas las claves chocan en la misma posición.

## Comparativo

| Método | Condición para usarlo | Caso promedio | Peor caso |
| --- | --- | --- | --- |
| Secuencial | Ninguna, los datos pueden estar sin ordenar | O(n) | O(n) |
| Binaria | Lista ordenada con acceso directo por posición | O(log n) | O(log n) |
| Hash | Tabla construida con una función hash | O(1) | O(n) |

## Salida de ejemplo

<details>
<summary>Búsqueda secuencial</summary>

```text

=== BÚSQUEDA SECUENCIAL ===
Inventario (sin ordenar):
  1042  Cuaderno profesional
  2305  Lápiz del número 2
  1177  Calculadora científica
  3410  Memoria USB 32 GB
  2288  Juego de marcadores
  1890  Carpeta de argollas
  4021  Regla de 30 cm
  3099  Tijeras escolares

Código del producto a buscar: 3410
  Comparación 1: posición 0 -> 1042 (Cuaderno profesional)
  Comparación 2: posición 1 -> 2305 (Lápiz del número 2)
  Comparación 3: posición 2 -> 1177 (Calculadora científica)
  Comparación 4: posición 3 -> 3410 (Memoria USB 32 GB)
Resultado: Memoria USB 32 GB (posición 3).
Comparaciones realizadas: 4 de 8
¿Buscar otro? (s/n): s

Código del producto a buscar: 9999
  Comparación 1: posición 0 -> 1042 (Cuaderno profesional)
  Comparación 2: posición 1 -> 2305 (Lápiz del número 2)
  Comparación 3: posición 2 -> 1177 (Calculadora científica)
  Comparación 4: posición 3 -> 3410 (Memoria USB 32 GB)
  Comparación 5: posición 4 -> 2288 (Juego de marcadores)
  Comparación 6: posición 5 -> 1890 (Carpeta de argollas)
  Comparación 7: posición 6 -> 4021 (Regla de 30 cm)
  Comparación 8: posición 7 -> 3099 (Tijeras escolares)
Resultado: el código 9999 NO está en el inventario.
Comparaciones realizadas: 8 de 8
¿Buscar otro? (s/n): n
```

</details>

<details>
<summary>Búsqueda binaria</summary>

```text

=== BÚSQUEDA BINARIA ===
Alumnos (ordenados por matrícula):
  [ 0] 21080012  Ana Cetina
  [ 1] 21080037  Luis Pech
  [ 2] 21080055  Marta Canul
  [ 3] 21080064  Diego Chan
  [ 4] 21080081  Carla Euán
  [ 5] 21080093  Jorge May
  [ 6] 21080110  Lucía Tun
  [ 7] 21080126  Pedro Uc
  [ 8] 21080142  Sofía Be
  [ 9] 21080158  Raúl Dzul
  [10] 21080171  Elena Cob
  [11] 21080189  Mateo Poot

Matrícula a buscar: 21080126
  Paso 1: bajo=0, alto=11, medio=5 -> 21080093
  Paso 2: bajo=6, alto=11, medio=8 -> 21080142
  Paso 3: bajo=6, alto=7, medio=6 -> 21080110
  Paso 4: bajo=7, alto=7, medio=7 -> 21080126
Resultado: Pedro Uc (posición 7).
Comparaciones realizadas: 4 de 12 posibles en una búsqueda secuencial
¿Buscar otra? (s/n): s

Matrícula a buscar: 21080100
  Paso 1: bajo=0, alto=11, medio=5 -> 21080093
  Paso 2: bajo=6, alto=11, medio=8 -> 21080142
  Paso 3: bajo=6, alto=7, medio=6 -> 21080110
Resultado: la matrícula 21080100 NO está en la lista.
Comparaciones realizadas: 3 de 12 posibles en una búsqueda secuencial
¿Buscar otra? (s/n): n
```

</details>

<details>
<summary>Búsqueda hash</summary>

```text

=== BÚSQUEDA HASH ===
Tabla hash (tamaño 7, función: suma ASCII mod 7):
  [0] Lucía (999-777-8807)
  [1] Marta (999-333-4403)
  [2] Diego (999-444-5504)
  [3] Ana (999-111-2201) -> Jorge (999-666-7706)
  [4] Luis (999-222-3302) -> Carla (999-555-6605)
  [5] vacía
  [6] Pedro (999-888-9908)

Nombre del contacto a buscar: Diego
Posición calculada por la función hash: 2
Resultado: teléfono de Diego: 999-444-5504
Comparaciones realizadas dentro de la posición: 1
¿Buscar otro? (s/n): s

Nombre del contacto a buscar: Sofía
Posición calculada por la función hash: 4
Resultado: 'Sofía' NO está en el directorio.
Comparaciones realizadas dentro de la posición: 2
¿Buscar otro? (s/n): n
```

</details>

<details>
<summary>Programa con menú</summary>

```text

==============================
      MÉTODOS DE BÚSQUEDA
==============================
  1. Búsqueda secuencial
  2. Búsqueda binaria
  3. Búsqueda hash
  4. Salir
Elige una opción: 7
Opción no válida, elige un número del 1 al 4.

==============================
      MÉTODOS DE BÚSQUEDA
==============================
  1. Búsqueda secuencial
  2. Búsqueda binaria
  3. Búsqueda hash
  4. Salir
Elige una opción: 3

=== BÚSQUEDA HASH ===
Tabla hash (tamaño 7, función: suma ASCII mod 7):
  [0] Lucía (999-777-8807)
  [1] Marta (999-333-4403)
  [2] Diego (999-444-5504)
  [3] Ana (999-111-2201) -> Jorge (999-666-7706)
  [4] Luis (999-222-3302) -> Carla (999-555-6605)
  [5] vacía
  [6] Pedro (999-888-9908)

Nombre del contacto a buscar: Diego
Posición calculada por la función hash: 2
Resultado: teléfono de Diego: 999-444-5504
Comparaciones realizadas dentro de la posición: 1
¿Buscar otro? (s/n): n

==============================
      MÉTODOS DE BÚSQUEDA
==============================
  1. Búsqueda secuencial
  2. Búsqueda binaria
  3. Búsqueda hash
  4. Salir
Elige una opción: 4
Programa terminado.
```

</details>

## Autor

Arévalo Erosa Christopher Abraham
Ingeniería en Sistemas Computacionales, Instituto Tecnológico de Mérida
