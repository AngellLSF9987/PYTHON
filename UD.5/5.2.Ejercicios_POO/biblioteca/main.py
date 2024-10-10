from autor import Autor
from libro import Libro

def biblioteca ():
    
    # Instanciar autores

    autor1 = Autor("Gabriel García Márquez", 1927)
    autor2 = Autor("J.K. Rowling", 1965)
    autor3 = Autor("George Orwell", 1903)

    # Instanciar libros

    libro1 = Libro("Cien años de soledad", autor1, 1967)
    libro2 = Libro("El amor en los tiempos del cólera", autor1, 1985)
    libro3 = Libro("Harry Potter y la Piedra Filosofal", autor2, 1997)
    libro4 = Libro("1984", autor3, 1949)
    libro5 = Libro("Rebelión en la granja", autor3, 1945)

    # Alamcenar los libros creados en un lista

    lista_libros = [libro1, libro2, libro3, libro4, libro5]

    # Marcar algunos libros como leídos

    libro1.marcar_como_leido()
    libro5.marcar_como_leido()

    # Comprobar y mostrar la información de los libros

    for libro in lista_libros:
        libro.mostrar_informacion()

    # Mostrar los libros de un autor específico

    print("\n Libros de Gabriel García Márquez:\n")
    for libro in lista_libros:
        if libro.autor == autor1:
            libro.mostrar_informacion()

    print("\n Libros de J.K. Rowling:\n")
    for libro in lista_libros:
        if libro.autor == autor2:
            libro.mostrar_informacion()

    print("\n Libros de George Orwell:\n")
    for libro in lista_libros:
        if libro.autor == autor3:
            libro.mostrar_informacion()


# Ejecutar la calculadora
if __name__ == "__main__":
    biblioteca()

