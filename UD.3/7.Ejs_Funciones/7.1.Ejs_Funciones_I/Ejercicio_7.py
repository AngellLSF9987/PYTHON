"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 7: \n")
print ("""
Crear un programa que pidiendo al usuario su nombre completo y su dni
con letra, cree un identificador para cada usuario.

    a. Controlar que usuario no introduce el nombre vacío.
    b. Se puede controlar que dni sea correcto
    c. Por cada socio se debe imprimir su identificador único, el cual
       estará formado por: el primer nombre, la cantidad de letras del

        primer apellido y los primeros 3 dígitos de su DNI. Ejemplo:
            Nombre: Loreto Pelegrín Castillo
            DNI: 11111111H
            Loreto8111                      
            
            
# Función para verificar si el DNI es válido
def es_dni_valido(dni):
    if len(dni) != 9:
        return False
    numeros = dni[:-1]
    letra = dni[-1]
    if not numeros.isdigit() or not letra.isalpha():
        return False
    return True

# Función para crear el identificador único
def crear_identificador(nombre_completo, dni):
    nombres = nombre_completo.split()
    primer_nombre = nombres[0]
    primer_apellido = nombres[1] if len(nombres) > 1 else ""
    cantidad_letras_apellido = len(primer_apellido)
    primeros_digitos_dni = dni[:3]
    
    return f"{primer_nombre}{cantidad_letras_apellido}{primeros_digitos_dni}"

# Solicitar datos al usuario
nombre_completo = input("Ingresa tu nombre completo: ").strip()

# Controlar que el nombre no esté vacío
if not nombre_completo:
    print("El nombre no puede estar vacío.")
else:
    dni = input("Ingresa tu DNI (formato: 12345678A): ").strip()
    
    # Controlar que el DNI sea válido
    if not es_dni_valido(dni):
        print("El DNI ingresado no es válido.")
    else:
        # Crear y mostrar el identificador único
        identificador = crear_identificador(nombre_completo, dni)
        print(f"Tu identificador único es: {identificador}")                        \n""")


# Función para verificar si el DNI es válido
def es_dni_valido(dni):
    if len(dni) != 9:
        return False
    numeros = dni[:-1]
    letra = dni[-1]
    if not numeros.isdigit() or not letra.isalpha():
        return False
    return True

# Función para crear el identificador único
def crear_identificador(nombre_completo, dni):
    nombres = nombre_completo.split()
    primer_nombre = nombres[0]
    primer_apellido = nombres[1] if len(nombres) > 1 else ""
    cantidad_letras_apellido = len(primer_apellido)
    primeros_digitos_dni = dni[:3]
    
    return f"{primer_nombre}{cantidad_letras_apellido}{primeros_digitos_dni}"

# Solicitar datos al usuario
nombre_completo = input("Ingresa tu nombre completo: ").strip()

# Controlar que el nombre no esté vacío
if not nombre_completo:
    print("El nombre no puede estar vacío.")
else:
    dni = input("Ingresa tu DNI (formato: 12345678A): ").strip()
    
    # Controlar que el DNI sea válido
    if not es_dni_valido(dni):
        print("El DNI ingresado no es válido.")
    else:
        # Crear y mostrar el identificador único
        identificador = crear_identificador(nombre_completo, dni)
        print(f"Tu identificador único es: {identificador}")
