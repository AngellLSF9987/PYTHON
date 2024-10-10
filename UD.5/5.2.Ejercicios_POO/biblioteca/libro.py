from autor import Autor
# Clase Libro

class Libro:
    def __init__(self, titulo, autor, ano_publicacion, leido=False):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.leido = leido

    # Método para comprobar si el libro ha sido leído

    def comprobar_leido(self):
        """- Devuelve si el libro ha sido leído."""
        return self.leido
            
    # Método para marcar un libro como leído

    def marcar_como_leido(self):
        """- Cambia el estado del libro a leído (True)"""
        self.leido = True

    # Método para mostrar la información del libro

    def mostrar_informacion(self):
        """- Muestra los detalles del libro, incluyendo si ha sido leído o no."""
        leido_str = "Leído" if self.leido else "No leído"
        print(f"\n- Título: {self.titulo}\n- Año de Publicación: {self.ano_publicacion}\n- Estado: {leido_str}\n")