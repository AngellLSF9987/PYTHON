"""
        >>>>>>>    Ejercicio Funciones II   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones II  <<<<<<")                                                            
print (f"\n","Ejercicio 2: \n")
print (""" Crea un programa de cifrado y descifrado, utilizando el Método Cesar. Que consiste en
desplazar la letra original x puestos hacia la derecha.

a. Por ejemplo, utilizando la frase: El perro y haciendo 2 desplazamientos a la
derecha quedaría Gn rgttq.

b. Recordar que Python es Case Sensitive (distingue entre mayúsculas y
minúsculas)

c. Se puede elegir el desplazamiento que se quiera  

        A B C D E 
        C D E F G
        A B C D E       

# Función cifrado utilizando el Método César

def cesar(text, desplazamiento)

    resultado = ""

    # Iterar caracteres introducidos
    
    for letra in texto:
        if letra.isalpha(): # Verficar si es una letra
            codigo = ord(letra)
            base = ord('A') if letra.isupper() else ord('a') # Comprueba y establece si es mayúscula o minúscula
        
            resultado += chr((codigo - base + desplazamiento) % 26 +base) # Aplica el desplazamiento
        
        else:
            resultado += letra # Mantiene los espacios y caracteres que no son letras.
        
    return resultado

        # Descifrar Cesar
        
def descifrar(texto, desplazamiento):
    return cesar(texto, -desplazamiento) # Invierte el desplazamiento para descifrar
        
###### USO ######

texto = input(f"Introduzca un texto para cifrar:\n")    
desplazamiento = int(input(f"Introduce el desplazamiento:\n"))

cifrado = cesar(texto, desplazamiento)

print(f"Texto cifrado: {cifrado}\n")

descifrado = descifrar(cifrado, desplazamiento)

print(f"Texto descifrado: {descifrado}\n")              \n""")

# Función cifrado utilizando el Método César

def cesar(texto, desplazamiento):

    resultado = ""

    # Iterar caracteres introducidos
    
    for letra in texto:
        if letra.isalpha(): # Verficar si es una letra
            codigo = ord(letra)
            base = ord('A') if letra.isupper() else ord('a') # Comprueba y establece si es mayúscula o minúscula
        
            resultado += chr((codigo - base + desplazamiento) % 26 +base) # Aplica el desplazamiento
        
        else:
            resultado += letra # Mantiene los espacios y caracteres que no son letras.
        
    return resultado

        # Descifrar Cesar
        
def descifrar(texto, desplazamiento):
    return cesar(texto, -desplazamiento) # Invierte el desplazamiento para descifrar
        
###### USO ######

texto = input(f"Introduzca un texto para cifrar:\n")    
desplazamiento = int(input(f"Introduce el desplazamiento:\n"))

cifrado = cesar(texto, desplazamiento)

print(f"Texto cifrado: {cifrado}\n")

descifrado = descifrar(cifrado, desplazamiento)

print(f"Texto descifrado: {descifrado}\n")
