from packages.operations import generar,obtener,comparar

# Función principal para ejecutar el juego
def jugar():
    num_magic = generar()
    num_user = None

    while num_user != num_magic:
        num_user = obtener()
        comparar(num_user,num_magic)

# Inicialización del juego
if __name__ == "__main__":
    jugar()