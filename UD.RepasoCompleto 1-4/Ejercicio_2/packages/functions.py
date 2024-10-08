# Función que muestra la tabla de multiplicar de un número dado.

def mostrar_tabla(num):
    """Función que muestra la tabla de multiplicar de un número dado."""

    tabla = []

    for i in range(1,11):
        res = num * i
        tabla.append(f"{num} x {i} = {res}")

    return tabla

# Función que imprime las tablas de multiplicar del 1 al 10.

def mostrar_tablas():
    """Función que imprime las tablas de multiplicar del 1 al 10."""

    tablas = {}

    for num in range(1,11):
        tablas[num] = mostrar_tabla(num)

    return tablas