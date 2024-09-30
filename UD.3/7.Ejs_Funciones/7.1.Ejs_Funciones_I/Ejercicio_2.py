"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 2: \n")
print ("""
. Escribir una función que reciba un número entero positivo y devuelva su
factorial. (Multiplicar todos los números enteros y positivos que hay entre
el número máximo que queramos y el número 1.)                                   


def factorial(num):
    res = 1
    
    for i in range(1, num +1):
        res *= i
    return res

num = input("Introduce un número entero positivo:\n")
print(f"El factorial del número {num} introducido es {factorial(num)}")

\n""")

def factorial(num):
    res = 1
    
    for i in range(1, num +1):
        res *= i
    return res

num = input("Introduce un número entero positivo:\n")
print(f"El factorial del número {num} introducido es {factorial(num)}")