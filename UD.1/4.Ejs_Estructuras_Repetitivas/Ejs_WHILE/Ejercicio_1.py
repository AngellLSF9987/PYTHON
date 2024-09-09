"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <   <<<<<<")                                                           
print (f"\nEjercicio 1: Crea un programa utilizando el bucle while en que hay que mostrar por pantalla números del 1 al 10. \n")

print("""Inicializar la variable:
      
        -> num = 1""")

# Inicializar la variable
num = 1

print(f"Este bucle empleado mostrará la secuencia numérica pero cada número ocupará una línea.")

print("""
      1. Condición del bucle: El bucle continuará mientras numero sea menor o igual a 10:
                -> while (num <= 10):
                        print(num)
                        num += 1      2. Incremento: Después de cada iteración, se incrementa el valor de numero en 1.
                \n""")

# Bucle while para imprimir los números del 1 al 10, pero cada número ocupará una línea.
while (num <= 10):
    print(num)
    num += 1            # Incrementar el número en 1

print("""El siguiente bucle WHILE mostrará la secuencia numérica en una sola línea.
      
        Para lograrlo, se aplicará el parámetro  >  end=" " < que, dentro de  > print() <, evita el salto de línea y agrega un espacio entre los números.

        # Inicializar la variable
                numero = 1

        # Bucle while para imprimir los números del 1 al 10 en una sola línea
                while numero <= 10:
                        print(numero, end="(ESPACIO ENTRE COMILLAS) ")  # Mostrar el número en la misma línea con un espacio
                        numero += 1  # Incrementar el número en 1 
      \n\n""")

# Inicializar la variable
numero = 1

# Bucle while para imprimir los números del 1 al 10 en una sola línea
while numero <= 10:
    print(numero, end=" ")  # Mostrar el número en la misma línea con un espacio
    numero += 1  # Incrementar el número en 1






