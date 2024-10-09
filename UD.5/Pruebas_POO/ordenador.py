class Ordenador:

    num_ordenadores = 0

    # Método __init__ (constructor de la clase)

    def __init__(self, procesador, memoria, ram, sistemaOperativo=False):
        """MÉTODO CONSTRUCTOR:
        - Crearemos el objeto con los argumentos que pasamos a la hora de iniciar el objeto"""
        #Variables de instancia
        self.procesador = procesador
        self.memoria = memoria
        self.ram = ram
        self.sistemaOperativo = sistemaOperativo

        Ordenador.num_ordenadores +=1

    def __str__(self):
        """MÉTODO __str__: 
        -  Define cómo un objeto, de una clase, debe ser representado como una 
           cadena de caracteres."""
        if self.sistemaOperativo:
            return (f"- Procesador: {self.procesador}\n- Memoria Interna: {self.memoria}\n- Memoria RAM: {self.ram}\n- Sistema Operativo: Tiene S.O.")
        
        else:
            return (f"- Procesador: {self.procesador}\n- Memoria Interna: {self.memoria}\n- Memoria RAM: {self.ram}\n- Sistema Operativo: No tiene S.O.")

    def instalarSO(self):
        if self.sistemaOperativo == False:
            print("El ordenador no tiene Sistema Operativo instalado.\n")
            SO = input("¿Qué sistema operativo quiere instalar?")
            self.sistemaOperativo = True
            print(f"El ordenador ya ha instalado el {SO}.")
        else:
            print("Ya tiene Sistema Operativo instalado.")


         
pc1 = Ordenador("AMD Ryzen 5","500GB", "16GB")
pc1.instalarSO() 
print(pc1,"\n")

print(f"Ordenadores creados: {Ordenador.num_ordenadores}\n")
pc2 = Ordenador("Intel i7", "1TB", "8GB",True)
print(pc2,"\n")
print(f"Ordenadores creados: {Ordenador.num_ordenadores}")


lista_ordenadores = [pc1, pc2]

for pc in lista_ordenadores:
    print(pc)