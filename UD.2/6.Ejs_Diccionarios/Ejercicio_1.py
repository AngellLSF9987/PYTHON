"""
        >>>>>>>    Ejercicios Diccionarios   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Diccionarios   <<<<<<")                                                            
print (f"\n","Ejercicio 1: \n")
print ("""

A. Crear un diccionario para representar un inventario de una frutería.

    Ej.: Manzanas = 3, Peras = 4, Naranjas = 8

B. Acceder a un valor específico de Peras.

C. Agregar un nuevo elemento.

D. Modificar un valor existente.

E. Mostrar las claves del inventario. (Nombres de la fruta)

F. Mostrar los valores del inventario. (Cantidad de fruta)

G. Mostrar el inventario completo, nombres y cantidad.

H. Verificar la existencia de uvas en el inventario.\n""")

print ("""

# A. Crear un diccionario para representar un inventario de una frutería.

        inventario = {
            "Manzanas": 3,
            "Peras": 4,
            "Naranjas": 8
        } 

# B. Acceder a un valor específico de Peras.

        nPeras = inventario["Peras"]
        print(f"Stock peras: {nPeras}.\n")

# C. Agregar un nuevo elemento.

        inventario["Uvas"] = 10
        nUvas = inventario["Uvas"]
        print(f"Se han añadido al stock {nUvas} uvas.\n")

# D. Modificar un valor existente.

        inventario["Manzanas"] = 6
        nManzanas = inventario["Manzanas"]
        print(f"Se ha modificado la cantidad en stock de manzanas a {nManzanas}.\n")

# E. Mostrar las claves del inventario. (Nombres de la fruta)

        print(f"El inventario de frutas existente es:\n {list(inventario.keys())}.\n")

# F. Mostrar los valores del inventario. (Cantidad de fruta)

        print(f"La cantidad de unidades por fruta existente es:\n {list(inventario.values())}.\n")

# G. Mostrar el inventario completo, nombres y cantidad.

        print("Inventario completo:")
        for fruta, cantidad in inventario.items():
            print (f"{fruta}: {cantidad}.")

        print()

# H. Verificar la existencia de uvas en el inventario.

        if "Uvas" in inventario:
            print("Las uvas están en el inventario.\n")
        else:
            print("Las uvas no están en el inventario.\n")\n\n""")

# A. Crear un diccionario para representar un inventario de una frutería.

inventario = {
    "Manzanas": 3,
    "Peras": 4,
    "Naranjas": 8
} 

# B. Acceder a un valor específico de Peras.

nPeras = inventario["Peras"]
print(f"Stock peras: {nPeras}.\n")

# C. Agregar un nuevo elemento.

inventario["Uvas"] = 10
nUvas = inventario["Uvas"]
print(f"Se han añadido al stock {nUvas} uvas.\n")

# D. Modificar un valor existente.

inventario["Manzanas"] = 6
nManzanas = inventario["Manzanas"]
print(f"Se ha modificado la cantidad en stock de manzanas a {nManzanas}.\n")

# E. Mostrar las claves del inventario. (Nombres de la fruta)

print(f"El inventario de frutas existente es:\n {list(inventario.keys())}.\n")

# F. Mostrar los valores del inventario. (Cantidad de fruta)

print(f"La cantidad de unidades por fruta existente es:\n {list(inventario.values())}.\n")

# G. Mostrar el inventario completo, nombres y cantidad.

print("Inventario completo:")
for fruta, cantidad in inventario.items():
    print (f"{fruta}: {cantidad}.")

print()

# H. Verificar la existencia de uvas en el inventario.

if "Uvas" in inventario:
    print("Las uvas están en el inventario.\n")
else:
    print("Las uvas no están en el inventario.\n")