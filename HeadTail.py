import sys

def main():
    try:
        if len(sys.argv) != 4:
            print("Utilisation : py HeadTail.py [head|tail] [nombre] [fichier]")
            return

        action = sys.argv[1]
        nb_lignes_str = sys.argv[2]
        chemin_fichier = sys.argv[3]

        if action not in ["head", "tail"]:
            raise ValueError("Le paramètre doit être 'head' ou 'tail'.")

        if not nb_lignes_str.isdigit() or int(nb_lignes_str) == 0:
            raise ValueError("Le nombre de lignes doit être un entier positif.")
        
        nb_lignes = int(nb_lignes_str)

        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                lignes = fichier.readlines()
        except IOError:
            raise IOError(f"Le fichier '{chemin_fichier}' est introuvable ou illisible.")

        lignes_a_afficher = lignes[:nb_lignes] if action == "head" else lignes[-nb_lignes:]

        for ligne in lignes_a_afficher:
            print(ligne, end='')

    except ValueError as e:
        print(f"Erreur de valeur (ValueError) : {e}")
    except IOError as e:
        print(f"Erreur de fichier (IOError) : {e}")

if __name__ == "__main__":
    main()