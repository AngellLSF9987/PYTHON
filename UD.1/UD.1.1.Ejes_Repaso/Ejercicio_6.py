"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 6: \n")
print (""" Realizar un programa que pida al usuario números por teclado. Preguntar después de ingresar el valor si desea cargar 
otro valor debiendo el operador introducir la cadena 'si' o 'no' por teclado. Mostrar la suma de los números una vez terminado el bucle."\n""")

print("""
# Inicializar la variable para almacenar la suma

                suma = 0

# Bucle para solicitar números al usuario

                while True:

# Pedir al usuario que ingrese un número

#       Entrada de número: Se solicita al usuario que ingrese un número. Para asegurar que se pueden ingresar números decimales, 
#       usamos float() para convertir el input a un número flotante. 
    
                numero = float(input("Ingrese un número: \n"))
    
# Sumar el número ingresado a la suma total

#       Acumulación: El número ingresado se suma a la variable suma.
        
                suma += numero
    
# Preguntar si desea ingresar otro número

#       Pregunta para continuar: Se pregunta al usuario si desea ingresar otro número. La respuesta se convierte a minúsculas 
#       y se elimina cualquier espacio adicional con .strip().lower()
    
                continuar = input("¿Desea ingresar otro número? (si/no): \n").strip().lower()
    
# Verificar la respuesta del usuario

#       Verificación de respuesta: Si la respuesta del usuario no es 'si', el bucle se rompe usando break.
    
                if continuar != 'si':
                                break

# Mostrar la suma de los números

                print("La suma de los números ingresados es:", suma,".")\n\n""")

# Inicializar la variable para almacenar la suma

suma = 0

# Bucle para solicitar números al usuario

while True:

# Pedir al usuario que ingrese un número

#       Entrada de número: Se solicita al usuario que ingrese un número. Para asegurar que se pueden ingresar números decimales, 
#       usamos float() para convertir el input a un número flotante.    
        
        numero = float(input("Ingrese un número: \n"))
    
# Sumar el número ingresado a la suma total
        
#       Acumulación: El número ingresado se suma a la variable suma.

        suma += numero
    
# Preguntar si desea ingresar otro número

#       Pregunta para continuar: Se pregunta al usuario si desea ingresar otro número. La respuesta se convierte a minúsculas 
#       y se elimina cualquier espacio adicional con .strip().lower().
    
        continuar = input("¿Desea ingresar otro número? (si/no): \n").strip().lower()
    
# Verificar la respuesta del usuario

#       Verificación de respuesta: Si la respuesta del usuario no es 'si', el bucle se rompe usando break.

        if (continuar != 'si'):
                        break

# Mostrar la suma de los números

        print("La suma de los números ingresados es:", suma,".\n")