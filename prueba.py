## A. CREAR DICCIONARIO

agenda = {
    
    "Enero": {
        
        1: "Año Nuevo", 
        31: "Cumpleaños Loreto"
    },
    
    "Febreo": {
        
        14: "San Valentin"
    },
    
    "Octubre": {
        
        15: "Examen Final Python"
    },

    "Diciembre": {
        
        24: "Noche Buena" ,
        25: "Navidad"
    }
}

## B. MOSTRAR EVENTO DEL DÍA 31 DE ENERO

evento_31 = agenda["Enero"][31]

print("Evento del 31 de Enero:", evento_31,"\n")

## C. VERIFICAR EVENTOS EN ABRIL

if "Abril" in agenda:
    print("Hay eventos en abril.\n")
else:
    print("No hay eventos en Abril.\n")
    
## D. MOSTRAR DICIEMBRE

diciembre = agenda["Diciembre"]
print("En el mes de Diciembre existen los eventos:", diciembre,"\n")
