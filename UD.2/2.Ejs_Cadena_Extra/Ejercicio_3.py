"""
        >>>>>>>    Ejercicios Extra de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extra de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 3: \n")

print ("""
# Solicitar una oración al usuario
    
        phrase = input("Introduce una oración: ")

# Dividir la oración en palabras usando espacios como delimitadores

    -> Dividir la oración: Usamos oracion.split() para dividir la oración en una lista de palabras. 
    
    -> El método .split() utiliza espacios por defecto para separar las palabras.
        
        words = phrase.split()

# Contar el número de palabras

    -> Contar palabras: La función len() nos da el número de elementos en la lista, que corresponde al número de palabras en la oración.
        
        numWords = len(words)

# Mostrar el resultado

        print("La oración tiene", numWords, "palabras.")
""")

# Solicitar una oración al usuario
phrase = input("Introduce una oración: ")

# Dividir la oración en palabras usando espacios como delimitadores
words = phrase.split()

# Contar el número de palabras
numWords = len(words)

# Mostrar el resultado
print("La oración tiene", numWords, "palabras.")
