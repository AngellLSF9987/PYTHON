"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 2:
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Crear una lista vacía para almacenar los números ganadores
    
    ganadores = []

# Pedir al usuario los números ganadores

    for i in range(6):  # La lotería primitiva tiene 6 números
        numero = int(input(f"Introduce el número ganador {i + 1}: "))
        ganadores.append(numero)


# Ordenar la lista de números ganadores de menor a mayor

    ganadores.sort()


# Mostrar los números ganadores ordenados

print("Los números ganadores ordenados de menor a mayor son:", ganadores+".")\n""")

# Crear una lista vacía para almacenar los números ganadores

ganadores = []

# Pedir al usuario los números ganadores
for i in range(6):  # La lotería primitiva tiene 6 números
    numero = int(input(f"Introduce el número ganador {i + 1}: \n"))
    ganadores.append(numero)

# Ordenar la lista de números ganadores de menor a mayor
ganadores.sort()

# Mostrar los números ganadores ordenados
print("Los números ganadores ordenados de menor a mayor son:", ganadores+".\n")
