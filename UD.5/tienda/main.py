from compras import Producto, Compra

if __name__ == "__main__":
    producto1 = Producto("Manzanas",1.5)
    producto2 = Producto("Peras", 1.2)
    producto3 = Producto("Uvas", 1.7)
    producto4 = Producto("Melocotón", 1.6)

    lista_productos = [producto1,producto2,producto3,producto4]

    compra = Compra(lista_productos)

    print(compra.totalCompra())
