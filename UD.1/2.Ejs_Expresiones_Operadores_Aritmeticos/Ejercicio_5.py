"""
        >>>>>>>    Ejercicios de Expresiones y Operadores Aritméticos  <<<<<<
                                                                            """
print (f"\n>>>>>>>    Ejercicios de Expresiones y Operadores Aritméticos   <<<<<<\n")  
print (f"Ejercicio 5. La escala Celsius es centígrada, 100 divisiones separan el punto de congelación del punto de ebullición del agua.")
print (f"\nEn la escala Fahrenheit de los anglosajones, estos dos puntos están separados por 180 grados.")
print (f"\nLa escala de Kelvin es una escala absoluta utilizada en ciencias.\n")
print (f">>> Cree un programa para convertir degrados centígrados a Kelvin y Fahrenheit.\n")
print (f"   - Solicite al usuario la cantidad de grados centígrados para convertirlos usando las siguientes tablas de conversión:\n\n")
print (f"                       -> kelvin = celsius + 273\n")
print (f"                       -> fahrenheit = celsius * 18/10 + 32\n")

print (f"Ahora se deberá tenr en cuenta las fórmulas especificadas arriba.\n")
print (f"El usuario deberá introducir el valor de la variable grados celsius > c <. Por tanto, deberá existir un input")
print (f"que luego deberá ser tratado.\n")

print (f"c = input(¿Introduzca cantidad de grados?)\n")

print (f"  - La variable para los grados kelvin será > k <")
print (f"  - La variable para los grados farenheit será > f <")

c = input("\n¿Introduzca cantidad de grados?\n")

k = float(c) + 273
f = float(c) * 18/10 +32

print (f"El valor en grados Kelvin es: ",round(k,2),"\n")
print (f"El valor en grados Kelvin es: ",round(f,2),"\n")
34

