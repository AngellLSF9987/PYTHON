"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <   <<<<<<")                                                           
print (f"\n","Ejercicio 4: Crear un programa, que pida al usuario un número, y muestre por pantalla, los números en orden inverso hasta 0. \n")

print("""
# Pedir al usuario que introduzca un número
        num = int(input("Introduce un número: \n"))

# Mostrar los números en orden inverso hasta 0 usando un bucle for
        print(f"Números en orden inverso desde ",num," hasta  0:\n")
        for i in range(num, -1, -1):
        print(i,end=" ")                        # Para mostrar en un sola línea la secuencia numérica, se añade > end= " " < 
\n\n""")

# Pedir al usuario que introduzca un número
num = int(input("Introduce un número: \n"))

# Mostrar los números en orden inverso hasta 0 usando un bucle for
print(f"\nNúmeros en orden inverso desde ",num," hasta  0:")
for i in range(num, -1, -1):
        print(i,end=" ")         # Para mostrar en un sola línea la secuencia numérica, se añade   > end= " " < 
