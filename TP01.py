#Exercice 01 :
def IMC(Poids, taille):
    Poids= int(input("Entrez votre poids en kg : "))
    taille= float(input("Entrez votre taille en m : "))
    IMC= Poids/(taille*taille)
print("Votre IMC est de : ", IMC)
