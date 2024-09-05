"""
        >>>>>>>    Ejercicios Extras   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extras   <<<<<<")                                                           
print (f"\n","Ejercicio 1: \n")
print (f"Una panadería vende trozos de tarta a 3.49€ cada una. El trozo que no es el día tiene un descuento del 60%.")
print (f"Escribir un programa que comience leyendo el número de trozos vendidos de hoy como los que no son del día.")
print (f"Después el programa debe mostrar el precio habitual de un trozo, el descuento que se le hace por no ser fresco,") 
print (f"el coste de lo ganado en los trozos del día y los que no, y el coste final total.")

print (f"     -> Variable para el precio del trozo del día > tD <")
print (f"     -> Variable para el precio del trozo no del día > nD <\n\n")

print (f"     -> Cada trozo que no es del día nD= 3.49 - (3.49%60).")
print (f"     -> Variable para el precio final del trozo que no es del día > nD <")
print (f"         - La fórmula será ->  tF = float(tD) - float(nD)")

print (f"El precio habitual del trozo de pizza es: 3.49€")

print (f"Ahora el programa pedirá al usuario que introduzca las cantidades vendidas para cada producto")
print (f"Por tanto, deberán crearse 2 input, 1 para cada producto.\n")

print (f"tD = input(¿Introduzca cantidad de trozos vendidos del día?)")
print (f"tF = input(¿Introduzca cantidad de trozos vendidos no frescos?)\n")

tD = input("\n¿Introduzca cantidad de unidades trozos vendidos del día?\n")
nD = input("\n¿Introduzca cantidad de unidades trozos vendidos no frescos?\n")

