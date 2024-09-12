"""
        >>>>>>>    Ejercicios de Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Listas   <<<<<<\n")                                                           
print ("""Ejercicio 6:
Dada esta lista: calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]. Calcula la nota media
de cada alumno y muéstrala por pantalla.

# Lista de calificaciones

        calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]

# Calcular la nota media de cada alumno

        for i, notas in enumerate(calificaciones):
                suma_notas = sum(notas)
                media = suma_notas / len(notas)
                print(f"La nota media del alumno {i + 1} es: {media:.2f}")\n""")

# Lista de calificaciones
calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]

# Calcular la nota media de cada alumno
for i, notas in enumerate(calificaciones):
    suma_notas = sum(notas)
    media = suma_notas / len(notas)
    print(f"La nota media del alumno {i + 1} es: {media:.2f}")
