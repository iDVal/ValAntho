#Ce code concerne la page d'accueil, il permettra d'identifier l'utilisateur ainsi que choisir le jeux : Substration ou Aleatory.
print("---BIENVENUE---\n")

#Choix du pseudo de l'utilisateur
username = input("Veuillez indiquer votre pseudonyme : \n ->")

#Demande d'informations sur un jeu de la part de l'utilisateur, ou non.
print("\n Bonjour " + username + " vous voici à présent dans le menu de séléction de jeux.\n Indiquez le jeu sur lequel vous voulez avoir des informations : Substraction ou Aleatory ?")
answer1 = input("Si vous ne voulez pas d'informations, tapez non \n ->")

for answer1 in('Substraction', 'Aleatory', 'non'):
        if answer1 == 'Substraction':
                 print("Le jeu substraction est un jeu dont l'objectif est d'atteindre 0 avant l'ordinateur, et cela par soustraction de valeur comprise entre 1 et 3, en partant de 50. ")
                 break
        if answer1 == 'Aleatory':
                 print("Désolé, nous manquons d'informations sur ce jeu pour le moment, réessayez plus tard.")
                 break
        if answer1 == 'non':
                  print("Compris, passons à la sélection du jeu auquel vous voulez jouer.")
                  break
 
        


#Choix du jeu de la part de l'utilisateur
gamechoice = input("Voulez vous jouer à Substraction ou Aleatory ? \n ->")

if gamechoice =='Substraction':
        import Substraction
if gamechoice == 'Aleatory':
        print("Nous sommes désolé, ce jeu n'est pas disponible pour le moment, réessayez plus tard.")
    
