"""
        >>>>>>>    Ejercicios Clase   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Clase   <<<<<<")                                                           
print (f"\n","Ejercicio 4: \n")
print ("""Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante 
que atrás.\n""")


print("""
# Solicitar una cadena de caracteres al usuario

            cadena = input("Introduce una cadena de caracteres: ")

# Eliminar espacios y convertir la cadena a minúsculas para hacer una comparación correcta
    
    -> Usamos replace() para eliminar los espacios y lower() para convertir todo a minúsculas (esto es opcional, pero facilita la comparación).
            
            limpia = cadena.replace(" ", "").lower()

# Verificar si la cadena es igual a su inversa
    
    -> Verificamos si la cadena limpia es igual a su reverso utilizando la sintaxis [::-1], que invierte la cadena.
    
            if limpia == limpia[::-1]:
                print("La cadena es un palíndromo.")
            else:
                print("La cadena no es un palíndromo.")\n\n""")

# Solicitar una cadena de caracteres al usuario
cadena = input("Introduce una cadena de caracteres: ")

# Eliminar espacios y convertir la cadena a minúsculas para hacer una comparación correcta
limpia = cadena.replace(" ", "").lower()

# Verificar si la cadena es igual a su inversa
if limpia == limpia[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
