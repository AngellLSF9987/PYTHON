import random

# Crea una matriz 3x4 con nombres aleatorios de la lista de alumnos.
def matriz_alumnos(nombres):
    """Crea una matriz 3x4 con nombres aleatorios de la lista de alumnos."""

    # Crea una matriz vacía
    matriz_alumnos = [[None for col in range(4)] for row in range(3)]

    # Mezclar la lista de nombres
    random.shuffle(nombres)
    
    # Llenar la matriz con los nombres
    index = 0

    for row in range(3): # 3 Filas
        for col in range(4): # 4 Columnas
            if index < len(nombres):
                matriz_alumnos[row][col] = nombres[index]
                index += 1

            else:
                matriz_alumnos[row][col] = None # Rellenar con None si no hay más nombres

    return matriz_alumnos

# Función imprimir la matriz en formato tabla.

def imprimir(matriz):
    """Función imprimir la matriz en formato tabla."""

    for row in matriz:
        for nombre in row:
            print(nombre, end=" | ") # Imprime cada nombre seguido de " | "
        print()


