"""
        >>>>>>>    Ejercicio Extra de Tuplas y Listas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios de Tuplas   <<<<<<")                                                            
print (f"\n","Ejercicio Extra: \n")
print ("""
#                        LORETIX

# Crear un programa para gestionar la plataforma de video LORETIX.

    # A. Crear una lista de usuarios con sus contraseñas para poder acceder a la
    #    plataforma, y una para el administrador. (Lista con tuplas anidadas)

    #    a. El usuario tendrá acceso a unas opciones, mientras que el
    #       administrador a otras.

users = [
    ("client1","password1"),
    ("client2","password2"),
    ("admin","admin") # El usuario administrador tiene su propio acceso
]


    # B. Crear una lista de películas: Define una lista llamada cartelera y agrega
    #    al menos 5 películas diferentes. Por ejemplo: Nombre, genero, duración.
    
films = [
    ("The Avengers","Ciencia Ficción",2012),
    ("Expediente Warren: The Conjuring","Terror",2013),
    ("El Señor de los Anillos: La Comunidad del Anillo","Ciencia Ficción",2001),
    ("Una Proposición Indecente","Drama",1993),
    ("Moana Vahiana","Infantil",2016)
]

    # C. Menú con las diferentes opciones.

     #   Usuario:

     #       A. Buscar película por título.
     #       B. Buscar películas por género.
     #       C. Cambiar contraseña de usuario
     #       D. Crear listas de películas favoritas que se quiere ver.
     #       E. Mostrar la lista de películas favoritas.

     #   Administrador:

     #       A. Agregar una nueva película.
     #       B. Modificar el contenido de la lista de películas.
     #       C. Eliminar una película de la lista.
     
# Plantear Inicio de Sesión para diferenciar el rol de cliente y admin.

user = input("Ingrese su nombre de usuario:\n")
password = input("Ingrese su contraseña:\n")

# Comparar credenciales de usuario.

if(user, password) in users:
    if user == "admin":
        es_admin = True
    else:
        es_admin = False
else:
    print("Algo ha ocurrido...Las credenciales dadas no existen en nuestra base de datos.")
    es_admin = False
    
# Menu si es cliente o administrador

if es_admin:
    option = ""
    
    # Menú ADMIN
    
    while option != "S":
        print("\nMenú Administrador.\n")
        print("A. Mostrar Lista de Películas en Cartelera.\n")        
        print("B. Agregar una nueva película.\n")
        print("C. Modificar el contenido de la lista de películas.\n")
        print("D. Eliminar una película de la lista.\n")
        print("S. Salir.\n")
        option = input("Seleccione una de las opciones disponibles:\n ").upper()
    
    # OPCIÓN A: MOSTRAR LISTA COMPLETA DE PELÍCULAS
    
    if option == "A":
        print("\nListado de Películas en Cartelera.\n")
        for film in films:
            print(film)
    
    # OPCIÓN B: AGREGAR UNA PELÍCULA
    
    elif option == "B":
        name = input("¿Nombre de la película?\n")
        gender = input("¿Género de la película?\n")
        date = int(input("¿Fecha lanzamiento de la película?\n"))
        films.append((name,gender,date))
        print("Película agregada correctamente!\n")
        
    # OPCIÓN C: MODIFICAR UNA PELÍCULA
    
    elif option == "C":
        name = input("Ingrese el título de la película que va a modificar:\n")
        for i, film in enumerate(films):
            if film[0].lower == name.lower():
                new_name = input("Ingrese nuevo título:\n")
                new_gender = input("Ingrese nuevo género:\n")
                new_date = input("Ingrese nueva fecha de lanzamiento:\n")
                films[i] = (new_name, new_gender, new_date)
                print("Película modificada correctamente!\n")
                break
        else:
            print("Película no encontrada")
        
    # OPCIÓN D: ELIMINAR UNA PELÍCULA.
    
    elif option == "D":
        name = input("Ingrese el título de la película a eliminar:\n")
        for film in films:
            if film[0].lower() == name.lower():
                films.remove(film)
                print("Película eliminada!\n")
                break
            else:
                print("La película que buscas no existe.\n")
    
    # OPCION S: SALIR.
    
    elif option == "S":
        print("Cerrando su sesión...")
        
    else:
        print("Opción no válida.")

