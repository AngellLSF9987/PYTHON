import random

# Función para imprimir con bucle WHILE.

def imprimir_num_while():
    """- Función para imprimir con bucle WHILE."""
    num = 1

    while num < 11:
        print(num, end=" ")
        num +=1

# Función para imprimir con bucle FOR.

def imprimir_num_for():
    """- Función para imprimir con bucle FOR."""
    
    for num in range(1,11):
        print(num, end=" ")

# Función generar números aleatorios y rellenar listas de pares e impares

def rellenar():
    """- Función generar números aleatorios y rellenar listas de pares e impares."""

    num_pares = []
    num_impares = []

    for i in range(10):
        num = random.randint(1,50)

        if num % 2 == 0:
            num_pares.append(num)

        else:
            num_impares.append(num)

    return num_pares,num_impares

# Función para obtener los números impares que son mútiplos de 3.

def impares_multi_3(num_impares):
    """- Función para obtener los números impares que son mútiplos de 3."""
    multiplos_3 = [num for num in num_impares if num % 3 == 0]
    
    return multiplos_3

# Función para obtener los números pares que son menores de 25.

def pares_menores_25(num_pares):
    """- Función para obtener los números pares que son menores de 25."""
    menores_25 = [num for num in num_pares if num < 25]

    return menores_25

# Función para imprimir las listas de múltiplos de 3 que son impares y de números pares menores de 25.

def imprimir_listas(lista_multiplos, lista_menores):
    """- Función para imprimir las listas:
        - De múltiplos de 3 que son impares.
        - De números pares menores de 25."""
    print(f"\nMúltiplos de 3 de la lista de impares:{lista_multiplos}")
    print(f"\nLista números pares menores de 25:{lista_menores}")



