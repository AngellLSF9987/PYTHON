from packages.functions import generar, obtener_fecha

# Función principal ejcutar el programa

def crear():
    num_ganadores, num_clave = generar()
    fecha = obtener_fecha()

    print(f"El boleto ganador es: {num_ganadores} y número clave: {num_clave}")
    print(f"Fecha del boleto:{fecha}")

# Ejecutar el programa

if __name__ == "__main__":
    crear()