"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                             """
                                                             
print (f">>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<\n")                                                           
print ("""Ejercicio 1: Escribir un programa que almacene la cadena de caracteres password en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable.\n""")

print(f"Primero habrá que crear la variable con valor almacenado > password <")
print (f"p = password")

print(f"Seguidamente se creará un input que pregunte al usuario por la contraseña")

print(f"u = input('¿Introduce un valor para m?\n')")
print (f"La variable > u < almacenará la respuesta del usuario")

print (f"Por último, se creará la estructura condicional que comparará la contraseña almacenada y la respuesta de la usuario")

print(""" if(u = p):
            print ("Contraseña correcta: ",u)
          else:
            print ("Algo ha ido mal...la contraseña no coincide")""")

p = password

u = input('¿Introduzca su contraseña?\n')

if (p == u):
    print("Contraseña correcta: ",u)
else:
    print ("Algo ha ido mal...la contraseña no coincide")