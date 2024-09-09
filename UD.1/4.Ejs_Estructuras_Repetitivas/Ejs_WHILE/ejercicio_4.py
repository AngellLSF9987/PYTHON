"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <   <<<<<<")                                                           
print (f"\n","Ejercicio 4: Crear un programa, que pida al usuario un número, y muestre por pantalla, los números en orden inverso hasta 0.\n")

print("""
      
        # Pedir al usuario que ingrese un número
                numero = int(input("Introduce un número: "))

        # Bucle while que imprime los números en orden inverso
                while (numero >= 0):
                print(numero)
                numero -= 1  # Restar 1 en cada iteración \n\n""")


# Pedir al usuario que ingrese un número
numero = int(input("Introduce un número: \n"))

# Bucle while que imprime los números en orden inverso
while (numero >= 0):
    print(numero, end= " ")
    numero -= 1  # Restar 1 en cada iteración
