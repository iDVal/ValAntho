#Création du tableau rôles
tableau_roles = ["Citoyen:0:3", "Necromancien:1:1", "Voyante:1:1", "Chef Zombie:1:1", "Assassin:1:1", "Lambda:1:1", "Cupidon:1:1", "Zombie:1:1"]

""" 
Citoyen : vote compte double
Necromancien : Possibilite de tuer et/ou de ramener a la vie UNE personne (ainsi qu'interroger un mort)
Voyante : peut savoir à chaque nuit UN role d'un joueur
Chef Zombie : tue UN joueur ennemie chaque nuit avec l'accord de son coéquipier + LA premiere victime devient le zombie contaminé
Assassin : lors de sa mort il choisit de tuer UNE personne avec lui
Lambda : non défini
Cupidon : lie 2 joueurs dans l'amour et la mort => les 2 amoureux devront etre les SEULS survivants
Zombie : tue UN joueur chaque nuit avec l'accord de son coéquipier

0 = plusieurs
1 = unique
"""
saisie_int_ok=0
nb_players=0
while saisie_int_ok != 1 or nb_players<1 or nb_players>10:   # keep looping until we break out of the loop
    'cls'
    import os
    clear = lambda: os.system('cls')
    clear()

    print("Bienvenue dans Zombie, il s'agit d'un jeu de rôle dans lequel s'affronte d'un côté les zombies et de l'autre les villageois!")
    print("\n Voici les différents rôles : \n ")
    print("Citoyen : vote compte double \n Necromancien : Possibilite de tuer et/ou de ramener a la vie UNE personne (ainsi qu'interroger un mort) \n Voyante : peut savoir à chaque nuit UN role d'un joueur \n Chef Zombie : tue UN joueur ennemie chaque nuit avec l'accord de son coéquipier + LA premiere victime devient le zombie contaminé \n Assassin : lors de sa mort il choisit de tuer UNE personne avec lui \n Cupidon : lie 2 joueurs dans l'amour et la mort => les 2 amoureux devront etre les SEULS survivants \n Zombie : tue UN joueur chaque nuit avec l'accord de son coéquipier \n Lambda : non défini")
    try:
        nb_players = int(input("Indiquez le nombre de joueurs non bot : \n ->"))
        saisie_int_ok=1
    except ValueError:
        print("erreur")


#Création dynamique du tableau joueurs
nb_bot = int(10 - nb_players)
tableau_players = []
cpt_player=1
while cpt_player != (nb_players+1):
    player_name = input('Entrez le Nom ou le Pseudo du Joueur N°'+ str(cpt_player) +' : \n ->')
    
    if cpt_player != 1 and (player_name in tableau_players):
        print('Attention : le Nom ou le Pseudo ' +str(player_name) +'existe déja, merci de choisir un autre Nom')
    else:
        tableau_players.append(player_name)
        cpt_player += 1

cpt_bot=1
while cpt_bot != (nb_bot+1):
    bot_name=('Bot'+ str(cpt_bot))
    tableau_players.append(bot_name)
    cpt_bot += 1


#Attribution des rôles
import random

tableau_attribution = []

for name in tableau_players:
    role_name_lu = random.choice(tableau_roles)
    role,nb_fois,nb_max = role_name_lu.split(":")
    if int(nb_fois) == 0:
        if int(nb_max) != 0:
            valeur=(str(name) +':'+ str(role))
            tableau_attribution.append(valeur) 
            nb_max = int(nb_max) - 1
            index = tableau_roles.index(role_name_lu)
            tableau_roles[index] = (str(role) +":"+ str(nb_fois) +":"+ str(nb_max))
        else:
            tableau_roles.remove(role_name_lu)
    elif int(nb_fois) == 1:
        valeur=(str(name) +':'+ str(role))
        tableau_attribution.append(valeur)
        tableau_roles.remove(role_name_lu)

print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("tableau_players: ",tableau_players)
print("tableau_attribution: ",tableau_attribution)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------\n")