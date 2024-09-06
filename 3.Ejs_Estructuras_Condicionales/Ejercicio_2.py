"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                             """
                                                             
print (f">>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<\n")                                                           
print ("""Ejercicio 2:  Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar un error.\n""")

print (f" - La variable para el primer número será > num1 <.")
print (f" - La variable para el segundo número será > num2 <.\n")

print ("""Ahora el programa pedirá al usuario que introduzca los valores para cada variable
Por tanto, deberán crearse 2 input, 1 para cada número.\n""")

print (f"divs = input(Introduzca el primer valor numérico:)")
print (f"divn = input(Introduca el segundo valor numérico:)\n")

# Petición de números al usuario

divs = input("Introduzca el primer valor numérico:\n")
divn = input("Introduzca el segundo valor numérico:\n")

# Convertir los inputs a float
print (f"divs = float(divs)")
print (f"divn = float(divn)\n")

divs = float(divs)
divn = float(divn)

print ("""\nA continuación, el programa realizará la operación de división entre ambos valores.
       
                - El resultado será almacenado una variable llamada > rest <
                
                - La fórmula será la siguiente: 
          
                        -> rest = divs / divn""")

print (f"Por último, el programa hará el tratamiento respectivo a las condicionantes interpuestas para el resultado del ejercicio")

print("""       if(divs == 0):
                  print ("Error: El valor de dividir por CERO")
                elif(divn == 0):
                  print ("Error: El valor de dividir por CERO")
                else:
                  rest = float(divs)/float(divn)
                  print ("El resultado de la división es: ",round(rest,1))\n\n""")

if(divs == 0 and divn!= 0):
  print ("Error: El valor de dividir por CERO")
elif(divn == 0):
  print ("Error: El valor de dividir por CERO")
else:
  rest = divs/divn
  print ("El resultado de la división es: ",rest,"\n")

