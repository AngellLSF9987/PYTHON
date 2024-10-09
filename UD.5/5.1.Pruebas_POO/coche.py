class Motor:
    def __init__(self,potencia, cilindrada):
        """MÉTODO CONSTRUCTOR __init__:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto"""
        self.potencia = potencia
        self.cilindrada = cilindrada

    def __str__(self):
        """MÉTODO __str__: 
        -  Define cómo un objeto, de una clase, debe ser representado como una 
           cadena de caracteres."""
        return (f"- Potencia: {self.potencia} cv \n- Cilindrada: {self.cilindrada} cc\n")

class Coche:

    encendido = False # Variable estática

    num_coches = 0
    # Método __init__ (constructor de la clase)

    def __init__(self, marca, modelo, color, motor, puertas=5):
        """MÉTODO CONSTRUCTOR __init__:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto"""
        #Variables de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.velocidad = 0
        Coche.num_coches +=1

    def __str__(self):
        """MÉTODO __str__: 
        -  Define cómo un objeto, de una clase, debe ser representado como una 
           cadena de caracteres."""
        return (f"- Marca de coche: {self.marca}\n- Modelo de coche: {self.modelo}\n- Color del coche: {self.color}\n- Motor del coche:\n-- Potencia: {self.motor.potencia}\n-- Cilindrada: {self.motor.cilindrada} \n- Nº de puertas: {self.puertas}")

    def arrancar(self):
        """MÉTODO DE INSTANCIA"""
        print("- El coche está arrancado")

    def acelerar(self):
        self.velocidad += 10
        print("- El coche acelera")

    def frenar(self):
        self.velocidad -= 5
        print("- El coche frena")
    
motor1= Motor(130, 1500)
motor2 = Motor(175, 1900)

coche1 = Coche("Audi","Q3", "Gris", motor1)
print(coche1,"\n")
print(f"Coches creados: {Coche.num_coches}\n")

coche1.arrancar()
print(f"  -> Velocidad Inicial: {coche1.velocidad}")

coche1.acelerar()
print(f"  -> Velocidad Actual: {coche1.velocidad}")

coche1.frenar()
print(f"  -> Velocidad Actual después de Frenado: {coche1.velocidad}\n\n")

coche2 = Coche("AUdi", "Q5", "Blanco",motor2)
print(coche2,"\n")
print(f"Coches creados: {Coche.num_coches}")
