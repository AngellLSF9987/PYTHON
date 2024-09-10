"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 7: \n")
print ("""Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador 
ingresar la cadena 'si' o 'no' por teclado. Mostrar la suma de los valores ingresados.\n""")

print ("""

# Inicializar la variable para almacenar la suma
        
        suma = 0

# Bucle para solicitar números enteros al usuario
        
        while True:
        
# Pedir al usuario que ingrese un número entero
        
                numero = int(input("Ingrese un número entero: \n"))
    
# Sumar el número ingresado a la suma total
    
                suma += numero
    
# Preguntar si desea ingresar otro número
    
                continuar = input("¿Desea ingresar otro número? (si/no): \n").strip().lower()
    
# Verificar la respuesta del usuario
    
                if continuar != 'si':
                                break

# Mostrar la suma de los números ingresados

print("La suma de los números ingresados es:", suma,".")\n\n""")

# Inicializar la variable para almacenar la suma
suma = 0

# Bucle para solicitar números enteros al usuario
while True:
    # Pedir al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero: \n"))
    
    # Sumar el número ingresado a la suma total
    suma += numero
    
    # Preguntar si desea ingresar otro número
    continuar = input("¿Desea ingresar otro número? (si/no): \n").strip().lower()
    
    # Verificar la respuesta del usuario
    if (continuar != 'si'):
        break

# Mostrar la suma de los números ingresados
print("La suma de los números ingresados es:", suma,".\n")
