#Exercice 01 :
def IMC():
    Poids= int(input("Entrez votre poids en kg : "))
    taille= float(input("Entrez votre taille en m : "))
    IMC= Poids/(taille*taille)
    print("Votre IMC est de : ", IMC)

#Exercice 02 :
def maxminmoy():
    N = 0
    Nombres = []
    while N >= 0 :
        N=int(input("Entrez un nombre  : "))
        Nombres.append(N)
    max = max(Nombres)
    min = min(Nombres)
    mous = sum(Nombres)/len(Nombres)
    print("Le maximum est : ", max)
    print("Le minimum est : ", min)
    print("La moyenne est : ", mous)

#Exercice 03 :
def agecanineshumain():
    age = int(input("Entrez l'âge du chien en années : "))
    if age <= 2:
        age_humain = age * 10.5
    else:
        age_humain = 21 + (age - 2) * 7
    print("L'âge du chien en années humaines est : ", age_humain)
#Exercice 05:
def decimal_to_binary():
    n = int(input("Entrez un nombre décimal :"))
    if n = 0:
        return "0"
    elif n>0 : 
        return bin(n)
    else:
        return "-" + bin(abs(n))
#Exercice 06:
def decimal_to_binaire():
    q = int(input("entrer un nombre décimal:"))
    resultat = []
    r = q % 2
    resultat.append(str(r))
    






