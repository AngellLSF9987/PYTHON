# Función para convertir la cadena a mayúsculas
def convertir(cadena):
    return cadena.upper()

# Función para separar las palabras y volverlas a unir con espacios
def espacios(cadena):
    palabras = cadena.split()  # Separamos las palabras
    cadena_resultado = ""  # Inicializamos una cadena vacía
    
    for palabra in palabras:
        cadena_resultado += palabra + " "  # Agregamos cada palabra con un espacio al final
    
    return cadena_resultado.strip()  # Quitamos el espacio extra final

# Programa principal
cadena_usuario = input("Introduce una cadena de texto: ")

# Convertir la cadena a mayúsculas
cadena_mayus = convertir(cadena_usuario)

# Separar y unir las palabras
resultado = espacios(cadena_mayus)

# Mostrar el resultado final
print("Cadena procesada:", resultado)


