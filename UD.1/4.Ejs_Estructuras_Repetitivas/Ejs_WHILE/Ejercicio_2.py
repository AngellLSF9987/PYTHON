"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <   <<<<<<\n")                                                           
print (f"\n","Ejercicio 2: Creo un programa para calcular la suma de números que introduzca el usuario por pantalla hasta que ingrese 0.\n")

print("""
        # Inicializar la variable para la suma
                -> Inicialización: suma empieza en 0.
                        suma = 0

        # Inicializar la variable para el número ingresado por el usuario
                numero = int(input("Introduce un número (0 para terminar): "))

        # Bucle while que continúa hasta que se introduce un 0
                -> Condición del bucle: El bucle continúa mientras el número ingresado no sea 0.
                        while numero != 0:
                        suma += numero  # Sumar el número a la variable suma
                -> Actualización: En cada iteración, el número ingresado se suma a suma.
                        numero = int(input("Introduce otro número (0 para terminar): "))  # Pedir otro número

        # Imprimir la suma total
                print("La suma total es:", suma)""")

# Inicializar la variable para la suma
suma = 0

# Inicializar la variable para el número ingresado por el usuario
numero = int(input("Introduce un número (0 para terminar): "))

# Bucle while que continúa hasta que se introduce un 0
while numero != 0:
    suma += numero  # Sumar el número a la variable suma
    numero = int(input("Introduce otro número (0 para terminar): "))  # Pedir otro número

# Imprimir la suma total
print("La suma total es:", suma)
