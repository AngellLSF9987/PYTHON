"""
        >>>>>>>     Ejercicio LORETIX - FUNCIONES   <<<<<<
                                                                    """

print (f">>>>>>>    Ejercicio LORETIX - FUNCIONES   <<<<<<")                                                            
print (f"\n","Ejercicio Extra: \n")
print ("""
#                        LORETIX

# Crear un programa para gestionar la plataforma de video LORETIX.

    # A. Crear una lista de usuarios con sus contraseñas para poder acceder a la
    #    plataforma, y una para el administrador. (Lista con tuplas anidadas)

    #    a. El usuario tendrá acceso a unas opciones, mientras que el
    #       administrador a otras.


    # B. Crear una lista de películas: Define una lista llamada cartelera y agrega
    #    al menos 5 películas diferentes. Por ejemplo: Nombre, genero, duración.
    

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


                    ###### FUNCTIONS CRUD REGION ########

#Función para verificar las credenciales

def verificar_credenciales(user, password, users):
    if(user, password) in users:
        return True if user == "admin" else False
    else:
        print("ALgo ha ocurrido... El usuario o contraseña ingresados no son válidos.")
    
# Función para mostrar la lista películas.

def mostrar(films):
    print("\nListado de Películas en Cartelera.\n")
    
    for film in films:
        print(film)

# Función para agregar una nueva película.

def agregar(films):
        name = input("¿Nombre de la película?\n")
        gender = input("¿Género de la película?\n")
        date = int(input("¿Fecha lanzamiento de la película?\n"))
        films.append((name, gender, date))
        print("Película agregada correctamente!\n")
    

# Función para modificar una película

def modificar(films):
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

# Función para eliminar una película.

def eliminar(films):
    name = input("Ingrese el título de la película a eliminar:\n")
    for film in films:
        if film[0].lower() == name.lower():
            films.remove(film)
            print("Película eliminada!\n")
            break
    else:
     print("La película que buscas no existe.\n")
    

            ##########  ADMIN REGION  ##########

    # Menú ADMIN

def menu_admin(films):
    option = ""
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
            mostrar(films)
        
        # OPCIÓN B: AGREGAR UNA PELÍCULA
        elif option == "B":
            agregar(films)
        
        # OPCIÓN C: MODIFICAR UNA PELÍCULA
        elif option == "C":
            modificar(films)
        
        # OPCIÓN D: ELIMINAR UNA PELÍCULA
        elif option == "D":
            eliminar(films)
        
        # OPCIÓN S: SALIR
        elif option == "S":
            print("Cerrando su sesión...")
        else:
            print("Opción no válida.")


        ##########  CLIENT REGION  ##########

# Función cambio de contraseña

def cambiar_contraseña(users, user):

    new_password = input("Ingrese su nueva contraseña: \n")
    
    for i, (u, _) in enumerate(users):
        if u == user:
            users[i] = (u, new_password)
            print("Contraseña Actualizada con exito!\n")
            break

def buscar_titulo(films):
    
    name = input("Ingrese el título de la película:\n")
    
    for film in films:
        if film[0].lower() == name.lower():
            print("Película encontrada!\n{film}")
            break
        else:
            print("La película que buscas no existe.\n")

def buscar_genero(films):
      
    gender = input("¿Género de la película?\n")
    
    print("Listado de películas por género:\n{gender}")
    for film in films:
        if film[1].lower() == gender.lower():
            print(film)
            break
    else:
        print("El género que buscas no existe.\n")

def agregar_favoritos(favorites):
    
    film = input("Ingrese el título de la película para añadir a su Lista de Favoritos:\n")
    favorites.append(film)
    print("Película agregada a su Lista de Favoritos correctamente!\n")
    
def mostrar_favoritos(favorites):
     print("Aquí está su Lista de Películas Favoritas:\n",favorites)

# MENÚ CLIENTES

def menu_cliente(films, users, user, favorites):
    option= ""
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
            mostrar(films)
    
        # OPCIÓN B: BUSCAR PELÍCULA POR TÍTULO

        elif option == "B":
            buscar_titulo(films)
            
        #   OPCIÓN C: BUSCAR PELÍCULA POR GÉNERO
        
        elif option == "C":
            buscar_genero(films)
            
        # OPCIÓN D: CAMBIAR LA CONTRASEÑA.
        
        elif option == "D":
            cambiar_contraseña(users, user)
                
        # OPCIÓN E: CREAR LISTA DE PELÍCULAS FAVORITAS.
        
        elif option == "E":
            agregar_favoritos(favorites)
            
        # OPCIÓN F: MOSTRAR LISTA DE PELÍCULAS FAVORITAS
        
        elif option == "F":
              mostrar_favoritos(favorites)     
                            
        # OPCION S: SALIR.
    
        elif option == "S":
            print("Cerrando su sesión...")
        
        else:
            print("Opción no válida.")
            
            
########  PROGRAM REGION  #######

# Función principal datos del programa

def main ():
    users = [
        ("client1","password1"),
        ("client2","password2"),
        ("admin","admin") # El usuario administrador tiene su propio acceso
    ]
    
    films = [
        ("The Avengers","Ciencia Ficción",2012),
        ("Expediente Warren: The Conjuring","Terror",2013),
        ("El Señor de los Anillos: La Comunidad del Anillo","Ciencia Ficción",2001),
        ("Una Proposición Indecente","Drama",1993),
        ("Moana Vahiana","Infantil",2016)
    ]
    
    favorites = []  # Lista para películas favoritas del usuario cliente.
    
    user = input("Ingrese su nombre de usuario:\n")
    password = input("Ingrese su contraseña:\n")
    
    es_admin = verificar_credenciales(user, password, users)
    
# Condicional si es cliente o administrador

    if es_admin is None:
        return
           
    if es_admin:
        menu_admin(films)
        
    else:
        menu_cliente(films, users, user, favorites)

# Iniciar el programa       
main()

\n""")

