from datetime import datetime

class Cultivo:

    def __init__ (self, nombre, variedad, fecha_siembra, fecha_cosecha):
        self.nombre = nombre
        self.variedad = variedad
        self.fecha_siembra = fecha_siembra
        self.fecha_cosecha = fecha_cosecha
        self.estado_cosecha = "No iniciado"

    def __str__(self):
        """MÉTODO CONSTRUCTOR:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto.
        - Define las fechas en formato de España.
        
            strftime("%d/%m/%Y"): Convierte las fechas fecha_siembra y fecha_cosecha_esperada en cadenas de texto con el formato dd/mm/YYYY, que es el estilo español.
                    %d: Día con dos dígitos.
                    %m: Mes con dos dígitos.
                    %Y: Año con cuatro dígitos."""

        fecha_siembra_formateada = self.fecha_siembra.strftime("%d/%m/%Y")
        fecha_cosecha_formateada = self.fecha_cosecha.strftime("%d/%m/%Y")

        return (f"- Nombre: {self.nombre}\n"
                f"- Nombre: {self.variedad}\n"
                f"- Nombre: {fecha_siembra_formateada}\n"
                f"- Nombre: {fecha_cosecha_formateada}\n"
                f"- Nombre: {self.estado_cosecha}\n")
    
    def iniciar_cosecha(self):
        """Método para iniciar la cosecha:
        - Cambia el estado por defecto de NO INICIADO al estado EN CURSO"""
        self.estado_cosecha = "En curso"
        print(f"La cosecha de {self.nombre} de la variedad ({self.variedad}) está curso.\n")

    def finalizar_cosecha(self):
        """Método para finalizar la cosecha:
        - Cambia el estado EN CURSO al estado FINALIZADO"""
        self.estado_cosecha = "Finalizado"
        print(f"La cosecha de {self.nombre} de la variedad ({self.variedad}) ha finalizado.")

    def calcular_dias_restantes(self):
        """Método para calcular los días restantes hasta la fecha esperada de la cosecha"""
        hoy = datetime.today().date()
        dias_restantes = (self.fecha_cosecha - hoy).days

        if dias_restantes > 0:
            print(f"Quedan {dias_restantes} para la cosecha de {self.nombre}.\n")
        elif dias_restantes == 0:
            print(f"Hoy es día de cosecha de {self.nombre}.\n")
        else:
            print(f"La fecha de cosecha de {self.nombre} han pasado {abs(dias_restantes)} días.")


                    



