from packages.functions import *

def main ():
    nombres = [
        "Ana","Luis","Pedro","Marta",
        "Jose","Carla","Raúl","Lucía",
        "Sofía","Pablo","David","Elena"
    ]

    matriz = matriz_alumnos(nombres)

    print("Alumnos en clase:\n")
    imprimir(matriz)

if __name__ == "__main__":
    main()