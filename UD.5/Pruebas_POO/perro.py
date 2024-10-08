class Perro:

    contador_perros = 0  # Variable estática

    # Método __init__ (constructor de la clase)

    def __init__(self, nombre, raza, edad, pelota = False):
        """MÉTODO CONSTRUCTOR:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto"""
        #Variables de instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

        Perro.contador_perros +=1

    def __str__(self):
        """MÉTODO __str__: 
        -  Define cómo un objeto, de una clase, debe ser representado como una 
           cadena de caracteres."""
        return (f"- Nombre: {self.nombre}\n- Raza: {self.raza}\n- Edad: {self.edad} años")

    def ladrar(self):
        print(f"{self.nombre} está ladrando")
            
    def jugar(self,pelota = False):
        if pelota == True:
            return print (f"{self.nombre} está jugando con su pelota ")
        else:
            return print(f"{self.nombre} no está jugando con su pelota")

perro1 = Perro("THOR","American Sttanford", "5")
print(perro1,"\n")
print(f"Perros creados: {Perro.contador_perros}\n")
perro1.ladrar()
perro1.jugar()
# perro2 = Perro("LOCKY", "GOLDEN RETRIEVER", "8")
# print(perro2,"\n")
# print(f"Perros creados: {Perro.contador_perros}")
# perro3 = Perro("ROCKO", "PITBULL", "6")
# print(perro3,"\n")
# print(f"Perros creados: {Perro.contador_perros}")
