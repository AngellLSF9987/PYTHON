"""
        >>>>>>>    Ejercicios Extras   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extras   <<<<<<")                                                           
print (f"\n","Ejercicio 2: \n")
print (f"Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.")
print (f"Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben") 
print (f"calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.\n")
print (f"     -> Cada payaso pesa 112 g.")
print (f"     -> Cada muñeca 75 g.")  
print (f"\n\nEscribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule") 
print (f"el peso total del paquete que será enviado.\n")

print (f" - La variable para el peso que tienen payasos vendidos será > p <.")
print (f" - La variable para el peso que tienen muñecas vendidos será > m <.\n")

p = 112
m = 75

print (f" - La variable que almacenará el peso total de los payasos vendidos será > cP <")
print (f" - La variable que almacenará el peso total de los payasos vendidos será > cM <\n")

print (f"Ahora el programa pedirá al usuario que introduzca las cantidades vendidas para cada producto")
print (f"Por tanto, deberán crearse 2 input, 1 para cada producto.\n")

print (f"cP = input(¿Introduzca cantidad de unidades vendidas de payasos?)")
print (f"cM = input(¿Introduzca cantidad de unidades vendidas de muñecas?)\n")

cP = input("\n¿Introduzca cantidad de unidades vendidas de payasos?\n")
cM = input("\n¿Introduzca cantidad de unidades vendidas de muñecas?\n")

print (f"\nA continuación, el programa realizará el cálculo de cada peso total por producto.")

print (f"La variable que almacenará el peso total de los payasos vendidos será > pT <")
print (f"La variable que almacenará el peso total de los payasos vendidos será > mT <")

print (f"Las fórmulas serán:\n")
print (f"      - pT = p * int(cP)\n")
print (f"      - mT = m * int(cM)\n")

pT = p*int(cP)
mT = m*int(cM)

print (f"Por último, sumaremos los pesos totales de ambos productos para obtener el resultado buscado.\n")
print (f"La fórmula será:\n")
print (f"    -  total = pT + mT \n")

total = pT + mT

print (f"El peso total del paquete que será enviado: ",total,"\n")

