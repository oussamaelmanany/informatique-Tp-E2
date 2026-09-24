#Exercice 01:
def factorielle():
    nombre = int(input("entrer un nombre entier :"))
    for i in range(1,nombre):
        nombre = i*nombre
    print(nombre)
#factorielle()

#Exercice 02:
def suite_syracuse():
    ent_natu = int(input("entrer un entier naturel"))
    if ent_natu == 1 :
        return
    if ent_natu % 2 == 0:
        return  ent_natu / 2
    if ent_natu % 2 != 0:
        return (ent_natu * 3) + 1
print(suite_syracuse())

#Exercice 03:


