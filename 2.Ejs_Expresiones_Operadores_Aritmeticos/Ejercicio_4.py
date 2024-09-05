"""
        >>>>>>>    Ejercicios de Expresiones y Operadores Aritméticos  <<<<<<
                                                                                        """
print (f"\n>>>>>>>   Ejercicios de Expresiones y Operadores Aritméticos   <<<<<<\n")                                                           
print (f"Ejercicio 4. Crea un programa para calcular la superficie y el volumen de una esfera, dado su radio.\n")

print (f"a) superficie = 4 * PI * radio al cuadrado(^2)\n")

print (f"El número PI será declarado como una constante.\n")
print (f"PI= 3.1415\n")

PI = 3.1415

print (f"El usuario deberá introducir el valor de la variable radio > r <. Por tanto, deberá existir un input")
print (f"que luego deberá ser tratado.\n")

print (f"r = input(¿Valor de radio?)\n")

r = input("¿Introduce un valor para radio?\n")

print (f"\nSentencia para calcular la superficie:\n")
print (f"    s = 4*PI*float(r)**2")

s = 4*PI*float(r)**2

print (f"\nEl valor de la superficie es: ",round(s,2),"\n")

print (f"b) volumen = 4/3 * PI* radio al cubo\n")

print (f"Sentencia para calcular el volumen:\n")
print (f"    v = 4/3*PI*float(r)**3\n")

v = 4/3*PI*float(r)**3

print (f"El valor del volumen es: ",round(v,2),"\n")
