Ejercicios de repaso.

    Ejercicio 1.
    
        A. Crear un programa que imprima los 10 primeros números naturales utilizando tanto un
           bucle while como el bucle for.

        B. Modificar el programa anterior para que muestre 10 números aleatorios entre 1 y 50
           (modulo random) realizar la modificación tanto para el bucle while, como el bucle for.

        C. Crear 2 listas, una para números pares y otra impares. Rellenar esas listas con los
           números aleatorios del apartado B.

        D. Con las listas impares, crear una lista y añadir los números que sean múltiplos de 3.

        E. Con las listas pares, crear otra lista con los números menores a 25.

        F. Imprimir por pantalla ambas listas.

    Ejercicio 2.

        A. Crea una función que muestra una tabla de multiplicar.

        B. Modifica ese programa para que imprima las tablas de multiplicar del 1 al 10.
           Se puede hacer con funciones.

    Ejercicio 3.

    La profesora de informática quiere crear un programa para organizar la clase:

    Partiendo de la lista de nombres de los alumnos de la clase, los situe en la disposición de las
    mesas de la clase que tiene forma de matriz 3x4 de manera aleatoria. (3 filas, 4 columnas)

    Por ejemplos: La lista tiene 12 nombres, sale un nombre aleatorio de la lista, y en la primera
                  posición de la matriz, la posición (0,0) se situe ese nombre.

    Nota: Una forma común de construir matrices es haciendo uso de listas anidadas (o listas de
          listas). Si una lista convencional forma un vector de elementos, al hacer que cada elemento sea
          un vector, se obtiene una matriz de elementos.

    Para crear una matriz vacía se puede utilizar listas de comprensión:

        matriz_alumnos = [[0 for _ in range(4)] for _ in range(3)]

    También se puede crear las matriz vacías de manera manual.

            matriz_alumnos = []
            
            for _ in range(3):
                fila = []
 
            for _ in range(4):
                fila.append(None)
                
            matriz_alumnos.append(fila)

    (Se utiliza _ a la otra de crear la lista, porque el contenido no se va a utilizar, es para sustituirlo,
    sería una variable desechable)

    Ejercicio 4.

        A partir del siguiente diccionario:

        fiestas = {"enero":{1:"Año Nuevo", 6:"Reyes",31:"Cumpleaños Loreto"},
                    "febrero": {14: "San Valentin"},
                    "marzo": {19: "San José"},
                    "abril":{17: "Jueves Santo",18:"Viernes Santo"},
                    "mayo":{4:"Día de la madre"},
                    "junio":{9: "Día de la Región de Murcia"},
                    "julio":{6:"San Fermín"},
                    "agosto":{15:"Asunción de la Virgen"},
                    "septiembre":{16:"Romeria de la Fuensanta"},
                    "octubre":{12:"El día del Pilar"},
                    "noviembre":{1: "Día de todos los santos"},
                    "diciembre":{6:"Día de la Constitución",8:"Día de la Inmaculada
                    Concepción",24:"NocheBuena",25:"Navidad"}}

        A. Sacar las fiestas del primer trimestre, almacenarlas en una lista y mostrarlas.
        
        B. Imprime las fiestas de diciembre

    Ejercicio 5.

    Crear un juego educativo donde el usuario debe adivinar las capitales de los países europeos.

    Los países en cada partida deben salir en orden diferente.

    A partir de este diccionario:

        paises_capitales = {“España": "Madrid", "Francia": "París", "Alemania": "Berlín", "Italia": "Roma",
                "Reino Unido": "Londres", "Portugal": "Lisboa", "Grecia": "Atenas", "Suecia": "Estocolmo",
                "Noruega": "Oslo", "Finlandia": "Helsinki", "Bélgica": "Bruselas", "Países Bajos": "Amsterdam",
                "Suiza": "Berna", "Austria": "Viena", "Dinamarca": "Copenhague", "Irlanda": "Dublín”}


    Extra: Se pueden añadir más países, o hacerlo por continentes.