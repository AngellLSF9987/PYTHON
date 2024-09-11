"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 5: \n")
print ("""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta."\n""")

print("""

# Solicitar los productos de la cesta al usuario

    productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

# Separar los productos utilizando la coma como delimitador

    lista = productos.split(',')

# Mostrar cada producto en una línea distinta

    print("Los productos en la cesta son:")

    for producto in lista:
    
        print(producto.strip())  # strip() elimina los espacios en blanco al principio y al fina.\n\n""")


# Solicitar los productos de la cesta al usuario
productos = input("Introduce los productos de la cesta de la compra, separados por comas: \n")

# Separar los productos utilizando la coma como delimitador
lista = productos.split(',')

# Mostrar cada producto en una línea distinta
print("Los productos en la cesta son:\n")
for producto in lista:
    print(producto.strip(),"\n")  # strip() elimina los espacios en blanco al principio y al final
