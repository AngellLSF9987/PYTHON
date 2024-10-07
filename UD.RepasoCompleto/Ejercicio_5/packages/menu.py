def mostrar_menu():
    """Mostrar el menú para seleccionar continente y número de jugadores."""

    print("¡Bienvenido al juego ADIVINA CAPITALES DE PAÍSES!")

    # Menú de Continentes

    print("Selecciona el continente o área para jugar:")
    print("1. Europa.")
    print("2. América del Norte.")
    print("3. América del Sur.")
    print("4. América (Norte y Sur).")
    print("5. Asia")
    print("6. África")
    print("7. Oceanía.")
    print("8. Todo el mundo.")

    opcion = input("Introduce el número de opción elegida para jugar:\n")

    if opcion == "0":
        print("Cerrando el juego...¡Hasta pronto!")
        exit() # Cerrar el programa

    # Menú para seleccionar número de jugadores

    while True:
        try:
            numero_jugadores = int(input("¿Cuántos jugadores van a jugar?:\n"))
            if numero_jugadores > 0:
                break
            else:
                print("El número de jugadores debe ser mayor que 0.")
        except ValueError:
            print("Introduce un número válido.")

    return opcion, numero_jugadores
