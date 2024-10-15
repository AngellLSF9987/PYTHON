class Material:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def mostrar_contenido(self):
        """
        - Muestra las características del material.
        - Este método ya funciona además comos método __str__"""
        return f"Material: {self.nombre}, Color: {self.color}"
    
class Estuche:
    def __init__(self, color):
        self.color = color
        self.materiales = []

    def contenedor(self, lista_materiales):
        """Añade un lista de materiales al estuche."""
        self.materiales.extend(lista_materiales)

    def mostrar_contenido_estuche(self):
        print(f"Estuche de color: {self.color}")
        for material in self.materiales:
            print(material.mostrar_contenido())

def main():
    material1 = Material("Lápiz", "Amarillo")
    material2 = Material("Bolígrafo", "Azul")
    material3 = Material("Libreta", "Roja")

    lista_materiales = [material1, material2, material3]

    estuche = Estuche("Verde")

    estuche.contenedor(lista_materiales)

    estuche.mostrar_contenido_estuche()


if __name__ == "__main__":
    main()