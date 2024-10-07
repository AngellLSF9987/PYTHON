from packages.functions import obtener_fiestas_diciembre, obtener_fiestas_primer

def main():
    
    primer_trimestre = obtener_fiestas_primer()

    print("Fiestas del Primer Trimestre del Año:")
    for fiesta in primer_trimestre:
        print(fiesta)

    print("\nFiestas de Diciembre:")
    fiestas_diciembre = obtener_fiestas_diciembre()
    for fiesta in fiestas_diciembre:
        print(fiesta)

if __name__ == "__main__":
    main()