from packages.functions import imprimir_num_while, imprimir_num_for, rellenar, impares_multi_3, pares_menores_25, imprimir_listas


def main():
    # Mostrar los 10 primeros números con bucle WHILE
    print("Números naturales con bucle WHILE:")

    imprimir_num_while()

    # Mostrar los 10 primeros números con bucle FOR
    print("\nNúmeros naturales con bucle FOR:")

    imprimir_num_for()

    # Rellenar listas de números pares e impares con números aleatorios
    num_pares, num_impares = rellenar()
    print(f"\nLista de números pares: {num_pares}")
    print(f"\nLista de números impares: {num_impares}")

    # Procesar listas

    multiplos_3 = impares_multi_3(num_impares)
    menores_25 = pares_menores_25(num_pares)

    # Imprimir listas

    imprimir_listas(multiplos_3,menores_25)

# Ejecutar el programa

if __name__ == "__main__":
    main()