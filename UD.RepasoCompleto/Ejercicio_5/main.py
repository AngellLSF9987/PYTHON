from packages.menu import mostrar_menu
from packages.functions import seleccionar_paises, adivinar_capitales

def main():
    
    opcion, num_users = mostrar_menu()

    paises_capitales = seleccionar_paises(opcion)

    adivinar_capitales(paises_capitales, num_users)

if __name__ == "__main__":
    main()