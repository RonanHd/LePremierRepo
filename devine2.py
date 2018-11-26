#Faire un jeu qui demande à l'utilisateur de deviner un chiffre
#généré aléatoirement entre 1 et 10 et qui précise si le chiffre
#rentré est plus grand ou plus petit que le chiffre généré.
#Exemple : le programme a généré le chiffre 8 aléatoirement
#"Entrer un chiffre" =>5 "Le chiffre mystère est plus élevé"=>9 "
#Le chiffre mystère est plus petit"=>8 "Vous avez trouvé le bon chiffre !"

import random
ADeviner = random.randint(1, 10)
print(ADeviner)
nombreUtilisateur = "Ronan est trop beau, si si croyez moi!"

tst = ('0','1','2','3','4','5','6','7','8','9','10')


while nombreUtilisateur != str(ADeviner) :
    nombreUtilisateur = input("Quel nombre entre 1 et 10?")
    if nombreUtilisateur not in tst :
        print("WOOH!!! Un nombre entre 1 et 10!")
        
    elif nombreUtilisateur in tst :
        if int(nombreUtilisateur) < ADeviner :
            print ("trop petit")
        elif int(nombreUtilisateur) > ADeviner :
            print ("trop grand")
        
print ("OK tu as trouvé")
