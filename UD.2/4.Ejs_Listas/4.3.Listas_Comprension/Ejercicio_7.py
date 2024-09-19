"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 7:
Crear una lista con los primeros 10 números pares.

# Crear una lista con los primeros 10 números pares
        
        pares = []

# Generar los primeros 10 números pares

        for i in range(10):
        par = 2 * i
        pares.append(par)

# Mostrar la lista de números pares
        print("Los primeros 10 números pares son:", numeros_pares, end = " ")
        
# Crear una lista con los primeros 10 números pares.

        pares = [i*2 i for in range (1,11)]
        print("Los primeros 10 números pares son:",pares, end = " ")\n""")

# Crear una lista con los primeros 10 números pares
pares = []

# Generar los primeros 10 números pares
for i in range(1,11):
    par = 2 * i
    pares.append(par)

# Mostrar la lista de números pares
print("Los primeros 10 números pares son:", pares, end = " "+".\n")

# Crear una lista con los primeros 10 números pares.

pares = [i*2 for i in range (1,11)]
print("Los primeros 10 números pares son:",pares, end = " "+".\n")
