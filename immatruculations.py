#Exercice 07:
import random
lettres = 'abcdefghjklmnpqrstvwxyz'
def bloclettre():
    lettre1 = random.choice(lettres.upper())
    lettre2 = random.choice(lettres.upper())
    bloc_lettre = lettre1 + lettre2
    if bloc_lettre == "SS":
        return bloclettre()
    return bloc_lettre
def blocchiffre():
    chiffre1 = random.randint(0, 9)
    chiffre2 = random.randint(0, 9)
    chiffre3 = random.randint(0, 9)
    bloc_chiffre = str(chiffre1) + str(chiffre2) + str(chiffre3)
    return bloc_chiffre
def matricule():
    print(f"le matricule est : {bloclettre()}-{blocchiffre()}-{bloclettre()}")
matricule()