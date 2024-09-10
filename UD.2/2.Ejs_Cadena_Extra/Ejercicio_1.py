"""
        >>>>>>>    Ejercicios Extra de Cadenas   <<<<<<
                                                             """
print (f">>>>>>>    Ejercicios Extra de Cadenas   <<<<<<")                                                           
print (f"\n","Ejercicio 1: \n")

print ("""

Hemos comenzado a trabajar en una empresa del sector farmacéutico llamada BioNTech. Nos vamos a ocupar de ciertos análisis 
bioinformáticos. La primera ocupación que tenemos a nuestra llegada es trabajar sobre la siguiente cadena de ARN:

“AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUGGUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGG
UCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUGGTOAUGGOTGACUGG”

Cada carácter de la cadena representa un nucleótido que forma parte del ARN. Sabemos que ARN esta formado por 4 nucleótidos: 

            - Adenina (A)
            - Guanina (G)
            - Citosina (C)
            - Uracilo (U).
            
La empresa está interesada en saber cuántas tripletas de nucleótidos presentes en la cadena van a codificar en aminoácido triptófano (UGG). 
Aparte de eso ha habido ciertos errores en la secuencia y han aparecido signos extraños (T y O) que no pertenecen al ARN.

Escribe un programa que primero limpie la cadena de caracteres extraños y a
continuación cuente el numero de tripletas UGG presentes.\n\n""")


print ("""

# Cadena de ARN proporcionada
    
    arn = "AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUGGUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGG
                  UCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUGGTOAUGGOTGACUGG"

# Limpiar la cadena de caracteres extraños (T y O) de manera básica

    -> Limpiar la cadena: Usamos un bucle for para recorrer cada carácter en cadena_arn. Si el carácter es uno de los nucleótidos válidos 
       (A, G, C, U), lo agregamos a cadena_limpia usando concatenación básica.

    limpia = ""

        for caracter in arn:
            if caracter in 'AGCU':
                limpia += caracter

# Contar cuántas veces aparece la tripleta 'UGG'

    -> Contar las tripletas: El conteo de tripletas sigue siendo el mismo, recorriendo la cadena limpia y buscando la secuencia "UGG".
    
    count_ugg = 0

    for i in range(len(limpia) - 2):
        if limpia[i:i+3] == 'UGG':
            count_ugg += 1

# Mostrar resultados

    print("Cadena limpia:", limpia)
    print("Número de tripletas 'UGG':", count_ugg)\n\n""")

# Cadena de ARN proporcionada
arn = "AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUGGUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGG" \
      "UCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUGGTOAUGGOTGACUGG"

# Limpiar la cadena de caracteres extraños (T y O) de manera básica

limpia = ""
for caracter in arn:
    if caracter in 'AGCU':
        limpia += caracter

# Contar cuántas veces aparece la tripleta 'UGG'
count_ugg = 0
for i in range(len(limpia) - 2):
    if limpia[i:i+3] == 'UGG':
        count_ugg += 1

# Mostrar resultados
print("\nCadena limpia:", limpia)
print("\nNúmero de tripletas 'UGG':", count_ugg,"\n")
