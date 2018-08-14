#code Substraction
#importation de la possibilitée de nombre random
import random
#valeur de départ du jeu
startingvalue = int(0)

#Choix du mode de jeu
#print("Le mode de jeu 'first' est un mode de jeu où le but est d'arriver en premier à la valeur 0. \n Le mode de jeu 'last' est un mode de jeu où le but est de ne pas atteindre la valeur 0.")
#variable du choix du joueur de commencer en premier
firstplayer = input("Voulez vous commencer en premier ? \n ->")
#condition si le joueur répond oui
if firstplayer == 'oui':
    print("Ok")
    #compte à rebours
    for starting_counter in range(1,4):
        print(starting_counter)
    print("GO !")
    #imporation du mode de jeu lorsque le joueur décide de commencer en premier.
    import PlayerFirst
  

if firstplayer == 'non':
    print("Ok")
    #compte à rebours
    for starting_counter in range(1,4):
        print(starting_counter)
    print("GO !")
    #importation du mode de jeu lorsque le joueur décide de commencer en premier.
    import PlayerSecond