"""
        >>>>>>>    Ejercicios de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 6: \n")
print ("""
# A. Crea una tupla anidada para representar una pequeña biblioteca.

# Cada elemento de la tupla será un libro con título, autor y año de
# publicación.

# • Cien años de soledad, Gabriel García Márquez, 1967
# • El señor de los anillos, J.R.R. Tolkien, 1954
# • La sombra del viento, Carlos Ruiz Zafón, 2001
# • Orgullo y prejuicio, Jane Austen, 1813
# • 1984, George Orwell, 1949
# • Harry Potter y las Reliquias de la Muerte, J.K. Rowling, 2007
# • Ángeles y demonios, Dan Brown, 2000

                biblioteca = (
                        ("• Cien años de soledad", "Gabriel García Márquez", 1967),
                        ("• El señor de los anillos", "J.R.R. Tolkien", 1954),
                        ("• La sombra del viento", "Carlos Ruiz Zafón", 2001),
                        ("• Orgullo y prejuicio", "Jane Austen", 1813),
                        ("• 1984", "George Orwell", 1949),
                        ("• Harry Potter y las Reliquias de la Muerte", "J.K. Rowling", 2007),
                        ("• Ángeles y demonios", "Dan Brown", 2000),
                )

# B. Imprime todos los libros publicados después de 2000

                print("Libros publicados después del 2000:\n")
                for libro in biblioteca:
                        titulo, autor, año = libro
                        if año > 2000:
                                print(f"{titulo},{autor},{año}")

print()\n""")

# A. Crea una tupla anidada para representar una pequeña biblioteca.

# Cada elemento de la tupla será un libro con título, autor y año de
# publicación.

# • Cien años de soledad, Gabriel García Márquez, 1967
# • El señor de los anillos, J.R.R. Tolkien, 1954
# • La sombra del viento, Carlos Ruiz Zafón, 2001
# • Orgullo y prejuicio, Jane Austen, 1813
# • 1984, George Orwell, 1949
# • Harry Potter y las Reliquias de la Muerte, J.K. Rowling, 2007
# • Ángeles y demonios, Dan Brown, 2000

biblioteca = (
        ("• Cien años de soledad", "Gabriel García Márquez", 1967),
        ("• El señor de los anillos", "J.R.R. Tolkien", 1954),
        ("• La sombra del viento", "Carlos Ruiz Zafón", 2001),
        ("• Orgullo y prejuicio", "Jane Austen", 1813),
        ("• 1984", "George Orwell", 1949),
        ("• Harry Potter y las Reliquias de la Muerte", "J.K. Rowling", 2007),
        ("• Ángeles y demonios", "Dan Brown", 2000),
)

# B. Imprime todos los libros publicados después de 2000

print("Libros publicados después del 2000:\n")
for libro in biblioteca:
        titulo, autor, año = libro
        if año > 2000:
                print(f"{titulo},{autor},{año}")
                
print()
