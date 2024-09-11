"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 5: \n")
print ("""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta."\n""")

print("""

total = ""  # Cadena para almacenar todos los productos

while True:
    productos = input("Introduce los productos de la cesta de la compra, separados por comas (o escribe 'exit' para salir): \n")
    
    if (productos.lower() == "exit"):  # Si el usuario escribe "exit", se sale del bucle
        print("Has salido de la cesta de la compra.")
        break

    # Mostrar cada producto en una línea distinta, eliminando espacios extra
    print("Los productos en la cesta son:\n")
    separador = productos.split(',')
    
    for producto in separador:
        producto = producto.strip()  # Elimina los espacios en blanco al principio y al final
        print(producto)
        
        # Agregar el producto a la cadena total
        if (total):
            total += ", " + producto
        else:
            total = producto

# Mostrar la lista final de productos
    else:
        print("\nLista final de productos en la cesta:\n")
        print(total,".\n")\n\n""")

total = ""  # Cadena para almacenar todos los productos

while True:
    productos = input("Introduce los productos de la cesta de la compra, separados por comas (o escribe 'exit' para salir): \n")
    
    if (productos.lower() == "exit"):  # Si el usuario escribe "exit", se sale del bucle
        print("Has salido de la cesta de la compra.")
        break

    # Mostrar cada producto en una línea distinta, eliminando espacios extra
    print("Los productos en la cesta son:\n")
    separador = productos.split(',')
    
    for producto in separador:
        producto = producto.strip()  # Elimina los espacios en blanco al principio y al final
        print(producto)
        
        # Agregar el producto a la cadena total
        if (total):
            total += ", " + producto +'.'
        else:
            total = producto

# Mostrar la lista final de productos después de "exit"
if (total):
    print("\nLista final de productos en la cesta:\n")
    print(total)



