"""
        >>>>>>>    Ejercicios Extras   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extras   <<<<<<")                                                           
print (f"\n","Ejercicio 1: \n")
print ("""Una panadería vende trozos de tarta a 3.49€ cada una. El trozo que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de trozos vendidos de hoy como los que no son del día.
Después el programa debe mostrar el precio habitual de un trozo, el descuento que se le hace por no ser fresco, 
el coste de lo ganado en los trozos del día y los que no, y el coste final total.\n""")

print (f"     -> Variable para el precio del trozo del día > pD <")
print (f"     -> Variable para el precio del trozo no del día > nD <\n\n")
print (f"     -> El precio habitual del trozo de pizza es: 3.49€")
print (f"     -> Cada trozo que no es del día pN = 3.49 - (3.49%60)")
print (f"     -> Usaremos una variable donde almacenar el precio con el decuento aplicado > dif <\n")
print (f"         - Las fórmulas empleadas:   dif = (tD*60)/100 ")
print (f"                                     pN = pD - round(dif,2)")
print (f"         - La fórmula final será ->  tF = float(tD) + float(nD)")

print (f"Ahora el programa pedirá al usuario que introduzca las cantidades vendidas para cada producto")
print (f"Por tanto, deberán crearse 2 input, 1 para cada producto.\n")

print (f"tD = input(¿Introduzca cantidad de trozos vendidos del día?)")
print (f"tF = input(¿Introduzca cantidad de trozos vendidos no frescos?)\n")


pD = 3.49
print (f"El precio habitual del trozo de pizza: ", pD)

dif = (pD*60)/100
print (f"El descuento aplicado en algunos sabores es del 60% ",round(dif,2),"\n")

pN = pD - round(dif,2)
print(f"El precio de esos trozos de pizza con descuento es: ",round(pN,2),"\n")

tD = input("\n¿Introduzca cantidad de unidades trozos vendidos del día?\n")
tD = int(tD)*pD

nD = input("\n¿Introduzca cantidad de unidades trozos vendidos no frescos?\n")
nD = int(nD)*pN

tF = float(tD) + float(nD)

print (f"LA VENTA DE TROZOS DEL DÍA: ", round(tD,2),"\n")
print (f"LA VENTA DE TROZOS CON DESCUENTO: ", round(nD,2),"\n")
print (f"LA VENTA TOTAL: ",round(tF,2),"\n")