"""
        >>>>>>>    Ejercicios Diccionarios   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Diccionarios   <<<<<<")                                                            
print (f"\n","Ejercicio 2: \n")
print ("""

# A. Crear un diccionario de estudiantes con sus calificaciones.

    # Ej. Juan = Matemáticas: 9, Historia: 8, Lengua: 7
    
alumnos = {
      
    "Juan": {"Matemáticas": 9,"Historia": 8,"Lengua": 7},   
    "Ana": {"Matemáticas": 8,"Historia": 9,"Lengua": 9},
    "Loreto": {"Matemáticas": 5,"Historia": 10,"Lengua": 9}
}

## Función para mostrar el registro de alumnos
    
def registro_alumnos(alumnos):
    if (alumnos):    
        print(f"Registro de alumnos inicial:\n",end=" ")

        for i, alumno in enumerate(alumnos):
            if i == len(alumnos) -1:
                print(f"{alumno}.")       
            else:
                print(f"{alumno},", end=" ")
    else:
        print("No existen alumnos registrados.\n")        

### Llamar a la función y mostrar registro de alumnos, sólo nombres.
registro_alumnos(alumnos)
print()
# B. Acceder a una calificación específica.
    
alumno_Juan_Matemáticas = alumnos["Juan"]["Matemáticas"]
print(f"La calificación de Juan en Matemáticas es: {alumno_Juan_Matemáticas}\n")

# C. Mostrar el contenido del diccionario para que quede de la siguiente manera:
#
#   Las notas de Juan son:

#   "Matemáticas": 9
#   "Historia": 8
#   "Lengua": 7

#   La nota media de Juan es: 8.0

#   Las notas de Ana son:

#   "Matemáticas": 8
#   "Historia": 9
#   "Lengua": 9

#   La nota media de Juan es: 8.67

#   Las notas de Juan son:

#   "Matemáticas": 5
#   "Historia": 10
#   "Lengua": 9

#   La nota media de Juan es: 8.0

def notas_alumnos(alumno):
    
    print(f"Las notas de {alumno} son:")
    notas = alumnos[alumno]
    
    for asignatura, nota in notas.items():
        print(f"• '{asignatura}': {nota}")
    media = sum(notas.values()) / len(notas)
    
    print(f"▻ La media de {alumno} es: {media:.2f}\n")

print("Las calificaciones de los alumnos han sido:\n")
notas_alumnos("Juan")
notas_alumnos("Ana")
notas_alumnos("Loreto")

# D. Elimina a Ana del diccionario.

def eliminar_alumno(nombre):
    
    if nombre in alumnos:
        del alumnos[nombre]
        print(f"{nombre} ha sido eliminado/a del diccionario.\n")
        
    else:
        print(f"No se encontró a {nombre} en el regitro de alumnos.\n")
        
eliminar_alumno("Ana")

# Registro Actualizado de Alumnos

registro_alumnos(alumnos)
print()\n\n""")


# A. Crear un diccionario de estudiantes con sus calificaciones.

    # Ej. Juan = Matemáticas: 9, Historia: 8, Lengua: 7
    
alumnos = {
      
    "Juan": {"Matemáticas": 9,"Historia": 8,"Lengua": 7},   
    "Ana": {"Matemáticas": 8,"Historia": 9,"Lengua": 9},
    "Loreto": {"Matemáticas": 5,"Historia": 10,"Lengua": 9}
}

## Función para mostrar el registro de alumnos
    
def registro_alumnos(alumnos):
    if (alumnos):    
        print(f"Registro de alumnos inicial:\n",end=" ")

        for i, alumno in enumerate(alumnos):
            if i == len(alumnos) -1:
                print(f"{alumno}.")       
            else:
                print(f"{alumno},", end=" ")
    else:
        print("No existen alumnos registrados.\n")        

### Llamar a la función y mostrar registro de alumnos, sólo nombres.
registro_alumnos(alumnos)
print()
# B. Acceder a una calificación específica.
    
alumno_Juan_Matemáticas = alumnos["Juan"]["Matemáticas"]
print(f"La calificación de Juan en Matemáticas es: {alumno_Juan_Matemáticas}\n")

# C. Mostrar el contenido del diccionario para que quede de la siguiente manera:
#
#   Las notas de Juan son:

#   "Matemáticas": 9
#   "Historia": 8
#   "Lengua": 7

#   La nota media de Juan es: 8.0

#   Las notas de Ana son:

#   "Matemáticas": 8
#   "Historia": 9
#   "Lengua": 9

#   La nota media de Juan es: 8.67

#   Las notas de Juan son:

#   "Matemáticas": 5
#   "Historia": 10
#   "Lengua": 9

#   La nota media de Juan es: 8.0

def notas_alumnos(alumno):
    
    print(f"Las notas de {alumno} son:")
    notas = alumnos[alumno]
    
    for asignatura, nota in notas.items():
        print(f"• '{asignatura}': {nota}")
    media = sum(notas.values()) / len(notas)
    
    print(f"▻ La media de {alumno} es: {media:.2f}\n")

print("Las calificaciones de los alumnos han sido:\n")
notas_alumnos("Juan")
notas_alumnos("Ana")
notas_alumnos("Loreto")

# D. Elimina a Ana del diccionario.

def eliminar_alumno(nombre):
    
    if nombre in alumnos:
        del alumnos[nombre]
        print(f"{nombre} ha sido eliminado/a del diccionario.\n")
        
    else:
        print(f"No se encontró a {nombre} en el regitro de alumnos.\n")
        
eliminar_alumno("Ana")

# Registro Actualizado de Alumnos

registro_alumnos(alumnos)
print()

