# Función para obtener la parte del nombre de usuario del correo
def obtener_nombre(correo):
    return correo.split('@')[0]  # Separar en base a '@' y tomar la parte de la izquierda

# Función para crear la nueva clave de usuario
def crear_clave(nombre, dia):
    return f"{nombre}{dia}@altavoces.es"  # Formatear la clave según las indicaciones

# Programa principal
correo_usuario = input("Introduce tu correo electrónico: ")
dia = input("Introduce tu día de nacimiento (solo número): ")

# Obtener el nombre de usuario
nombre = obtener_nombre(correo_usuario)

# Crear la clave de usuario final
clave_usuario = crear_clave(nombre, dia)

# Mostrar la clave de usuario final
print("Tu nueva clave de usuario es:", clave_usuario)

