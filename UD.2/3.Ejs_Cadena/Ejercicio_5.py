"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 5: \n")
print ("""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta."\n""")

print("""

productos_totales = []  # Lista para almacenar todos los productos

while True:
    productos = input("Introduce los productos de la cesta de la compra, separados por comas (o escribe 'exit' para salir): \n")
    
    if productos.lower() == "exit":  # Si el usuario escribe "exit", se sale del bucle
        print("Has salido de la cesta de la compra.")
        break

    # Separar los productos utilizando la coma como delimitador
    lista = productos.split(',')

    # Agregar cada producto a la lista total, eliminando espacios extra
    productos_totales.extend([producto.strip() for producto in lista])

    # Mostrar cada producto en una línea distinta
    print("Los productos en la cesta son:\n")
    
    for producto in lista:
        print(producto.strip(), "\n")  # strip() elimina los espacios en blanco al principio y al final

# Mostrar la lista final de productos

if productos_totales:
    print("Lista final de productos en la cesta:\n")
    print(", ".join(productos_totales))  # Mostrar los productos separados por comas.\n\n""")

total = []  # Lista para almacenar todos los productos

while True:
    productos = input("Introduce los productos de la cesta de la compra, separados por comas (o escribe 'exit' para salir): \n")
    
    if productos.lower() == "exit":  # Si el usuario escribe "exit", se sale del bucle
        print("Has salido de la cesta de la compra.")
        break

    # Separar los productos utilizando la coma como delimitador
    lista = productos.split(',')

    # Agregar cada producto a la lista total, eliminando espacios extra
    total.extend([producto.strip() for producto in lista])

    # Mostrar cada producto en una línea distinta
    print("Los productos en la cesta son:\n")
    
    for producto in lista:
        print(producto.strip(), "\n")  # strip() elimina los espacios en blanco al principio y al final

# Mostrar la lista final de productos
if total:
    print("Lista final de productos en la cesta:\n")
    print(", ".join(total))  # Mostrar los productos separados por comas


