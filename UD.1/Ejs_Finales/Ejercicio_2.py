"""
        >>>>>>>    Ejercicios Finales   <<<<<<
                                                            """
print (f"\n>>>>>>>    Ejercicios Finales   <<<<<<")                                                           
print ("""Ejercicio 2: Realizar un programa que simule un simule de un cajero automático.
Al iniciar el programa, imprime por pantalla las siguientes opciones:

    Bienvenido al cajero automático
        1. Consultar saldo
        2. Retirar dinero
        3. Ingresar dinero
        4. Salir
    Ingrese una opción:

-> El saldo inicial será de 1000€.
\n""")

print("""
# Saldo inicial
saldo = 1000

# Bucle principal del cajero automático
    
    -> while True:: Un bucle infinito para seguir mostrando el menú hasta que el usuario elija salir.

        while True:    

# Mostrar el menú de opciones
    
    -> print: Muestra el menú de opciones.
      
            print("\nBienvenido al cajero automático")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Ingresar dinero")
            print("4. Salir")
    
# Solicitar al usuario que ingrese una opción
    
    -> input("Ingrese una opción: "): Solicita al usuario que elija una opción del menú.

            opcion = input("Ingrese una opción: ")
    
                if opcion == "1":
        # Consultar saldo
                    print(f"Su saldo actual es: ",saldo,"€")
    
                elif opcion == "2":
        # Retirar dinero
                    reintegro = float(input("Ingrese la cantidad a retirar: "))
                        if reintegro > saldo:
                            print("Fondos insuficientes.")
                        else:
                            saldo -= reintegro
            print(f"Ha retirado", reintegro,"€. Su saldo actual es: ",saldo,"€")
    
                elif opcion == "3":
        # Ingresar dinero
                    ingreso = float(input("Ingrese la cantidad a ingresar: "))
                    saldo += ingreso
                    print(f"Ha ingresado ", ingreso,"€. Su saldo actual es: ", saldo,"€")
    
                elif opcion == "4":
        # Salir
                    print("Gracias por usar el cajero automático. ¡Hasta luego!")
                    break
    
                else:
        # Opción no válida
                    print("Opción no válida. Por favor, ingrese una opción del menú.")
\n\n""")

# Saldo inicial
saldo = 1000

# Bucle principal del cajero automático
    
    # while True:: Un bucle infinito para seguir mostrando el menú hasta que el usuario elija salir.

while True:    

# Mostrar el menú de opciones
    
    # print: Muestra el menú de opciones.
      
    print("\nBienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    
# Solicitar al usuario que ingrese una opción
    
    #input("Ingrese una opción: "): Solicita al usuario que elija una opción del menú.

    opcion = input("Ingrese una opción: \n")
    
    if opcion == "1":
        # Consultar saldo
        print(f"Su saldo actual es: ",saldo,"€")
    
    elif opcion == "2":
        # Retirar dinero
        reintegro = float(input("Ingrese la cantidad a retirar: "))
        if reintegro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= reintegro
            print(f"Ha retirado", reintegro,"€. Su saldo actual es: ",saldo,"€")
    
    elif opcion == "3":
        # Ingresar dinero
        ingreso = float(input("Ingrese la cantidad a ingresar: "))
        saldo += ingreso
        print(f"Ha ingresado ", ingreso,"€. Su saldo actual es: ", saldo,"€")
    
    elif opcion == "4":
        # Salir
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    
    else:
        # Opción no válida
        print("Opción no válida. Por favor, ingrese una opción del menú.\n")