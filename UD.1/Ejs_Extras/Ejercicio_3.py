"""
        >>>>>>>    Ejercicios Extras   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extras   <<<<<<")                                                           
print (f"\n","Ejercicio 3: \n")
print (""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
Tu índice de masa corporal es imc donde imc es el índice de masa corporal calculado 
redondeado con dos decimales.
              
                        Imc = peso/estatura**2
                Redondear con 2 decimales => round(variable,2) """)

print (f"     -> Variable para el peso > p <")
print (f"     -> Variable para la estatura > e <\n\n")

print (f"El programa pedirá al usuario que introduzca su peso y estatura")
print (f"Por tanto, deberán crearse 2 input, 1 para cada valor.\n")


p = input("¿Introduzca su peso?\n")
e = input("\n¿Introduzca su estatura?\n")

print (f"El programa mostrará los datos introducidos por el usuario")

print (f"Sus datos introducidos son:")
print ("        - Su peso: ",p)
print ("        - Su estatura: ",e)

print (f"\nPor último, el programa calculará el índice de masa corporal del usuario y lo redondeará a 2 decimales")

imc = (float(p)/float(e))**2

print (f"Su índice de masa corporal es: ", round(imc,2),"\n")



