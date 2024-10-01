"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 4: \n")
print ("""
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
indicando si la dirección es válida o no, valiéndose de una función para
decidirlo. Una dirección se considerará válida si contiene el símbolo "@".    

# Función validar correo

def es_valido(correo):
        if "@" in correo:
                return True
        else:
                return False
        
# Solictar email al usuario

correo = input("Ingresa el email a validar:\n")

# Llamar a la función de validar

if es_valido(correo):
        print(f"El e-mail {correo} es válido.\n")
else:
        print(f"El e-mail {correo} no es válido.\n")    \n""")

# Función validar correo

def es_valido(correo):
        if "@" in correo:
                return True
        else:
                return False
        
# Solictar email al usuario

correo = input("Ingresa el email a validar:\n")

# Llamar a la función de validar

if es_valido(correo):
        print(f"El e-mail {correo} es válido.\n")
else:
        print(f"El e-mail {correo} no es válido.\n")