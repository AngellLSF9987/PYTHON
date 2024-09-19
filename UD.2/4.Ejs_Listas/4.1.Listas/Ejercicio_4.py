"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 2:
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# Lista de precios

    precios = [50, 75, 46, 22, 80, 65, 8]

# Encontrar el precio menor y mayor usando las funciones min() y max()

    menor = min(precios)
    mayor = max(precios)

# Mostrar el precio menor y el precio mayor
print(f"El precio menor es: {menor}"+".")
print(f"El precio mayor es: {mayor}"+".\n")\n""")

# Lista de precios
precios = [50, 75, 46, 22, 80, 65, 8]

# Encontrar el precio menor y mayor usando las funciones min() y max()
precio_menor = min(precios)
precio_mayor = max(precios)

# Mostrar el precio menor y el precio mayor
print(f"El precio menor es: {precio_menor}.")
print(f"El precio mayor es: {precio_mayor}.")



# Lista de precios
precios = [50, 75, 46, 22, 80, 65, 8]

# Encontrar el precio menor y mayor usando sort()

precios.sort()
#print(precios[0])
#print(precios[-1])

num = len(precios)
print(f"El precio menor es: {precios[0]}.")
print(f"El precio mayor es: {precios[-1]}.")