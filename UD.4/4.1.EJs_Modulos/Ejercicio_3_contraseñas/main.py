from packages.functions import generar

# Función principal que ejecuta el programa.

def crear():
    longitud = int(input("Introduce la longitud deseada para la contraseña:\n"))
    contraseña = generar(longitud)
    
    print(f"Su contraseña segura es: {contraseña}")

# Incialización del programa

if __name__ == "__main__":
    crear()