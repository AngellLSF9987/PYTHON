from packages.operaciones import sumar,restar,dividir,multiplicar

def mostrar_menu():
    print("Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def elegir_operacion(opcion, num1, num2):
    if opcion == '1':
        return sumar(num1, num2)
    elif opcion == '2':
        return restar(num1, num2)
    elif opcion == '3':
        return multiplicar(num1, num2)
    elif opcion == '4':
        return dividir(num1, num2)
    else:
        return "Opción no válida"