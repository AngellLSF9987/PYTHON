import random


paises_europa = {
    "España": "Madrid", "Francia": "París", "Alemania": "Berlín", "Italia": "Roma",
    "Reino Unido": "Londres", "Portugal": "Lisboa", "Grecia": "Atenas", "Suecia": "Estocolmo",
    "Noruega": "Oslo", "Finlandia": "Helsinki", "Bélgica": "Bruselas", "Países Bajos": "Ámsterdam",
    "Suiza": "Berna", "Austria": "Viena", "Dinamarca": "Copenhague", "Irlanda": "Dublín"
}

paises_america_norte = {
    "Estados Unidos": "Washington D.C.", "Canadá": "Ottawa", "México": "Ciudad de México"
}

paises_america_sur = {
    "Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Colombia": "Bogotá",
    "Perú": "Lima", "Bolivia" : "La Paz", "Chile": "Santiago de Chile"
}

paises_asia = {
    "China": "Pekín", "Japón": "Tokio", "India": "Nueva Delhi", "Corea del Sur": "Seúl"
}

paises_africa = {
    "Egipto": "El Cairo", "Sudáfrica": "Pretoria", "Nigeria": "Abuja", "Kenya": "Nairobi"
}

paises_oceania = {
    "Australia": "Canberra", "Nueva Zelanda": "Wellington", "Islas Fidji": "Suva"
}

paises_mundo = {**paises_europa, **paises_america_norte, **paises_america_sur, **paises_asia, **paises_africa, **paises_oceania}

def seleccionar_paises(opcion):
    """Seleccionar el diccinario de países según la opción del continente."""

    if opcion == "1":
        return paises_europa
    elif opcion == "2":
        return paises_america_norte
    elif opcion == "3":
        return paises_america_sur
    elif opcion == "4":
        return {**paises_america_norte, **paises_america_sur}
    elif opcion == "5":
        return paises_asia
    elif opcion == "6":
        return paises_africa
    elif opcion == "7":
        return paises_oceania
    elif opcion == "8":
        return paises_mundo
    
def adivinar_capitales(paises_capitales, num_users):
    """Juego donde el usuario adivina capitales de países europeos."""

    # Mezclar los países
    paises = list(paises_capitales.keys())
    random.shuffle(paises)

    print(f"\nJugadores: {num_users}. ¡Comienza el juego!\n")
    
    resultados = {f"Jugador {i+1}": {"aciertos":0, "errores":0} for i in range(num_users)}
    
    print("Adivina las capitales de los países europeos.\n")
    print("NORMAS A TENER EN CUENTA:\n 1. Deben estar correctamente escritos los países, es decir, teniendo en cuenta las tildes que pudieran existir en los nombres.\n 2. El juego no tiene en cuenta si se escribe en minúsculas o mayúsculas.\n 3. El juego tiene en cuenta los espacios.")
    
    total_paises = len(paises)

    # Iterar sobre los países en orden aleatorio

    for pais in paises:
        cap_correcta = paises_capitales[pais]
        
        for user in range(1, num_users + 1):
            respuesta = input(f"Jugador {user},¿Cuál es la capital de {pais}?\n")

            if respuesta.lower() == cap_correcta.lower():
                print("Acertaste!\n")

                resultados[f"Jugador {user}"]["aciertos"] += 1
        
            else:
                print(f"Ups! Incorrecto.\n")
                resultados[f"Jugador {user}"]["errores"] += 1
        
        # Mostrar la respueta correcta después de responder todos los jugadores.
        print(f"La capital de {pais} es {cap_correcta}.\n")

    print("\nJuego terminado.\nResultados finales:")
    
    for user, resultado in resultados.items():

        print(f"\nJugador{user} - Adivinaste: {resultado['aciertos']}.\n - Erraste: {resultado['errores']} de {total_paises} capitales.\n  ")
