"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 2:
Escribir un programa que almacene en una lista con 10 números y los ordene de
mayor a menor.

# Crear una lista vacía para almacenar los números
    
    numeros = []

# Pedir al usuario que introduzca 10 números

    for i in range(10):
        numero = int(input(f"Introduce el número {i + 1}: "))
        numeros.append(numero)

# Ordenar la lista de números de mayor a menor

    numeros.sort(reverse=True)

# Mostrar los números ordenados de mayor a menor

    print("Los números ordenados de mayor a menor son:", numeros+".\n")\n""")

# Crear una lista vacía para almacenar los números
    
numeros = []

# Pedir al usuario que introduzca 10 números

for i in range(10):
        numero = int(input(f"Introduce el número {i + 1}: "))
        numeros.append(numero)

# Ordenar la lista de números de mayor a menor

#numeros.reverse()
numeros.sort(reverse=True)

# Mostrar los números ordenados de mayor a menor

print("Los números ordenados de mayor a menor son:", numeros,".\n")

# Ordenar la lista de números de menor a mayor

numeros.sort()

# Mostrar los números ordenados de menor a mayor

print("Los números ordenados de menor a mayor son:", numeros,".\n")