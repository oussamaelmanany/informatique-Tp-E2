#Exercice 06 :
def calcul():
    opperation = input("type d'operation souhaité : (a)ddition, (s)oustraction, (m)ultiplication, (d)ivision : ")
    opperation = opperation.lower()
    nombre_1= int(input("Entrez un nombre 1  : "))
    nombre_2 = int(input("Entrez un nombre 2  : "))
    if opperation == "a":
        resultat = nombre_1 + nombre_2
    if opperation == "s":
        resultat = nombre_1 - nombre_2
    if opperation == "m":
        resultat = nombre_1 * nombre_2
    if opperation == "d":
        if nombre_2 == 0:
            resultat = print("division impossible")
        else: 
            resultat = nombre_1 / nombre_2
    else:
        print("operation non compris")
    print("Le resultat est : ", resultat)
    recalculer = input("voulez vous recalculer ? (o/n) : ")
    recalculer = recalculer.lower()
    if recalculer == "o":
        calcul()
    if recalculer == "n":
        print("fin du programme")
    else:
        print("reponse non compris")
calcul()
