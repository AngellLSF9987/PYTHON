import random

# Función para generar el número aleatorio.
def generar():
    """- Se usa random.randint para generar un número aleatorio entre 1 y 20."""
    return random.randint(1,20)

# Función solicitar número.
def obtener():
    """- Solicita al usuario que ingrese un número."""
    return int(input("Adivina el número entre 1 y 20:"))

# Función comparar número mágico y número dado por el usuario.
def comparar(num_user,num_magic):
    """- Indica si el número es menor, mayor o si el usuario acertó."""
    if num_user < num_magic:
        print("El número buscado es mayor.\n")
    elif num_user > num_magic:
        print("El número buscado es menor.")
    else:
        print("¡Genial! ¡Acertaste!")
