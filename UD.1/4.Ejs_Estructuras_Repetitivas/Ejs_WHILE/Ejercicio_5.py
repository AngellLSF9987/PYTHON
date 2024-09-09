"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <  <<<<<<
                                                                                    """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > WHILE <   <<<<<<")                                                           
print ("""Ejercicio 5: Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. 
Tenemos hasta 3 intentos. 

Simula el proceso con Python:
       -> En caso de acceder, lanza al usuario 'login correcto'. 
       -> Sino, 'llamando al policía'.\n""")

print("""
        # Definir el PIN secreto
                PIN_SECRETO = "1234"

        # Inicializar el número de intentos
                intentos = 0

        # Bucle while para los intentos
                while intentos < 3:
        # Pedir al usuario que ingrese el PIN. Variable > u <
                u = input("Introduce el PIN para desbloquear: ")

        # Verificar si el PIN es correcto
                if u == PIN_SECRETO:
                        print("Login correcto")
                        break  # Salir del bucle si el PIN es correcto
                 else:
                        intentos += 1
                        print(f"PIN incorrecto. Te quedan", 3-intentos, "intentos.")

        # Si se agotaron los intentos
                if intentos == 3:
                        print("Llamando a la policía.")""")

# Definir el PIN secreto
PIN_SECRETO = "1234"

# Inicializar el número de intentos
intentos = 0

# Bucle while para los intentos
while intentos < 3:

# Pedir al usuario que ingrese el PIN
        u = input("Introduce el PIN para desbloquear: \n")

# Verificar si el PIN es correcto
        if u == PIN_SECRETO:
                print("Login correcto")
                break  # Salir del bucle si el PIN es correcto
        else:
                intentos += 1
                print(f"PIN incorrecto. Te quedan", 3 - intentos, "intentos.\n")

# Si se agotaron los intentos
if intentos == 3:
    print("Llamando a la policía.\n")

