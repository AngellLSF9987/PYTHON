"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 2: \n")
print ("""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la 
frase invertida."\n""")

print("""
# Solicitar una frase al usuario

        frase = input("Introduce una frase: ")

# Invertir la frase

    -> frase[::-1]: Esta es una técnica sencilla en Python que usa el slicing (rebanado) de cadenas para invertir la frase. 
                    El tercer parámetro en [::-1] indica que se recorrerá la cadena de forma inversa.
    
        invertida = frase[::-1]

# Mostrar la frase invertida

        print("La frase invertida es:", frase_invertida,".")\n\n""")

# Solicitar una frase al usuario
frase = input("Introduce una frase: ")

# Invertir la frase
invertida = frase[::-1]

# Mostrar la frase invertida
print("La frase invertida es:", invertida,".")
