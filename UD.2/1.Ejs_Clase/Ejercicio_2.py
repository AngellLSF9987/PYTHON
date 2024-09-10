"""
        >>>>>>>    Ejercicios Clase   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Clase   <<<<<<")                                                           
print (f"\n","Ejercicio 2: \n")
print ("""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra 
solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas
y minúsculas como quiera. \n""")

print("""

# Solicitar el nombre completo al usuario.

            nombre = input("Introduce tu nombre completo: ")

# Mostrar el nombre en minúsculas.

        -> Minúsculas: El método .lower() convierte todas las letras a minúsculas.

            print("Nombre en minúsculas:", nombre.lower())

# Mostrar el nombre en mayúsculas.

        -> Mayúsculas: Usamos el método .upper() para convertir todas las letras a mayúsculas.
        
            print("Nombre en mayúsculas:", nombre.upper())

# Mostrar el nombre con la primera letra de cada palabra en mayúscula.

        -> Primera letra en mayúscula: Con .title(), convertimos la primera letra de cada palabra a mayúscula y el resto a minúsculas.

            print("Nombre con primeras letras en mayúscula:", nombre.title())
""")


# Solicitar el nombre completo al usuario
nombre = input("Introduce tu nombre completo: ")

# Mostrar el nombre en minúsculas
print("Nombre en minúsculas:", nombre.lower())

# Mostrar el nombre en mayúsculas
print("Nombre en mayúsculas:", nombre.upper())

# Mostrar el nombre con la primera letra de cada palabra en mayúscula
print("Nombre con primeras letras en mayúscula:", nombre.title())
