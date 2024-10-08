
fiestas = {
    "Enero":{1:"Año Nuevo", 6:"Reyes",31:"Cumpleaños Loreto"},
    "Febrero": {14: "San Valentin"},
    "Marzo": {19: "San José"},
    "Abril":{17: "Jueves Santo",18:"Viernes Santo"},
    "Mayo":{4:"Día de la madre"},
    "Junio":{9: "Día de la Región de Murcia"},
    "Julio":{6:"San Fermín"},
    "Agosto":{15:"Asunción de la Virgen"},
    "Septiembre":{16:"Romeria de la Fuensanta"},
    "Octubre":{12:"El día del Pilar"},
    "Noviembre":{1: "Día de todos los santos"},
    "Diciembre":{6:"Día de la Constitución",8:"Día de la Inmaculada Concepción",24:"NocheBuena",25:"Navidad"}
}

def obtener_fiestas_primer():
    """Obtiene fiestas del primes trimestre"""

    primer_trimestre = []
    for mes in ["Enero","Febrero","Marzo"]:
        for dia, fiesta in fiestas[mes].items():
            primer_trimestre.append(f"{dia} de {mes}: {fiesta}")

        return primer_trimestre
    
def obtener_fiestas_diciembre():
    """Obtiene las fiestas de Diciembre."""

    fiestas_diciembre = []

    for dia, fiesta in fiestas["Diciembre"].items():
        fiestas_diciembre.append(f"{dia} de Diciembre: {fiesta}")
    
    return fiestas_diciembre
