import random
from datetime import datetime

# Función para generar los números del boleto de lotería

def generar():
    """
    - random.sample() para generar 5 números sin repeticón entre 1 y 54.
    - random.choice() para elegir un número clave entre 0 y 9.
    """
    num_ganadores = random.sample(range(0,9), 5) # Genera 5 números entre 0 y 9 sin repeticón.
    num_clave = random.choice(range(10)) # Genera un número clave entre 0 y 9

    return num_ganadores, num_clave

def obtener_fecha():
    """- Utiliza el módulo datetime para obtener la fecha actual y formatearla en formato 'dd/mm/yyyy'"""
    actual = datetime.now().strftime("%d/%m/%Y") # Obtiene la fecha en formato día/mes/año
    return actual