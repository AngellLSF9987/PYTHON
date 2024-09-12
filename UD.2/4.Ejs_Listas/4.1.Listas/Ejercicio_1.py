"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 1: 

A. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
   Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
   
B. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
   Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
   el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las
   asignaturas de la lista.

C. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
   Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
   nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
   mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
   asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
   por el usuario.

D. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
   Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
   nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
   Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que
   repetir.\n""")

# A. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
#    Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# Lista de asignaturas

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar asignaturas en una sola línea con comas y punto al final

if (asignaturas): 
    print("Asignaturas del curso:", end=" ")

    # Bucle con índice: Recorremos la lista asignaturas_repetir utilizando un bucle for con índices (range(len(repetir))).

    for i in range(len(asignaturas)):
        
    # Condicional para la última asignatura: Verificamos si estamos en la última asignatura (if i == len(asignaturas_repetir) - 1). 
    # Si es así, añadimos un punto (".") al final. Si no, se añade una coma con un espacio (", ").    
        
        if i == len(asignaturas) - 1:
            print(asignaturas[i] + ".")  # Última asignatura con punto final
            
        else:
            
    # Uso de end=" ": En las asignaturas que no son la última, usamos end=" " para que las asignaturas se impriman en la misma línea.
    
            print(asignaturas[i] + ",", end=" ")

# B. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
#    Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
#    el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las
#    asignaturas de la lista.

# Mostrar mensaje personalizado

for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# C. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
#    Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#    nota que ha sacado en cada asignatura, y después las muestre por pantalla con el#
#    mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
#    asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
#    por el usuario.

# Lista vacía para alamcenar las notas

notas = []

# Preguntar la nota por cada asignatura

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? \n"))
    notas.append(nota)

# Mostrar las notas

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}\n")

# D. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
#    Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#    nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
#    Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que
#    repetir.

# Crear una nueva lista para asignaturas a repetir

suspensas = []

# Identificar las asignaturas con nota menor a 5

for i in range(len(asignaturas)):
    if notas[i] < 5:
        suspensas.append(asignaturas[i])

# Mostrar asignaturas a suspensas en una sola línea con comas y punto al final

if suspensas:
    print("Tienes que suspensas las siguientes asignaturas:", end=" ")
    
    # Bucle con índice: Recorremos la lista suspensas utilizando un bucle for con índices (range(len(suspensas))).
    
    for i in range(len(suspensas)):
        
    # Condicional para la última asignatura: Verificamos si estamos en la última asignatura (if i == len(suspensas) - 1). 
    # Si es así, añadimos un punto (".") al final. Si no, se añade una coma con un espacio (", ").    
        
        if i == len(suspensas) - 1:
            print(suspensas[i] + ".")  # Última asignatura con punto final
            
        else:
            
    # Uso de end=" ": En las asignaturas que no son la última, usamos end=" " para que las asignaturas se impriman en la misma línea.
    
            print(suspensas[i] + ",", end=" ")
else:
    print("¡Felicidades! No tienes asignaturas que suspensas.")