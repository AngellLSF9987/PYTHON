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

        lista_medias = []                
        for notas_alumno in calificaciones:
        media = sum(notas_alumno)/len(notas_alumno)
        lista_medias.append(media)
        print(lista_medias)
        
        for media_alumno in lista_medias:
        print(f"La nota media del alumno es: {round(media_alumno)}")

print()
     
# Calcular la nota media de cada alumno "class enumerate"

        for i, notas in enumerate(calificaciones):
                suma_notas = sum(notas)
                media = suma_notas / len(notas)
                print(f"La nota media del alumno {i + 1} es: {media:.2f}")
                
                -> .2f - Indica un redondeo 2 decimales.\n""")

# Lista de calificaciones

calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]
    
# # Calcular la nota media de cada alumno

lista_medias = []                
for notas_alumno in calificaciones:
        media = sum(notas_alumno)/len(notas_alumno)
        lista_medias.append(media)
                
for media_alumno in lista_medias:
        print(f"La nota media del alumno es: {round(media_alumno,2)}")
        
print()
      
# Calcular la nota media de cada alumno "class enumerate"
for i, notas in enumerate(calificaciones):
    suma_notas = sum(notas)
    media = suma_notas / len(notas)
    print(f"La nota media del alumno {i + 1} es: {media:.2f}") # .2f - Indica un redondeo 2 decimales.

