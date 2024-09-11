"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 4: \n")
print ("""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro 
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio avanza.es."\n""")

print("""
# Solicitar el correo electrónico al usuario

    mail = input("Introduce tu correo electrónico: \n")

# Encontrar la posición de la arroba (@)

    arroba = correo.find('@')

# Verificar que el correo tiene un arroba

    if arroba != -1:
    
    # Extraer la parte antes de la arroba
    
        nomUser = correo[:arroba]
    
    # Construir el nuevo correo con el dominio avanza.es
    
        newMail = nomUser + "@avanza.es"
    
    # Mostrar el nuevo correo
    
        print("Tu nuevo correo es:", newMail,".\n")
    
    else:
        print("El correo electrónico introducido no es válido.\n")\n\n""")

# Solicitar el correo electrónico al usuario
mail = input("Introduce tu correo electrónico: \n")

# Encontrar la posición de la arroba (@)
arroba = mail.find('@')

# Verificar que el correo tiene un arroba
if arroba != -1:
    # Extraer la parte antes de la arroba
    nomUser = mail[:arroba]
    
    # Construir el nuevo correo con el dominio avanza.es
    newMail = nomUser + "@avanza.es"
    
    # Mostrar el nuevo correo
    print("Tu nuevo correo es:", newMail,".\n")
else:
    print("El correo electrónico introducido no es válido.\n")
