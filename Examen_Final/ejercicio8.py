import random

def generar_numero_aleatorio():
    """Genero un número aleatorio entre 1 y 10."""

    return random.randint(1,10)

def pedir_numero():
    while True:
        """Piede un núimero entero al usuario y lo devuelve"""
        num = int(input("Introduce un número entre 1 y 10:\n"))

        if 1 <= num <= 10:
            return num
        else:
            print("Introduce un número válido entre 1 y 10.")

def comprobar_coincidencia(num_random, num_user):
    """Compara si los números coinciden"""

    if num_random == num_user:
        print("Coinciden!")
    else:
        print(f"No hay coincidencia. El número aleatorio era: {num_random}")

def main():
    num_random = generar_numero_aleatorio()
    num_user = pedir_numero()
    comprobar_coincidencia(num_random,num_user)

if __name__ == "__main__":
    main()