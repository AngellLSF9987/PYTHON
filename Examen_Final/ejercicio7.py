def invertir_cadena(cadena):
    return cadena[::-1]

def main():
    cadena = input("Introduce una cadena:\n")
    cadena_invertida = invertir_cadena(cadena)

    print("Resultado Cadena Invertida:",cadena_invertida)

if __name__ == "__main__":
    main()