"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 4: \n")
print (""" Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y, (no incluir 0). 
Decir que cuadrante son."\n""")

print ("""
# Solicitar al usuario que introduzca las coordenadas x e y.

        x = int(input("Introduzca la coordenada x (no debe ser 0): \n"))
        y = int(input("Introduzca la coordenada y (no debe ser 0): \n"))

# Determinar el cuadrante según los valores de x e y.

        if x > 0 and y > 0:
                print("El punto está en el primer cuadrante.\n")
        elif x < 0 and y > 0:
                print("El punto está en el segundo cuadrante.\n")
        elif x < 0 and y < 0:
                print("El punto está en el tercer cuadrante.\n")
        elif x > 0 and y < 0:
                print("El punto está en el cuarto cuadrante.\n")\n\n""")

# Solicitar al usuario que introduzca las coordenadas x e y.
x = int(input("Introduzca la coordenada x (no debe ser 0): \n"))
y = int(input("Introduzca la coordenada y (no debe ser 0): \n"))

# Determinar el cuadrante según los valores de x e y.
if (x > 0 and y > 0):
    print("El punto está en el primer cuadrante.\n")
elif (x < 0 and y > 0):
    print("El punto está en el segundo cuadrante.\n")
elif (x < 0 and y < 0):
    print("El punto está en el tercer cuadrante.\n")
elif (x > 0 and y < 0):
    print("El punto está en el cuarto cuadrante.\n")


