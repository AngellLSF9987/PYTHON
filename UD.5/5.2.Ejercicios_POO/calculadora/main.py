# main.py
from menu import mostrar_menu,elegir_operacion

def calculadora():
    opcion = ''

    while opcion != '5':
        mostrar_menu()

        opcion = input("Elige una operación (1/2/3/4/5(salir)): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            resultado = elegir_operacion(opcion, num1, num2)
            print(f"Resultado: {resultado}")
        
        elif opcion == '5':
            print(elegir_operacion(opcion, None, None)) # Muestra el mensaje de cierre
        else:
            print("Opción no válida")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
