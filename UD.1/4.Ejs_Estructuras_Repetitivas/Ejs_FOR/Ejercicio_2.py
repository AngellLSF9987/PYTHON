"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <  <<<<<<
                                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <   <<<<<<")                                                           
print (f"\n","Ejercicio 2: Pedir al usuario 5 números y decir si son par o impar.\n")

print("""
        for i in range(5):
                num = int(input("Introduce un número: "))
        if num % 2 == 0:
                print(f"{num} es par.")
        else:
                print(f"{num} es impar.")
\n\n""")

for i in range(5):
        num = int(input("Introduce un número: "))
        if num % 2 == 0:
                print(f"{num} es par.")
        else:
                print(f"{num} es impar.")
