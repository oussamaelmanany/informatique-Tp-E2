Exercice cesar :
def decalage_cesar(cle, phrase):
      cle = cle.upper(       phrase = phrase.upper     
    phrase_encodee     
  ur_cle = lei    e i
    for i in range(len(p    hras
        lettre_phrase = phra]    es ees)
        if 'A' <= lettre_ph     au modu)
            lettre_cle e     2, ...,> 26
            decalage = ord(lettre_c)     décalagdulo 26
            position_initiale = ord(lettr    e_phraseord('A')
            nouvelle_position = (position_inia    SCII (enjoutant 65)
            lettre_finale = chr(nouve    lle_posi + ord('A'))
            phrase    _enc += le     ne s'agas d'une lettre
            phrase_enco+    ttre_phrase
          t avec l'exemple de l'énoncé ---
resultat = decalage_cesa
import random
def random_election(noms):
    ele = []
    i  = 0
    while len(ele) < 4:
        candidat = random.choice(noms)
        if candidat not in ele:
            ele = ele.append(candidat)
    resultat = {
    delegues = [ele[0],ele[1]]
    suppleants = [ele[2], ele[3]]
    }
    return delegues,suppleants
            
        resultat)  # Affiche bien : CQOLPWS