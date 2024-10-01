"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 3: \n")
print ("""
Escribir una función que calcule el total de una factura tras aplicarle el
IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a
aplicar, y devolver el total de la factura. Si se invoca la función sin
pasarle el porcentaje de IVA, deberá aplicar un 21%.                        \n""")


def total_factura(sin_iva, porcentaje=21):
    total = sin_iva + (sin_iva * porcentaje / 100)
    
    return total

cantidad = float(input("Introduce la cantidad sin IVA:\n"))
iva = input("Introduce el porcentaje de IVA:\n") # Ésto es opcional ya que el sistema lleva aplicado el 21%

if iva:
    total = total_factura(cantidad,float(iva))
else:
    total = total_factura(cantidad)
    
print(f"El total de la factura es:{total}")