"""
        >>>>>>>    Ejercicios de Expresiones y Operadores Aritméticos  <<<<<<
                                                                                    """
print (f"\n>>>>>>>    Ejercicios de Expresiones y Operadores Aritméticos   <<<<<<\n")                                                           

print ("""Ejercicio 3. Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año
o cuántos años faltan para llegar a ese año.\n""")

print (f"> Petición del año actual\n")
print (f"actual = input('¿Introduce el año actual?\n")

actual = input("¿Introduce el año actual?\n")

print (f"\n> Petición al usuario de una año cualquiera\n")
print (f"otro = input('¿Introduce un año cualquiera?\n")

otro = input("¿Introduce un año cualquiera?\n")

print (f"\nUna vez que se han introducido los dos valores para cada año, el programa calculará cuanto")
print (f"tiempo falta o cuanto tiempo ha pasado.\n")


print (f"Tratamiento y Casting de la variable resultado para su comparación con variable actual\n\n")
print ("""          if (int(actual) > int(otro)):
                        resultado = int(actual)-int(otro)
                        print(f'Han pasado ,resultado, años')
                    else:
                        resultado = int(otro)-int(actual)")
                        print(f'Faltan,resultado, años para llegar')\n\n""")


if (int(actual) > int(otro)):
    resultado = int(actual)-int(otro)
    print(f"Han pasado ",resultado," años")
else:
    resultado = int(otro)-int(actual)
    print(f"Faltan",resultado,"años para llegar")