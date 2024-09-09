"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <  <<<<<<
                                                                                    """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <   <<<<<<")                                                           
print (f"\n","Ejercicio 3: Pedir al usuario 5 números y decir si son par o impar.\n")

print("""
        # Inicializar el contador de números
                contador = 0
      
        # Bucle while: Se ejecuta 5 veces, ya que el contador comienza en 0 y aumenta con cada iteración.
        
                while (contador < 5):
                numero = int(input("Introduce un número: "))  # Pedir un número al usuario
    
        # Condicional: Para cada número ingresado, el programa verifica si es divisible entre 2 para determinar si es par o impar.
                
                if (numero % 2 == 0):
                        print(f"El número {numero} es par.")
                else:
                        print(f"El número {numero} es impar.")
    
        # Incrementar el contador
                contador += 1 \n\n""")

# Inicializar el contador de números
contador = 0

# Bucle while que se repite 5 veces
while (contador < 5):
    numero = int(input("Introduce un número: "))  # Pedir un número al usuario
    
    # Comprobar si el número es par o impar
    if (numero % 2 == 0):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
    
    # Incrementar el contador
    contador += 1
