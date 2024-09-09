"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <   <<<<<<")                                                           
print (f"\n","Ejercicio 3: Crea un programa que imprima una tabla de multiplicar del número que introduzca el usuario.\n")

print("""
        # Pedir al usuario que introduzca un número
                num = int(input("Introduce un número para mostrar su tabla de multiplicar: "))

        # Imprimir la tabla de multiplicar usando un bucle for
                print(f"Tabla de multiplicar del", num,":")
        -> range(1, 11): Genera los números del 1 al 10 para multiplicar.
        -> Bucle for: Recorre estos números, realiza la multiplicación y muestra el resultado en la forma estándar de la tabla de multiplicar.
                for i in range(1, 11):
                        resultado = num * i
                        print(f"num, 'x', i = resultado")
\n\n""")

# Pedir al usuario que introduzca un número
num = int(input("Introduce un número para mostrar su tabla de multiplicar: \n"))

# Imprimir la tabla de multiplicar usando un bucle for
print(f"\nTabla de multiplicar del", num,":\n")
for i in range(1, 11):
        resultado = num * i
        print("->",num, "x", i, "=", resultado)