#                        LORETIX

# Crear un programa para gestionar la plataforma de video LORETIX.

    # A. Crear una lista de usuarios con sus contraseñas para poder acceder a la
    #    plataforma, y una para el administrador. (Lista con tuplas anidadas)

    #    a. El usuario tendrá acceso a unas opciones, mientras que el
    #       administrador a otras.

    # B. Crear una lista de películas: Define una lista llamada cartelera y agrega
    #    al menos 5 películas diferentes. Por ejemplo: Nombre, genero, duración.

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


                    ###### FUNCTIONS CRUD REGION ########

#Función para verificar las credenciales

def verificar_credenciales(user, password, users):
    if(user, password) in users:
        return True if user == "admin" else False
    else:
        print("ALgo ha ocurrido... El usuario o contraseña ingresados no son válidos.")
    
# Función para mostrar la lista películas.

def mostrar(films):
    print("\nListado de Películas en Cartelera.\n")
    
    for film in films:
        print(film)

# Función para agregar una nueva película.

def agregar(films):
        name = input("¿Nombre de la película?\n")
        gender = input("¿Género de la película?\n")
        date = int(input("¿Fecha lanzamiento de la película?\n"))
        films.append((name, gender, date))
        print("Película agregada correctamente!\n")
    

# Función para modificar una película

def modificar(films):
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

# Función para eliminar una película.

def eliminar(films):
    name = input("Ingrese el título de la película a eliminar:\n")
    for film in films:
        if film[0].lower() == name.lower():
            films.remove(film)
            print("Película eliminada!\n")
            break
    else:
     print("La película que buscas no existe.\n")
    

            ##########  ADMIN REGION  ##########

    # Menú ADMIN

def menu_admin(films):
    option = ""
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
            mostrar(films)
        
        # OPCIÓN B: AGREGAR UNA PELÍCULA
        elif option == "B":
            agregar(films)
        
        # OPCIÓN C: MODIFICAR UNA PELÍCULA
        elif option == "C":
            modificar(films)
        
        # OPCIÓN D: ELIMINAR UNA PELÍCULA
        elif option == "D":
            eliminar(films)
        
        # OPCIÓN S: SALIR
        elif option == "S":
            print("Cerrando su sesión...")
        else:
            print("Opción no válida.")


        ##########  CLIENT REGION  ##########

# Función cambio de contraseña

def cambiar_contraseña(users, user):

    new_password = input("Ingrese su nueva contraseña: \n")
    
    for i, (u, _) in enumerate(users):
        if u == user:
            users[i] = (u, new_password)
            print("Contraseña Actualizada con exito!\n")
            break

def buscar_titulo(films):
    
    name = input("Ingrese el título de la película:\n")
    
    for film in films:
        if film[0].lower() == name.lower():
            print("Película encontrada!\n{film}")
            break
        else:
            print("La película que buscas no existe.\n")

def buscar_genero(films):
      
    gender = input("¿Género de la película?\n")
    
    print("Listado de películas por género:\n{gender}")
    for film in films:
        if film[1].lower() == gender.lower():
            print(film)
            break
    else:
        print("El género que buscas no existe.\n")

def agregar_favoritos(favorites):
    
    film = input("Ingrese el título de la película para añadir a su Lista de Favoritos:\n")
    favorites.append(film)
    print("Película agregada a su Lista de Favoritos correctamente!\n")
    
def mostrar_favoritos(favorites):
     print("Aquí está su Lista de Películas Favoritas:\n",favorites)

# MENÚ CLIENTES

def menu_cliente(films, users, user, favorites):
    option= ""
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
            mostrar(films)
    
        # OPCIÓN B: BUSCAR PELÍCULA POR TÍTULO

        elif option == "B":
            buscar_titulo(films)
            
        #   OPCIÓN C: BUSCAR PELÍCULA POR GÉNERO
        
        elif option == "C":
            buscar_genero(films)
            
        # OPCIÓN D: CAMBIAR LA CONTRASEÑA.
        
        elif option == "D":
            cambiar_contraseña(users, user)
                
        # OPCIÓN E: CREAR LISTA DE PELÍCULAS FAVORITAS.
        
        elif option == "E":
            agregar_favoritos(favorites)
            
        # OPCIÓN F: MOSTRAR LISTA DE PELÍCULAS FAVORITAS
        
        elif option == "F":
              mostrar_favoritos(favorites)     
                            
        # OPCION S: SALIR.
    
        elif option == "S":
            print("Cerrando su sesión...")
        
        else:
            print("Opción no válida.")
            
            
########  PROGRAM REGION  #######

# Función principal datos del programa

def main ():
    users = [
        ("client1","password1"),
        ("client2","password2"),
        ("admin","admin") # El usuario administrador tiene su propio acceso
    ]
    
    films = [
        ("The Avengers","Ciencia Ficción",2012),
        ("Expediente Warren: The Conjuring","Terror",2013),
        ("El Señor de los Anillos: La Comunidad del Anillo","Ciencia Ficción",2001),
        ("Una Proposición Indecente","Drama",1993),
        ("Moana Vahiana","Infantil",2016)
    ]
    
    favorites = []  # Lista para películas favoritas del usuario cliente.
    
    user = input("Ingrese su nombre de usuario:\n")
    password = input("Ingrese su contraseña:\n")
    
    es_admin = verificar_credenciales(user, password, users)
    
# Condicional si es cliente o administrador

    if es_admin is None:
        return
           
    if es_admin:
        menu_admin(films)
        
    else:
        menu_cliente(films, users, user, favorites)

# Iniciar el programa       
main()