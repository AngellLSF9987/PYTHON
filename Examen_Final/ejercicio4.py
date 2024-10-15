"""Crea un programa para controlar la edad de una persona. 

El programa debe controlar si es mayor de edad para dejarlo entrar en la discoteca. (0.5 puntos)

Pedir la edad por teclado
Hacer el programa con funciones"""

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
def main():
    edad = int(input("¿Qué edad figura en su DNI?\n"))
    if es_mayor_edad(edad):
        print("Puedes pasar")
    else:
        print(f"No eres mayor de {edad}")

    

if __name__ == "__main__":
    main()

