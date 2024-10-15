def main():
    comida = "Huevo"

    lista_comida = [comida, "Leche", "Azúcar"]


    print("Elementos de la lista:\n")

    for item in lista_comida:
        print(item)

        print("\nPosición y elemento en la lista:")
        for index, item in enumerate(lista_comida):
            print(f"Posición {index}: {item}")


if __name__ == "__main__":
    main()