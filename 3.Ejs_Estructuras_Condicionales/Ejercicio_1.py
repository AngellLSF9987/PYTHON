"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                             """
                                                             
print (f"\n>>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<\n")                                                           
print ("""Ejercicio 1: Escribir un programa que almacene la cadena de caracteres password en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable.\n""")

print(f"Primero habrá que crear la variable con valor almacenado > password <")
print (f'p = "password"\n')

print(f"Seguidamente se creará un input que pregunte al usuario por la contraseña\n")

print(f"u = input('¿Introduzca su contraseña?\n')")
print (f"La variable > u < almacenará la respuesta del usuario\n")

print (f"Por último, se creará la estructura condicional que comparará la contraseña almacenada y la respuesta de la usuario\n")

print("""       if(p != u):
                  print ("Algo ha ido mal...la contraseña no coincide")
                else:
                  print ("Contraseña correcta: ",u)\n\n""")

p = "password" 

u = input("¿Introduzca su contraseña?\n")

if (p != u):
    print("Algo ha ido mal...la contraseña no coincide")
else:
    print ("Contraseña correcta: ",u)