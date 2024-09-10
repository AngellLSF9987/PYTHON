"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 1: \n")
print ("""Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda 
"Todos los números son menores a diez."\n""")

print("""

# Solicitar al usuario que introduzca los tres valores numéricos.

num1 = input("Introduzca el primer número: \n")
num2 = input("Introduzca el segundo número: \n")
num3 = input("Introduzca el tercero número: \n")

# Casting de los input pasar a tipo entero.

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Tratar las entradas del usuario comparando los valores numéricos con el número 10.

if (num1 < 10 and num2 < 10 and num3 > 10):
    print("El primer y el segundo número son menores que 10 y el tercero es mayor que 10.\n")
elif (num1 < 10 and num2 > 10 and num3 < 10):
    print("El primer y el tercer número son menores que 10 y el segundo es mayor que 10.\n")
elif (num1 < 10 and num2 < 10 and num3 < 10):
    print("Todos los números son menores que 10.\n")
elif (num1 > 10 and num2 > 10 and num3 > 10):
    print("Todos los números son mayores que 10.\n")
else:
    print("Una combinación de números no cubierta por las condiciones anteriores.\n")\n\n""")

# Solicitar al usuario que introduzca los tres valores numéricos.

num1 = input("Introduzca el primer número: \n")
num2 = input("Introduzca el segundo número: \n")
num3 = input("Introduzca el tercero número: \n")

# Casting de los input pasar a tipo entero.

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Tratar las entradas del usuario comparando los valores numéricos con el número 10.

if (num1 < 10 and num2 < 10 and num3 > 10):
    print("El primer y el segundo número son menores que 10 y el tercero es mayor que 10.\n")
elif (num1 < 10 and num2 > 10 and num3 < 10):
    print("El primer y el tercer número son menores que 10 y el segundo es mayor que 10.\n")
elif (num1 > 10 and num2 < 10 and num3 < 10):
    print("El segundo y el tercer número son menores que 10 y el primero es mayor que 10.\n")
elif (num1 < 10 and num2 < 10 and num3 < 10):
    print("Todos los números son menores que 10.\n")
else: 
    print("Todos los números son mayores que 10.\n")
