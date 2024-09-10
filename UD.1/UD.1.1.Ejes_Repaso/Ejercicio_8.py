"""
        >>>>>>>    Ejercicios Repaso   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Repaso   <<<<<<")                                                           
print (f"\n","Ejercicio 8: \n")
print ("""Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 
y cuantossuspensos."\n""")

# Inicializar contadores
aprobados = 0
suspensos = 0

# Solicitar 10 notas
for i in range(10):
        
# Pedir al usuario que ingrese una nota
        nota = float(input(f"Ingrese la nota del alumno {i + 1}: \n"))
# Verificar que la nota esté en el rango válido (0-10)
        if (0 <= nota <= 10):
                break
        else:
                print("La nota debe estar entre 0 y 10. Inténtelo de nuevo.")
    
    # Contar aprobados y suspensos
if nota >= 7:
        aprobados += 1
else:
        suspensos += 1

# Mostrar resultados
print("Cantidad de alumnos aprobados (nota >= 7):", aprobados,".\n")
print("Cantidad de alumnos suspendidos (nota < 7):", suspensos,".\n")
