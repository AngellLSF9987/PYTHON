from cultivo import Cultivo
from datetime import date

# Objetos

cultivo1 = Cultivo("Maíz", "Dulce", date(2024, 10, 10), date(2024, 10, 15))
cultivo2 = Cultivo("Fresas", "Fresón", date(2024, 9, 9), date(2024, 10,10))

lista_cultivos = [cultivo1,cultivo2]

# Mostrar la info de los cultivos

print("Información de los cultivos:\n")
for cultivo in lista_cultivos:
    print (cultivo)


# Iniciar programa / cosechas

cultivo1.iniciar_cosecha()
cultivo2.iniciar_cosecha()

# Mostrar nuevamente la información actualizada incluyendo los días restantes

for cultivo in lista_cultivos:
    print(cultivo)

# Invocar metodo de calculo de días

for cultivo in lista_cultivos:
    cultivo.calcular_dias_restantes()