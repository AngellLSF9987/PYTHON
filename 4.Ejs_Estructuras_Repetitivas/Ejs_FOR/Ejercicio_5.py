"""
        >>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <  <<<<<<
                                                                                    """

print (f"\n>>>>>>>    Ejercicios de Estructuras Repetitivas. BUCLE  > FOR <   <<<<<<\n")                                                           
print ("""Ejercicio 5: Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. 
Tenemos hasta 3 intentos. 

Simula el proceso con Python:
       -> En caso de acceder, lanza al usuario 'login correcto'. 
       -> Sino, 'llamando al policía'.\n\n""")

print("""
# Definir el PIN secreto
        PIN_SECRETO = "1234"

# Número máximo de intentos
        MAX_INTENTOS = 3

# Proceso de desbloqueo usando un bucle for

        -> for intento in range(MAX_INTENTOS): Utiliza un bucle for para iterar hasta 3 veces (0, 1, 2).

                for intento in range(MAX_INTENTOS):

# Pedir al usuario que introduzca el PIN

        -> input: Solicita al usuario que introduzca el PIN.

                u = input("Introduce el PIN para desbloquear la pantalla: ")

# Verificar si el PIN es correcto
        
        -> if pin_usuario == PIN_SECRETO: Verifica si el PIN ingresado es correcto. Si es correcto, imprime "Login correcto" y termina el bucle con break.

                if u == PIN_SECRETO:
                        print("Login correcto.")
                        break
        -> else: Si el PIN es incorrecto:

                else:
      
        -> if intento < MAX_INTENTOS - 1: Verifica si quedan intentos. Si quedan intentos, informa cuántos quedan.

                        if intento < MAX_INTENTOS - 1:
                                print(f"PIN incorrecto. Te quedan", MAX_INTENTOS - intento - 1, "intentos.")
        
        -> else: Si no quedan más intentos, imprime "Llamando al policía."

                        else:
                                print("Llamando al policía.")\n\n""")

# Definir el PIN secreto
PIN_SECRETO = "1234"

# Número máximo de intentos
MAX_INTENTOS = 3

# Proceso de desbloqueo usando un bucle for
for intento in range(MAX_INTENTOS):
    # Pedir al usuario que introduzca el PIN
        u = input("Introduce el PIN para desbloquear la pantalla: ")
    
    # Verificar si el PIN es correcto
        if u == PIN_SECRETO:
                print("Login correcto.")
                break
        else:
                if intento < MAX_INTENTOS - 1:
                        print(f"PIN incorrecto. Te quedan {MAX_INTENTOS - intento - 1} intentos.")
                else:
                        print("Llamando al policía.")



