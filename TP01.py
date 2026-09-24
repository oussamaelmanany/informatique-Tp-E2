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
def decimal_to_binaire():
    q = int(input("entrer un nombre décimal : "))
    binaire = ""
    if q ==0 :
        print("0")
    else:
        while q!=0:
            r = q%2
            binaire = str(r) + binaire
            q = q//2
    print("Le nombre binaire est : ", binaire)

#Exercice 04:
def approphi():
    phi_appro = 3.00
    phiutili = input("Entrez la valeur de phi : ")
    N= int(phiutili)
    if N < 0:
        print("Erreur : la valeur de phi doit être positive.")
    else:
        if N <= 0:
            print(f"La valeur approchée de phi est :{phi_appro}")
            for i in range(2, N + 1):
                k = i - 1 
                d = 2 * k 
                terme = signe * (4 / (d * (d + 1) * (d + 2)))
                pi_approx += terme
                print(f"Approximation {i} : {pi_approx}")


