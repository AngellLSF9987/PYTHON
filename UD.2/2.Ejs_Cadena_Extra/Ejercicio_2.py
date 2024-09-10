"""
        >>>>>>>    Ejercicios Extra de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extra de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 2: \n")

print (""" Ingresar un mail por teclado. Verificar si el texto ingresado contiene solo un carácter \"@\".\n\n""")

print("""
# Solicitar el correo electrónico al usuario

        email = input("Introduce tu correo electrónico: ")

# Contar cuántas veces aparece el carácter '@'
    
    -> Contar '@': Usamos el método .count('@') para contar cuántas veces aparece el carácter '@' en el texto ingresado.
    
        count_arroba = email.count('@')

# Verificar si el texto contiene solo un '@'

    -> Verificar la cantidad: Si el contador es igual a 1, significa que el correo contiene exactamente un '@'. 
       Si es diferente, no cumple con el criterio.
       
        if count_arroba == 1:
            print("El correo electrónico es válido (contiene solo un '@').")
        else:
            print("El correo electrónico no es válido (debe contener exactamente un '@').")\n\n""")

# Solicitar el correo electrónico al usuario
email = input("Introduce tu correo electrónico: ")

# Contar cuántas veces aparece el carácter '@'
count_arroba = email.count('@')

# Verificar si el texto contiene solo un '@'
if count_arroba == 1:
    print("El correo electrónico es válido (contiene solo un '@').")
else:
    print("El correo electrónico no es válido (debe contener exactamente un '@').")
