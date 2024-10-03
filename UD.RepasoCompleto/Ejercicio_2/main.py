from packages.functions import mostrar_tablas

def main():
    # Mostrarblas tablas de multiplicar del 1 al 10

    tablas = mostrar_tablas()

    for num, tabla in tablas.items():
        print(f"\nTabla del {num}:\n")

        for line in tabla:
            print(line)

if __name__ == "__main__":
    main()