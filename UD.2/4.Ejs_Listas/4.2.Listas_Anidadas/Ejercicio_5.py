"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 5:
A. Crear una matriz de 3x3 utilizando listas anidadas y mostrarlo por pantalla.

        # Crear una matriz de 3x3 utilizando listas anidadas

                        matriz = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                        ]

        # Mostrar la matriz por pantalla

                        print("La matriz de 3x3 es:")
                        for fila in matriz:
                        print(fila)
                        
B. Acceder al elemento 1,2 de la matriz y mostrarlo por pantalla.

        # Acceder al elemento en la fila 1, columna 2 (recordando que los índices empiezan en 0)
        
                        elemento_1_2 = matriz[1][2]

C. Imprimir todos los elementos de una lista anidada.

        # Imprimir todos los elementos de la lista anidada

                        print("Todos los elementos de la matriz son:")
                                for fila in matriz:
                                        for elemento in fila:
                                                print(elemento, end=" ")
                                print()  # Para crear un salto de línea después de cada fila\n""")

# A. Crear una matriz de 3x3 utilizando listas anidadas y mostrarlo por pantalla.

        # Crear una matriz de 3x3 utilizando listas anidadas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

        # Mostrar la matriz por pantalla

print("La matriz de 3x3 es:")
for fila in matriz:
    print(fila)
    
# B. Acceder al elemento 1,2 de la matriz y mostrarlo por pantalla.

        # Acceder al elemento en la fila 1, columna 2 (recordando que los índices empiezan en 0)
        
elemento_1_2 = matriz[1][2]

        # Mostrar el elemento por pantalla
        
print(f"El elemento en la posición 1,2 es: {elemento_1_2}")

# C. Imprimir todos los elementos de una lista anidada.

        # Imprimir todos los elementos de la lista anidada

print("Todos los elementos de la matriz son:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Para crear un salto de línea después de cada fila


