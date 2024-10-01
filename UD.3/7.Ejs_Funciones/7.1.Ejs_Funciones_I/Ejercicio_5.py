"""
        >>>>>>>    Ejercicio Funciones I   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones I  <<<<<<")                                                            
print (f"\n","Ejercicio 5: \n")
print ("""
Solicitar números al usuario hasta que ingrese el cero. Por cada uno,
mostrar la suma de sus dígitos (utilizando una función que realice dicha
suma).                                                                      

# Función para sumar los dígitos de un número
def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  # Extraer el último dígito
        numero = numero // 10  # Eliminar el último dígito
    return suma

# Solicitar números al usuario hasta que ingrese el cero
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        print("Fin del programa.")
        break
    
    # Mostrar la suma de los dígitos del número ingresado
    suma = sumar_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma}")                     \n""")


# Función para sumar los dígitos de un número
def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  # Extraer el último dígito
        numero = numero // 10  # Eliminar el último dígito
    return suma

# Solicitar números al usuario hasta que ingrese el cero
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        print("Fin del programa.")
        break
    
    # Mostrar la suma de los dígitos del número ingresado
    suma = sumar_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma}")
