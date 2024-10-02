import random
import string

# Función para generar la contraseña segura.

def generar(longitud):
    """
    Genera una contraseña con:
        - string.ascii_letters - letras(mayúsculas y minúsculas), tomando como referencia la tabla ASCII
        - string.digits - números del 0 al 9
        - string.puntuctuation - Caracteres especiales: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "" # Usamos una cadena vacía para ir añadiendo caracteres

    for i in range(longitud):
        contraseña += random.choice(caracteres) # Agregamos cada caracter
    
    return contraseña