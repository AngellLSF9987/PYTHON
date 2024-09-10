"""
        >>>>>>>    Ejercicios Clase   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Clase   <<<<<<")                                                           
print (f"\n","Ejercicio 3: \n")
print ("""Crea un programa que pida al usuario una frase y luego:
                    
                    ▻ Convierta toda la frase a minúsculas.
                    ▻ Cuente cuántas veces aparece la letra "a" en la frase.
                    ▻ Imprima la frase sin las vocales.\n""")

print ("""
# Solicitar una frase al usuario
    
            frase = input("Introduce una frase: ")

# Convertir toda la frase a minúsculas

    -> Convertir a minúsculas: Utilizamos el método .lower() para convertir toda la frase a minúsculas.
    
        minus = frase.lower()
        print("Frase en minúsculas:", minus)

# Contar cuántas veces aparece la letra "a"

    -> Contar las "a": Usamos el método .count("a") para contar cuántas veces aparece la letra "a" en la frase ya convertida.

        count = minus.count("a")
        print("La letra 'a' aparece", count, "veces.")

# Crear una nueva frase sin las vocales

    -> Eliminar las vocales: Recorremos la frase con un bucle for, verificamos si cada letra no es una vocal, y si no lo es, 
       la agregamos a la nueva cadena.

        vocales = "aeiou"
        noVocal = ""

        for letra in minus:
            if letra not in vocales:
                noVocal += letra

print("Frase sin vocales:", noVocal)\n""")

# Solicitar una frase al usuario
frase = input("Introduce una frase: ")

# Convertir toda la frase a minúsculas
minus = frase.lower()
print("Frase en minúsculas:", minus)

# Contar cuántas veces aparece la letra "a"
count = minus.count("a")
print("La letra 'a' aparece", count, "veces.")

# Crear una nueva frase sin las vocales
vocales = "aeiou"
noVocales = ""

for letra in minus:
    if letra not in vocales:
        noVocales += letra

print("Frase sin vocales:", noVocales)
