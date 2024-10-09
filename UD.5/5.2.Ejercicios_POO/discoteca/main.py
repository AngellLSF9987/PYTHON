from discoteca import Discoteca

discoteca1 = Discoteca("Night Party", 18, 4, True)
discoteca2 = Discoteca("Pool Party", 12, 22, False)

hora_tom = 16

lleva_sandalias = True
lleva_bermudas = True

# Comprobar si Tom puede entrar  en la primera Fiesta

discoteca1.comprobar_entrada("Tom el guiri", lleva_sandalias, lleva_bermudas, hora_tom)
print()
discoteca2.comprobar_entrada("Tom el guiri", lleva_sandalias,lleva_bermudas,hora_tom)
print()
print(discoteca1)
print()
print(discoteca2)
print()