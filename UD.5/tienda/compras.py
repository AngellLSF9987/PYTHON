class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    def __str__(self):
        return (f"El nombre del producto es {self.nombre} y su precio es {self.precio}")

class Compra:

    def __init__(self, productos):
        self.productos = productos
    
    def totalCompra(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

