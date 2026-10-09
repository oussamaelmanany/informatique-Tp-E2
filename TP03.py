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

#Exercice 04:
import random
def jouer_pendu():
    try:
        with open("dic.txt", "r", encoding="utf-8") as fichier:
            mots = fichier.readlines()
            if not mots:
                print("Le dictionnaire est vide.")
                return
            mot_secret = random.choice(mots).upper()
    except FileNotFoundError:
        print("Erreur : Le fichier dic.txt est introuvable.")
        return
vies = 6
lettres_testees = set()
lettres_trouvees = {mot_secret[0]}
print("Début de la partie")
while vies > 0:
    affichage = [lettre if lettre in lettres_trouvees else "_" for lettre in mot_secret]
    print(f"\nMot à trouver : {' '.join(affichage)}")
        
    if "_" not in affichage:
        print("\nFélicitations, tu as trouvé toutes les lettres, tu as gagné !")
        return
    print(f"Vies restantes : {vies}")
    lettre_propose = input("saisir un lettre").strip().upper()
    if len(lettre_propose) !=1 or not lettre_propose.isalpha():
        print("merci de saisir un lettre valide")
        continue

    try:
        if lettre_proposee in lettres_testees:
            raise LettreDejaSoumiseError(f"La lettre '{lettre_proposee}' a déjà été essayée.")
            
        lettres_testees.add(lettre_proposee)

        if lettre_proposee in mot_secret:
            print("Bien joué !")
            lettres_trouvees.add(lettre_proposee)
        else:
            print("Raté !")
            vies -= 1

    except LettreDejaSoumiseError as erreur:
        print(f"Erreur : {erreur}")
    print(f"\nTu n'as plus de vies, tu as perdu ! Le mot était : {mot_secret}")
jouer_pendu()

#Exercice 05 :
def hanoi(n,source, cible, auxiliaire, fichier):
    if n > 0:
        hanoi(n - 1, source, auxiliaire, cible, fichier)
        mouvement = f"Déplacer le disque de la tige {source} vers la tige {cible}\n"
        fichier.write(mouvement)
        hanoi(n - 1, auxiliaire, cible, source, fichier)

def lancer_simulation_hanoi(nombre_disques):
    with open("hanoi.txt", "w", encoding="utf-8") as fichier:
        hanoi(nombre_disques, "A", "C", "B", fichier)
    
    print(f"Simulation terminée pour {nombre_disques} disques.")
    print("Les mouvements ont été enregistrés dans le fichier hanoi.txt.")
lancer_simulation_hanoi(3)