def media(*valores):
    suma = 0
    for num in valores:
        suma += num
        print (f"La media aritmética de los números introducidos es: {suma/len(valores)}")

# media(3,6,2,6,1,6,3,3,3)
print()
media(1,2,3)       