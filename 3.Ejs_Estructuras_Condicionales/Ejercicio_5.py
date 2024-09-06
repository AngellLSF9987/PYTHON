"""
        >>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<
                                                                        """

print (f"\n>>>>>>>    Ejercicios de Estructuras Condicionales   <<<<<<")                                                           
print ("""Ejercicio 5: Crear un programa que pida al usuario su DNI sin letra, y la letra.
                -> Calcular si el DNI es correcto. 
                -> Para calcular la letra del DNI, el número entero del DNI modulo 23 y el resto es la letra.\n""")

print (f" RESTO  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |")
print (f" LETRA  | T | R | W | A | G | M | Y | F | P | D | X | B | N | J | Z | S | Q | V | H | L | C | K | E |\n\n")

print ("""Pedir al usuario el número del DNI (sin letra) y la letra:
                
                -> dni = int(input("Introduce el número de tu DNI (sin letra): "))
                -> letra = input("Introduce la letra de tu DNI: ").upper()

        # El atributo > .upper() < Se encargará de convertir la letra o caracter, introducido por el usuario, en mayúscula\n\n""")

# Pedir al usuario el número del DNI (sin letra) y la letra
dni = int(input("Introduce el número de tu DNI (sin letra): "))
letra = input("Introduce la letra de tu DNI: ").upper()

print (f"Calcular el índice para la letra correcta:   ->  indice = dni % 23  \n\n")

# Calcular el índice para la letra correcta
indice = dni % 23


print('''Asignar la letra correspondiente al índice usando condicionales
                        if indice == 0:
                                correcta = "T"
                        elif indice == 1:
                                correcta = "R"
                        elif indice == 2:
                                correcta = "W"
                        elif indice == 3:
                                correcta = "A"
                        elif indice == 4:
                                correcta = "G"
                        elif indice == 5:
                                correcta = "M"
                        elif indice == 6:
                                correcta = "Y"
                        elif indice == 7:
                                correcta = "F"
                        elif indice == 8:
                                correcta = "P"
                        elif indice == 9:
                                correcta = "D"
                        elif indice == 10:
                                correcta = "X"
                        elif indice == 11:
                                correcta = "B"
                        elif indice == 12:
                                correcta = "N"
                        elif indice == 13:
                                correcta = "J"
                        elif indice == 14:
                                correcta = "Z"
                        elif indice == 15:
                                correcta = "S"
                        elif indice == 16:
                                correcta = "Q"
                        elif indice == 17:
                                correcta = "V"
                        elif indice == 18:
                                correcta = "H"
                        elif indice == 19:
                                correcta = "L"
                        elif indice == 20:
                                correcta = "C"
                        elif indice == 21:
                                correcta = "K"
                        elif indice == 22:
                                correcta = "E"''')

# Asignar la letra correspondiente al índice usando condicionales
if indice == 0:
        correcta = "T"
elif indice == 1:
        correcta = "R"
elif indice == 2:
        correcta = "W"
elif indice == 3:
        correcta = "A"
elif indice == 4:
        correcta = "G"
elif indice == 5:
        correcta = "M"
elif indice == 6:
        correcta = "Y"
elif indice == 7:
        correcta = "F"
elif indice == 8:
        correcta = "P"
elif indice == 9:
        correcta = "D"
elif indice == 10:
        correcta = "X"
elif indice == 11:
        correcta = "B"
elif indice == 12:
        correcta = "N"
elif indice == 13:
        correcta = "J"
elif indice == 14:
        correcta = "Z"
elif indice == 15:
        correcta = "S"
elif indice == 16:
        correcta = "Q"
elif indice == 17:
        correcta = "V"
elif indice == 18:
        correcta = "H"
elif indice == 19:
        correcta = "L"
elif indice == 20:
        correcta = "C"
elif indice == 21:
        correcta = "K"
elif indice == 22:
        correcta = "E"

print("""Comprobar si la letra es correcta:
                
                if letra == correcta:
                        print("El DNI es correcto.")
                else:
                        print(f"El DNI es incorrecto. La letra correcta debería ser: ",correcta,".\n")""")

# Comprobar si la letra es correcta
if letra == correcta:
        print("El DNI es correcto.")
else:
        print(f"El DNI es incorrecto. La letra correcta debería ser: ",correcta,".\n")

