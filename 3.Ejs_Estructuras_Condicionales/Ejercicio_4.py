"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                                        """
print (f"\n>>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<\n\n")                                                           
print ("""Ejercicio 4: La pizzería “Pizza Paradiso” ofrece pizzas vegetarianas y no
vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
a continuación.\n""")
print(f"   • Ingredientes vegetarianos: Pimiento, cebolla, champiñones, ... ")
print(f"   • Ingredientes no vegetarianos: Pepperoni, Jamón, atún, ... \n\n")
print("""Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o
no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija.\n""")
print("""El programa debe preguntar al usuario cuantos ingredientes quiere elegir, y
mostrárselos, hasta un total de 3 ingredientes.\n""")
print("""Se debe mostrar el contenido de la pizza: Tomate, queso y los ingredientes
extras.\n""")

print ("""El programa contará con dos variables que almacenarán si la pizza es vegetariana o no
                -> Variable para pizza vegetariana > v <
                -> Variable para el resto de pizzas > r <""")

print ("""El programa contará con dos variables que almacenarán, en una cadena de caracteres, los ingredientes posibles para cada tipo de pizza:\n
                -> ingredientesVeg = 'Pimiento, Cebolla, Champiñones'
                -> ingredientesRes = 'Pepperoni, Jamón, Atún'""")

print ("""El programa pedirá al usuario que elija entre vegetariana o no. Dicha respuesta quedará almacenada en una variable > u <\n""")

print (f"u = input(Realice su pedido: (Introduzca 'v' para vegetariana, 'r' para el resto))")

print (f"Por último, el programa hará el tratamiento respectivo a las condicionantes interpuestas para el resultado del ejercicio.\n\n")

print("""
# Declaración de las opciones para pizza vegetariana o no vegetariana

        vegetariana = "v"
        resto = "r"

# Ingredientes disponibles para cada tipo de pizza con valores numéricos

        ingredientesVeg = "Pimiento, Cebolla, Champiñones"
        ingredientesRes = "Pepperoni, Jamón, Atún"

# Petición al usuario para elegir el tipo de pizza

        u = input("Realice su pedido (v para vegetariana, r para resto): ")

if (u == vegetariana):
    print("Ha seleccionado una pizza vegetariana.")
    print("Puede elegir entre los siguientes ingredientes:")
    print("1: Pimiento")
    print("2: Cebolla")
    print("3: Champiñones")
    
    # Preguntar al usuario cuántos ingredientes quiere
    numIng = int(input("¿Cuántos ingredientes quiere en su pizza? (1-3): "))
    
    if (numIng == 1):
        num = int(input("Elija un ingrediente (1-3): "))
        if (num == 1):
            ing1 = "Pimiento"
        elif (num == 2):
            ing1 = "Cebolla"
        elif (num == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")
      
        if (ing1):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ".")
    
    elif (numIng == 2):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pimiento"
        elif (num1 == 2):
            ing1 = "Cebolla"
        elif (num1 == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pimiento"
        elif (num2 == 2):
            ing2 = "Cebolla"
        elif (num2 == 3):
            ing2 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")
      
        if (ing1 and ing2):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ".")
    
    elif (numIng == 3):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        num3 = int(input("Elija el tercer ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pimiento"
        elif (num1 == 2):
            ing1 = "Cebolla"
        elif (num1 == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pimiento"
        elif (num2 == 2):
            ing2 = "Cebolla"
        elif (num2 == 3):
            ing2 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num3 == 1):
            ing3 = "Pimiento"
        elif (num3 == 2):
            ing3 = "Cebolla"
        elif (num3 == 3):
            ing3 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2 and ing3):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ", " + ing3 + ".")
    
    else:
        print("Número de ingredientes no válido.")
        
elif u == resto:
    print("Ha seleccionado una pizza no vegetariana.")
    print("Puede elegir entre los siguientes ingredientes:")
    print("1: Pepperoni")
    print("2: Jamón")
    print("3: Atún")
    
    # Preguntar al usuario cuántos ingredientes quiere
    numIng = int(input("¿Cuántos ingredientes quiere en su pizza? (1-3): "))
    
    if (numIng == 1):
        num = int(input("Elija un ingrediente (1-3): "))
        if (num == 1):
            ing1 = "Pepperoni"
        elif (num == 2):
            ing1 = "Jamón"
        elif (num == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ".")
    
    elif (numIng == 2):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pepperoni"
        elif (num1 == 2):
            ing1 = "Jamón"
        elif (num1 == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pepperoni"
        elif (num2 == 2):
            ing2 = "Jamón"
        elif (num2 == 3):
            ing2 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ".")
    
    elif (numIng == 3):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        num3 = int(input("Elija el tercer ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pepperoni"
        elif (num1 == 2):
            ing1 = "Jamón"
        elif (num1 == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pepperoni"
        elif (num2 == 2):
            ing2 = "Jamón"
        elif (num2 == 3):
            ing2 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num3 == 1):
            ing3 = "Pepperoni"
        elif (num3 == 2):
            ing3 = "Jamón"
        elif (num3 == 3):
            ing3 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2 and ing3):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ", " + ing3 + ".")
    
    else:
        print("Número de ingredientes no válido.")
        
else:
    print("Opción no válida. Debe elegir 'v' para vegetariana o 'r' para resto.")\n\n""")

