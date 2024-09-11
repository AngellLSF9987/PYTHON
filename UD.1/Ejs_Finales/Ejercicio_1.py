"""
        >>>>>>>    Ejercicios Finales   <<<<<<
                                                            """
print (f"\n>>>>>>>    Ejercicios Finales   <<<<<<")                                                           
print ("""Ejercicio 1: Escribir un programa que muestre todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que saldrá del programa.\n\n""")

print("""
# Bucle infinito que se detendrá solo cuando el usuario escriba "salir"
    -> while True:: Un bucle infinito que solo se detendrá con una instrucción > break <.
    
        while True:
    
# Pedir al usuario que introduzca un texto
    -> input: Solicita al usuario que introduzca un texto.

        u = input("Introduce algo (escribe 'salir' para terminar): ")
    
# Verificar si el usuario quiere salir
    -> if entrada_usuario.lower() == "salir": Verifica si el texto introducido es "salir".
    
        if (u.lower() == "salir"):            # El parámetro > .lower() < convierte la entrada a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas.
        
        print("Programa terminado.")
    -> break: Sale del bucle si la entrada es "salir".
        
        break

    -> else: Si la entrada no es "salir", se muestra el texto introducido por el usuario.

        else:

# Mostrar lo que el usuario ha introducido
            print("Has introducido:", u)
\n\n""")

# Bucle infinito que se detendrá solo cuando el usuario escriba "salir"
while True:
    # Pedir al usuario que introduzca un texto
    u = input("Introduce algo (escribe 'salir' para terminar): \n")
    
    # Verificar si el usuario quiere salir
    if (u.lower() == "salir"):
        print("Programa terminado.")
        break
    else:
        # Mostrar lo que el usuario ha introducido
        print("Has introducido:", u,"\n")
