
# Definimos el diccionario
diccionario = {"bolso": "negro", "mando": "blanco", 
               "boligrafo": "azul", "libreta": "roja"}

# Función para buscar un elemento en el diccionario
def buscar(dic, clave):
    if clave in dic:
        return (f'El objeto {clave} es de color {dic[clave]}.')
    else:
        return (f'El objeto {clave} no se encuentra en el diccionario.')

# Solicitamos al usuario que ingrese la clave a buscar
clave_buscar = input("¿Qué objeto deseas buscar? \n")

# Llamamos a la función y mostramos el resultado
resultado = buscar(diccionario, clave_buscar)
print(resultado)