# Declaración de las opciones para pizza vegetariana o no vegetariana

vegetariana = "v"
resto = "r"

# Ingredientes disponibles para cada tipo de pizza con valores numéricos

ingredientesVeg = "Pimiento, Cebolla, Champiñones"
ingredientesRes = "Pepperoni, Jamón, Atún"

# Petición al usuario para elegir el tipo de pizza

u = input("Realice su pedido (v para vegetariana, r para resto): ")

if (u == vegetariana):
    print("Ha seleccionado una pizza vegetariana.")
    print("Puede elegir entre los siguientes ingredientes:")
    print("1: Pimiento")
    print("2: Cebolla")
    print("3: Champiñones")
    
    # Preguntar al usuario cuántos ingredientes quiere
    numIng = int(input("¿Cuántos ingredientes quiere en su pizza? (1-3): "))
    
    if (numIng == 1):
        num = int(input("Elija un ingrediente (1-3): "))
        if (num == 1):
            ing1 = "Pimiento"
        elif (num == 2):
            ing1 = "Cebolla"
        elif (num == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")
      
        if (ing1):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ".")
    
    elif (numIng == 2):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pimiento"
        elif (num1 == 2):
            ing1 = "Cebolla"
        elif (num1 == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pimiento"
        elif (num2 == 2):
            ing2 = "Cebolla"
        elif (num2 == 3):
            ing2 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")
      
        if (ing1 and ing2):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ".")
    
    elif (numIng == 3):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        num3 = int(input("Elija el tercer ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pimiento"
        elif (num1 == 2):
            ing1 = "Cebolla"
        elif (num1 == 3):
            ing1 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pimiento"
        elif (num2 == 2):
            ing2 = "Cebolla"
        elif (num2 == 3):
            ing2 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (num3 == 1):
            ing3 = "Pimiento"
        elif (num3 == 2):
            ing3 = "Cebolla"
        elif (num3 == 3):
            ing3 = "Champiñones"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2 and ing3):
            print("Su pizza vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ", " + ing3 + ".")
    
    else:
        print("Número de ingredientes no válido.")
        
elif u == resto:
    print("Ha seleccionado una pizza no vegetariana.")
    print("Puede elegir entre los siguientes ingredientes:")
    print("1: Pepperoni")
    print("2: Jamón")
    print("3: Atún")
    
    # Preguntar al usuario cuántos ingredientes quiere
    numIng = int(input("¿Cuántos ingredientes quiere en su pizza? (1-3): "))
    
    if (numIng == 1):
        num = int(input("Elija un ingrediente (1-3): "))
        if (num == 1):
            ing1 = "Pepperoni"
        elif (num == 2):
            ing1 = "Jamón"
        elif (num == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ".")
    
    elif (numIng == 2):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pepperoni"
        elif (num1 == 2):
            ing1 = "Jamón"
        elif (num1 == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pepperoni"
        elif (num2 == 2):
            ing2 = "Jamón"
        elif (num2 == 3):
            ing2 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ".")
    
    elif (numIng == 3):
        num1 = int(input("Elija el primer ingrediente (1-3): "))
        num2 = int(input("Elija el segundo ingrediente (1-3): "))
        num3 = int(input("Elija el tercer ingrediente (1-3): "))
        if (num1 == 1):
            ing1 = "Pepperoni"
        elif (num1 == 2):
            ing1 = "Jamón"
        elif (num1 == 3):
            ing1 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num2 == 1):
            ing2 = "Pepperoni"
        elif (num2 == 2):
            ing2 = "Jamón"
        elif (num2 == 3):
            ing2 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (num3 == 1):
            ing3 = "Pepperoni"
        elif (num3 == 2):
            ing3 = "Jamón"
        elif (num3 == 3):
            ing3 = "Atún"
        else:
            print("Número de ingrediente no válido.")

        if (ing1 and ing2 and ing3):
            print("Su pizza no vegetariana tendrá: Tomate, Queso, " + ing1 + ", " + ing2 + ", " + ing3 + ".")
    
    else:
        print("Número de ingredientes no válido.")
        
else:
    print("Opción no válida. Debe elegir 'v' para vegetariana o 'r' para resto.")