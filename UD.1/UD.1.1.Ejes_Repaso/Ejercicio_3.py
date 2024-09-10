"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 3: \n")
print ("""Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."\n""")

print("""

# Solicitar al usuario que introduzca los tres valores numéricos.

num1 = input("Introduzca el primer número: \n")
num2 = input("Introduzca el segundo número: \n")
num3 = input("Introduzca el tercero número: \n")

# Casting de los input pasar a tipo entero.

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Tratar las entradas del usuario comparando los valores numéricos para encontrar el de mayor valor.

if (num1 > num2 and num1 > num3):
    print("El primer número es el de mayor valor numérico.\n")
elif (num2 < num1 and num2 > num3):
    print("El segundo número es el de mayor valor numérico.\n")
elif (num3 > num1 and num3 < num2):
    print("El tercer número es el de mayor valor numérico.\n")
else: 
    print("Todos los números tienen el mismo valor numérico.\n")\n\n""")

# Solicitar al usuario que introduzca los tres valores numéricos.

num1 = input("Introduzca el primer número: \n")
num2 = input("Introduzca el segundo número: \n")
num3 = input("Introduzca el tercero número: \n")

# Casting de los input pasar a tipo entero.

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Tratar las entradas del usuario comparando los valores numéricos para encontrar el de mayor valor.

if (num1 > num2 and num1 > num3):
    print("El primer número es el de mayor valor numérico.\n")
elif (num2 > num1 and num2 > num3):
    print("El segundo número es el de mayor valor numérico.\n")
elif (num3 > num1 and num3 > num2):
    print("El tercer número es el de mayor valor numérico.\n")
else: 
    print("Todos los números tienen el mismo valor numérico.\n")