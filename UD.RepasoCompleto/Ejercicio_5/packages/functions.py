import random

paises_capitales = {
    "España": "Madrid", "Francia": "París", "Alemania": "Berlín", "Italia": "Roma",
    "Reino Unido": "Londres", "Portugal": "Lisboa", "Grecia": "Atenas", "Suecia": "Estocolmo",
    "Noruega": "Oslo", "Finlandia": "Helsinki", "Bélgica": "Bruselas", "Países Bajos": "Ámsterdam",
    "Suiza": "Berna", "Austria": "Viena", "Dinamarca": "Copenhague", "Irlanda": "Dublín"
}

def adivinar_capitales():
    """Juego donde el usuario adivina capitales de países europeos."""

    # Mezclar los países
    paises = list(paises_capitales.keys())
    random.shuffle(paises)

    print("Adivina las capitales de los países europeos.\nSi quieres acabar la partida solo escribe < salir >")

    aciertos = 0
    errores = 0
    total_paises = len(paises)

    # Iterar sobre los países en orden aleatorio

    for pais in paises:
        
        respuesta = input(f"¿Cuál es la capital de {pais}?\n")
        
        # Verificar que el usuario no haya escrito "salir".
        if respuesta.lower() == "salir":
            print("\nJuego interrumpido. Has salido del juego.\n")
            break

        # Verificar que no se ha pulsado la tecla ESCAPE del teclado durante la pregunta.

        if respuesta.lower() == "salir":
            print("\nJuego interrumpido. Has salido del juego.\n")
            break

        # Verificar respuesta
        
        elif respuesta.lower() == paises_capitales[pais].lower():
            print("Acertaste!")

            aciertos += 1
        
        else:
            print(f"Ups! Incorrecto. La Capital de {pais} es {paises_capitales[pais]}.\n")
            errores += 1
    
    print(f"\nJuego terminado. Adivinaste: {aciertos}. Erraste: {errores} de {total_paises} capitales.\n  ")
