"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                             """
                                                             
print (f">>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<\n")                                                           
print ("""Ejercicio 3: Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.\n""")

print ("""El programa pedirá al usuario que introduzca el valor para la variable
Por tanto, deberán crearse 2 input, 1 para cada número.\n""")

print (f" - La variable para el número será > num <.")

print (f"num = input(Introduzca el primer valor numérico:)")

# Petición de números al usuario

num = input("Introduzca un valor numérico:\n")

# Convertir los inputs a int
print (f"num = int(num)\n")

num = int(num)

print (f"Por último, el programa hará el tratamiento respectivo a las condicionantes interpuestas para el resultado del ejercicio.\n")

print("""Si el número introducido por el usuario es divisible por 2:
            if(num % 2 == 0):
                  print ("EL número introducido es par")
        De lo contrario:
            else:
                  print ("ERROR: El número introducido no es un número entero: ",num)\n\n""")

# Estructura condicional para verificar si es par o impar
if(num % 2 == 0):
        print ("EL número introducido es par") 
else:
        print ("EL número introducido es impar\n")