else:
    # INYECCIÓN USUARIOS CLIENTES
    favorites = []  # Lista para películas favoritas del usuario cliente.
    
    option = ""
    
    # MENÚ CLIENTES
    
    while option != "S":
        print("\nMenú Cliente:\n")
        print("A. Mostrar Lista de Películas en Cartelera.\n")
        print("B. Buscar película por título.\n")
        print("C. Buscar películas por género.\n")
        print("D. Cambiar contraseña de usuario.\n")
        print("E. Crear listas de películas favoritas que se quiere ver.\n")
        print("F. Mostrar la lista de películas favoritas.\n")
        print("S. Salir.\n")
        option = input("Seleccione una de las opciones disponibles:\n ").upper()
    
        # OPCIÓN A: MOSTRAR LISTA COMPLETA DE PELÍCULAS
    
        if option == "A":
            print("\nListado de Películas en Cartelera.\n")
            for film in films:
                print(film)
    
        # OPCIÓN B: BUSCAR PELÍCULA POR TÍTULO

        elif option == "B":
            name = input("Ingrese el título de la película:\n")
            for film in films:
                if film[0].lower == name.lower():
                    print("Película encontrada!\n{film}")
                    break
                else:
                    print("La película que buscas no existe.\n")
            
        #   OPCIÓN C: BUSCAR PELÍCULA POR GÉNERO
        
        elif option == "C":
            gender = input("¿Género de la película?\n")
            print("Listado de películas por género:\n{gender}")
            for film in films:
                if film[1].lower == gender.lower():
                    print(film)
                    break
            else:
                print("El género que buscas no existe.\n")
            
        # OPCIÓN D: CAMBIAR LA CONTRASEÑA.
        
        elif option == "D":
            new_password = input("Ingrese su nueva contraseña: \n")
            for i, (u, c) in enumerate(users):
                if u == user:
                    users[i] = (u, new_password)
                    print("Contraseña Actualizada con exito!\n")
                    break
                
        # OPCIÓN E: CREAR LISTA DE PELÍCULAS FAVORITAS.
        
        elif option == "E":
            film = input("Ingrese el título de la película para añadir a su Lista de Favoritos:\n")
            favorites.append(film)
            print("Película agregada a su Lista de Favoritos correctamente!\n")
            
        # OPCIÓN F: MOSTRAR LISTA DE PELÍCULAS FAVORITAS
        
        elif option == "F":
            print("Aquí está su Lista de Películas Favoritas:\n",favorites)        
                            
        # OPCION S: SALIR.
    
        elif option == "S":
            print("Cerrando su sesión...")
        
        else:
            print("Opción no válida.")    \n""")

#                        LORETIX

# Crear un programa para gestionar la plataforma de video LORETIX.

    # A. Crear una lista de usuarios con sus contraseñas para poder acceder a la
    #    plataforma, y una para el administrador. (Lista con tuplas anidadas)

    #    a. El usuario tendrá acceso a unas opciones, mientras que el
    #       administrador a otras.

users = [
    ("client1","password1"),
    ("client2","password2"),
    ("admin","admin") # El usuario administrador tiene su propio acceso
]


    # B. Crear una lista de películas: Define una lista llamada cartelera y agrega
    #    al menos 5 películas diferentes. Por ejemplo: Nombre, genero, duración.
    
films = [
    ("The Avengers","Ciencia Ficción",2012),
    ("Expediente Warren: The Conjuring","Terror",2013),
    ("El Señor de los Anillos: La Comunidad del Anillo","Ciencia Ficción",2001),
    ("Una Proposición Indecente","Drama",1993),
    ("Moana Vahiana","Infantil",2016)
]

    # C. Menú con las diferentes opciones.

     #   Usuario:

     #       A. Buscar película por título.
     #       B. Buscar películas por género.
     #       C. Cambiar contraseña de usuario
     #       D. Crear listas de películas favoritas que se quiere ver.
     #       E. Mostrar la lista de películas favoritas.

     #   Administrador:

     #       A. Agregar una nueva película.
     #       B. Modificar el contenido de la lista de películas.
     #       C. Eliminar una película de la lista.
     
# Plantear Inicio de Sesión para diferenciar el rol de cliente y admin.

user = input("Ingrese su nombre de usuario:\n")
password = input("Ingrese su contraseña:\n")

# Comparar credenciales de usuario.

if(user, password) in users:
    if user == "admin":
        es_admin = True
    else:
        es_admin = False
else:
    print("Algo ha ocurrido...Las credenciales dadas no existen en nuestra base de datos.")
    es_admin = False
    
# Menu si es cliente o administrador

if es_admin:
    option = ""
    
    # Menú ADMIN
    while option != "S":
        
        print("\nMenú Administrador.\n")
        print("A. Mostrar Lista de Películas en Cartelera.\n")        
        print("B. Agregar una nueva película.\n")
        print("C. Modificar el contenido de la lista de películas.\n")
        print("D. Eliminar una película de la lista.\n")
        print("S. Salir.\n")
        option = input("Seleccione una de las opciones disponibles:\n ").upper()
        
        # OPCIÓN A: MOSTRAR LISTA COMPLETA DE PELÍCULAS
        if option == "A":
            print("\nListado de Películas en Cartelera.\n")
            for film in films:
                print(film)
        
        # OPCIÓN B: AGREGAR UNA PELÍCULA
        elif option == "B":
            name = input("¿Nombre de la película?\n")
            gender = input("¿Género de la película?\n")
            date = int(input("¿Fecha lanzamiento de la película?\n"))
            films.append((name, gender, date))
            print("Película agregada correctamente!\n")
        
        # OPCIÓN C: MODIFICAR UNA PELÍCULA
        elif option == "C":
            name = input("Ingrese el título de la película que va a modificar:\n")
            for i, film in enumerate(films):
                if film[0].lower() == name.lower():
                    new_name = input("Ingrese nuevo título:\n")
                    new_gender = input("Ingrese nuevo género:\n")
                    new_date = int(input("Ingrese nueva fecha de lanzamiento:\n"))
                    films[i] = (new_name, new_gender, new_date)
                    print("Película modificada correctamente!\n")
                    break
            else:
                print("Película no encontrada")
        
        # OPCIÓN D: ELIMINAR UNA PELÍCULA
        elif option == "D":
            name = input("Ingrese el título de la película a eliminar:\n")
            for film in films:
                if film[0].lower() == name.lower():
                    films.remove(film)
                    print("Película eliminada!\n")
                    break
            else:
                print("La película que buscas no existe.\n")
        
        # OPCIÓN S: SALIR
        elif option == "S":
            print("Cerrando su sesión...")
        else:
            print("Opción no válida.")

else:
    # INYECCIÓN USUARIOS CLIENTES
    favorites = []  # Lista para películas favoritas del usuario cliente.
    
    option = ""
    
    # MENÚ CLIENTES
    
    while option != "S":
        
        print("\nMenú Cliente:\n")
        print("A. Mostrar Lista de Películas en Cartelera.\n")
        print("B. Buscar película por título.\n")
        print("C. Buscar películas por género.\n")
        print("D. Cambiar contraseña de usuario.\n")
        print("E. Crear listas de películas favoritas que se quiere ver.\n")
        print("F. Mostrar la lista de películas favoritas.\n")
        print("S. Salir.\n")
        option = input("Seleccione una de las opciones disponibles:\n ").upper()
    
        # OPCIÓN A: MOSTRAR LISTA COMPLETA DE PELÍCULAS
    
        if option == "A":
            print("\nListado de Películas en Cartelera.\n")
            for film in films:
                print(film)
    
        # OPCIÓN B: BUSCAR PELÍCULA POR TÍTULO

        elif option == "B":
            name = input("Ingrese el título de la película:\n")
            for film in films:
                if film[0].lower() == name.lower():
                    print("Película encontrada!\n{film}")
                    break
                else:
                    print("La película que buscas no existe.\n")
            
        #   OPCIÓN C: BUSCAR PELÍCULA POR GÉNERO
        
        elif option == "C":
            gender = input("¿Género de la película?\n")
            print("Listado de películas por género:\n{gender}")
            for film in films:
                if film[1].lower() == gender.lower():
                    print(film)
                    break
            else:
                print("El género que buscas no existe.\n")
            
        # OPCIÓN D: CAMBIAR LA CONTRASEÑA.
        
        elif option == "D":
            new_password = input("Ingrese su nueva contraseña: \n")
            for i, (u, c) in enumerate(users):
                if u == user:
                    users[i] = (u, new_password)
                    print("Contraseña Actualizada con exito!\n")
                    break
                
        # OPCIÓN E: CREAR LISTA DE PELÍCULAS FAVORITAS.
        
        elif option == "E":
            film = input("Ingrese el título de la película para añadir a su Lista de Favoritos:\n")
            favorites.append(film)
            print("Película agregada a su Lista de Favoritos correctamente!\n")
            
        # OPCIÓN F: MOSTRAR LISTA DE PELÍCULAS FAVORITAS
        
        elif option == "F":
            print("Aquí está su Lista de Películas Favoritas:\n",favorites)        
                            
        # OPCION S: SALIR.
    
        elif option == "S":
            print("Cerrando su sesión...")
        
        else:
            print("Opción no válida.")