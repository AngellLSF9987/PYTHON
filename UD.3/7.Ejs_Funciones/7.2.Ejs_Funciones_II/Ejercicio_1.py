"""
        >>>>>>>    Ejercicio Funciones II   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Funciones II  <<<<<<")                                                            
print (f"\n","Ejercicio 1: \n")
print ("""Crea un programa que introduciendo una lista como argumento de una función.
Realice:
a. Suma de todos los elementos de la lista
b. La media
c. El número mayor y menor de la lista 

# Función para calcular la suma, media, mayor y menor de una lista

def operaciones(lista):
    
    # Suma
    suma = sum(lista)
    
    # Media
    media = suma / len(lista)
    
    # Mayor y menor
    
    mayor = max(lista)
    menor = min(lista)
    
    # Mostrar resultados
    
    print(f"Suma de los items:{suma}")
    print(f"Media de los items:{media}")
    print(f"Mayor de los items:{mayor}")
    print(f"Menor de los items:{menor}")
    
items = [10,20,25,50,100]
operaciones(items)              \n""")


# Función para calcular la suma, media, mayor y menor de una lista

def operaciones(lista):
    
    # Suma
    suma = sum(lista)
    
    # Media
    media = suma / len(lista)
    
    # Mayor y menor
    
    mayor = max(lista)
    menor = min(lista)
    
    # Mostrar resultados
    
    print(f"Suma de los items:{suma}")
    print(f"Media de los items:{media}")
    print(f"Mayor de los items:{mayor}")
    print(f"Menor de los items:{menor}")
    
items = [10,20,25,50,100]
operaciones(items)