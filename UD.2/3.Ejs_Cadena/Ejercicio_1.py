"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 1: \n")
print ("""Los teléfonos de una empresa tienen el siguiente formato prefijo-número extensión donde el prefijo es el código del
país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de 
teléfono sin el prefijo y la extensión."\n""")

print("""
# Solicitar número de teléfono al usuario

    telefono = input("Introduce un número de teléfono con el formato +34-913724710-56: ")

# Verificar la longitud mínima y si contiene exactamente dos guiones

    if len(telefono) >= 17 and telefono.count('-') == 2:
        
        # Encontrar las posiciones de los guiones
        
            primer_guion = telefono.find('-')
            segundo_guion = telefono.rfind('-')

    # Extraer el prefijo, número central y la extensión

        -> El prefijo se extrae de telefono[:primer_guion].
        
            prefijo = telefono[:primer_guion]
        
        -> El número central se obtiene de telefono[primer_guion + 1 : segundo_guion].
        
            numero_central = telefono[primer_guion + 1 : segundo_guion]
        
        -> La extensión se obtiene de telefono[segundo_guion + 1:].
        
            extension = telefono[segundo_guion + 1:]

    # Verificar que el prefijo sea +34, el número central tenga 9 dígitos y la extensión tenga 2 dígitos
    
    if prefijo == "+34" and len(numero_central) == 9 and len(extension) == 2:
        
        # Mostrar el número sin el prefijo y la extensión
        
        print("El número de teléfono es:", numero_central)
    else:
        
        if prefijo != "+34":
            print("El prefijo debe ser +34.")
        if len(numero_central) != 9:
            print("El número central debe tener 9 dígitos.")
        if len(extension) != 2:
            print("La extensión debe tener 2 dígitos.")
else:
    print("El formato del número de teléfono es incorrecto. Asegúrate de seguir el formato +34-XXXXXXXXX-XX.")\n\n""")

# Solicitar número de teléfono al usuario
telefono = input("Introduce un número de teléfono con el formato +34-913724710-56: \n")

# Verificar la longitud mínima y si contiene exactamente dos guiones
if len(telefono) >= 17 and telefono.count('-') == 2:
    # Encontrar las posiciones de los guiones
    primer_guion = telefono.find('-')
    segundo_guion = telefono.rfind('-')

    # Extraer el prefijo, número central y la extensión
    prefijo = telefono[:primer_guion]
    num = telefono[primer_guion + 1 : segundo_guion]
    extension = telefono[segundo_guion + 1:]

    # Verificar que el prefijo sea +34, el número central tenga 9 dígitos y la extensión tenga 2 dígitos
    if prefijo == "+34" and len(num) == 9 and len(extension) == 2:
        # Mostrar el número sin el prefijo y la extensión
        print("El número de teléfono es:", num,".\n")
    else:
        if prefijo != "+34":
            print("El prefijo debe ser +34.\n")
        if len(num) != 9:
            print("El número central debe tener 9 dígitos.\n")
        if len(extension) != 2:
            print("La extensión debe tener 2 dígitos.\n")
else:
    print("El formato del número de teléfono es incorrecto. Asegúrate de seguir el formato +34-XXXXXXXXX-XX.\n")

