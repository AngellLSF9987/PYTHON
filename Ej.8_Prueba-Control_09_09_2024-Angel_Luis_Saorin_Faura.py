# Bucle principal del cajero automático
    
    # while True:: Un bucle infinito para seguir mostrando el menú hasta que el usuario elija salir.

while True:    

# Mostrar el menú de opciones
    
    # print: Muestra el menú de opciones.

    print("1. Comenzar Programa")
    print("2. Imprimir Números")
    print("3. Salir")
    
# Solicitar al usuario que ingrese una opción
    
    #input("Ingrese una opción: "): Solicita al usuario que elija una opción del menú.

    opcion = input("Ingrese una opción: \n")
    
    if opcion == "1":
        # Consultar saldo
        print(f"Comenzamos!")
    
    elif opcion == "2":
       print("Listado de números: 1, 2, 3, 4..")
    
    elif opcion == "3":
         # Salir
        print("¡Hasta la próxima!")
        break       
    
    else:
        # Opción no válida
        print("Opción incorrecta. Debe ingresar 1, 2 o 3.\n")