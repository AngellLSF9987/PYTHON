"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 3: \n")
print ("""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula, 
y después muestre por pantalla la misma frase, pero con la vocal introducida en mayúscula."\n""")

print("""
# Solicitar una frase al usuario

    frase = input("Introduce una frase: ")

# Solicitar una vocal en minúscula

    vocal = input("Introduce una vocal en minúscula: ")

# Verificar que la entrada sea una vocal y tenga solo un carácter

    -> Validación: Se verifica que la vocal tenga solo un carácter y sea una vocal válida (a, e, i, o, u).

            if len(vocal) == 1 and vocal in "aeiou":
    
# Crear una nueva frase con la vocal en mayúscula
    
                modificada = ""
                
                for letra in frase:
                    if letra == vocal:
                        modificada += letra.upper()  # Convertir la vocal a mayúscula
                    else:
                        modificada += letra  # Mantener las demás letras igual
    
    # Mostrar la frase modificada
    
                print("La frase modificada es:", modificada,".\n")
            
            else:
    
                print("Debes introducir una vocal en minúscula.\n")\n\n""")

# Solicitar una frase al usuario

frase = input("Introduce una frase: \n")

# Solicitar una vocal en minúscula

vocal = input("Introduce una vocal en minúscula: \n")

# Verificar que la entrada sea una vocal y tenga solo un carácter

if len(vocal) == 1 and vocal in "aeiou":
    # Crear una nueva frase con la vocal en mayúscula
    frase_modificada = ""
    for letra in frase:
        if letra == vocal:
            frase_modificada += letra.upper()  # Convertir la vocal a mayúscula
        else:
            frase_modificada += letra  # Mantener las demás letras igual
    
    # Mostrar la frase modificada
    print("La frase modificada es:", frase_modificada)
else:
    print("Debes introducir una vocal en minúscula.\n")

