"""
        >>>>>>>    Ejercicios Diccionarios   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Diccionarios   <<<<<<")                                                           
print (f"\n","Ejercicio: \n")
print ("""
El Comité Olímpico nos ha proporcionado los datos del medallero olímpico de la siguiente manera:

    pais;oro;plata;bronce\n
    Estados Unidos de América;40;44;42\n
    República Popular de China;40;27;24\n
    Japón;20;12;13\n
    
Nuestra empresa necesita mostrar los datos en forma de diccionario, siendo el
resultado esperado así:

{
    'Estados Unidos de América': {'oro': '40', 'plata': '44', 'bronce': '42'}, 
    'República Popular de China': {'oro': '40', 'plata': '27', 'bronce': '24'}, 
    'Japón': {'oro': '20', 'plata': '12', 'bronce': '13'}
}

• Realizar un programa que permita este objetivo.\n""")

print ('''
# Datos del medallero olímpico en formato de texto
medallero_data = """Pais;oro;plata;bronce
Estados Unidos de América;40;44;42
República Popular de China;40;27;24
Japón;20;12;13


# Función para convertir los datos en un diccionario
def convertir_medallero_a_diccionario(data):
    # Crear un diccionario vacío para almacenar los resultados
    medallero = {}
    
    # Separar las líneas del texto
    lineas = data.strip().split('\n')
    
    # Iterar sobre las líneas, empezando desde la segunda (saltando la cabecera)
    for linea in lineas[1:]:
        # Separar los elementos por el separador ';'
        pais, oro, plata, bronce = linea.split(';')
        
        # Agregar los datos al diccionario
        medallero[pais] = {
            'oro': oro,
            'plata': plata,
            'bronce': bronce
        }
    
    return medallero

# Convertir los datos y mostrar el resultado
medallero_dict = convertir_medallero_a_diccionario(medallero_data)

# Mostrar el diccionario
print(medallero_dict)
\n\n''')


# Datos del medallero olímpico en formato de texto
medallero_data = """Pais;oro;plata;bronce
Estados Unidos de América;40;44;42
República Popular de China;40;27;24
Japón;20;12;13
"""

# Función para convertir los datos en un diccionario
def convertir_medallero(data):
    # Crear un diccionario vacío para almacenar los resultados
    medallero = {}
    
    # Separar las líneas del texto
    lineas = data.strip().split('\n')
    
    # Iterar sobre las líneas, empezando desde la segunda (saltando la cabecera)
    for linea in lineas[1:]:
        # Separar los elementos por el separador ';'
        pais, oro, plata, bronce = linea.split(';')
        
        # Agregar los datos al diccionario
        medallero[pais] = {
            'oro': oro,
            'plata': plata,
            'bronce': bronce
        }
    
    return medallero

# Convertir los datos y mostrar el resultado
medallero_dic = convertir_medallero(medallero_data)

# Mostrar el diccionario
print(medallero_dic)
