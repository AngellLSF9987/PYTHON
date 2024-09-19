"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 8:
Crear una lista con las primeras letras de una está lista: palabras = ["manzana",
"banana", "cereza"]

# Lista de palabras
palabras = ["manzana", "banana", "cereza"]

# Crear una lista con las primeras letras de cada palabra
iniciales = [palabra[0] for palabra in palabras]

# Mostrar la lista de primeras letras
print("Las primeras letras de las palabras son:", iniciales+".")

# Otra forma Crear una lista con las primeras letras de cada palabra

iniciales = [i[0] for i in range palabras]
print(f"Las primeras letras de las palabras son:", iniciales,".\n")\n""")

# Lista de palabras
palabras = ["manzana", "banana", "cereza"]

# Crear una lista con las primeras letras de cada palabra
iniciales = [palabra[0] for palabra in palabras]

# Mostrar la lista de primeras letras
print(f"Las primeras letras de las palabras son:", iniciales,".\n")

# Otra forma Crear una lista con las primeras letras de cada palabra

iniciales = [i[0] for i in palabras]
print(f"Las primeras letras de las palabras son:", iniciales,".\n")