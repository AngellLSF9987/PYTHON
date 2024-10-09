class Discoteca:

    def __init__(self, nombre, hora_apertura, hora_cierre, codigo_vestimenta = True):

        self.nombre = nombre
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.codigo_vestimenta = codigo_vestimenta

    def __str__(self):
            """MÉTODO CONSTRUCTOR:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto."""
            if self.codigo_vestimenta:
                return (f"- Nombre: {self.nombre}\n"
                        f"- Horario: De {self.hora_apertura}:00 a {self.hora_cierre}:00\n"
                        f"- Código de vestimenta: Tiene código de vestimenta")
            else:
                return (f"- Nombre: {self.nombre}\n"
                        f"- Horario: De {self.hora_apertura}:00 a {self.hora_cierre}:00\n"
                        f"- Código de vestimenta: Tiene código de vestimenta")
            
    def esta_abierta(self,hora_actual):
            """Comprueba si la discoteca está abieerta según la hora actual"""
            if self.hora_apertura <= hora_actual <= self.hora_cierre:
                return True
            return False
        
    def tiene_codigo_vestimenta(self):
            """Devuelve True si la discoteca tiene código de vestimenta, False si no."""
            return self.codigo_vestimenta
        
    def comprobar_entrada(self, nombre_persona, sandalias, bermudas, hora):
            """Comprueba si una persona puede entrar a la discoteca."""
            print(f"\nComprobando entrada de {nombre_persona} en {self.nombre} a las {hora}:00")

            if self.esta_abierta(hora) != False:
                print(f"{self.nombre} está cerrada a esa hora.")
                return False
            
            if self.tiene_codigo_vestimenta() and (sandalias or bermudas):
                print(f"{nombre_persona} no puede entrar debido al código de vestimenta.")
                return False
            
            else:
                print (f"{nombre_persona} puede entrar en {self.nombre}")

