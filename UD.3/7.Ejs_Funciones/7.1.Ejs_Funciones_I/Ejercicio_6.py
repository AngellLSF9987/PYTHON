"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 6: \n")
print ("""
Crear un programa que le diga al usuario que ingrese un número entero
e informar si es primo o no.                                            

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: \n"))

# Verificar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")           \n""")

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: \n"))

# Verificar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

