#boucle while, qui permet de répéter les actions nécessaire au déroulement du jeu, jusqu'à ce que la valeur 0 est atteinte, lorsque le joueur décide de jouer en premier.
import random
startingvalue = 50
while startingvalue > 0:
  userchoice = int(input("C'est votre tour! \n Sélectionnez une valeur comprise entre 1 et 3 \n ->"))
  if userchoice > 3:
      print("-ERREUR-")
      continue
  if userchoice < 1:
      print("-ERREUR-")
      continue
  newvalue = startingvalue - userchoice
  print(newvalue)
  if newvalue == int(0):
      break
  print("C'est à l'ordinateur de jouer")
  computer = random.randint(1, 3)
  startingvalue = newvalue - computer
  print(startingvalue)
  if startingvalue == int(0):
      break


if newvalue - computer == int(0):
    print("Désolé, vous avez perdu... Retentez votre chance !")

if startingvalue - userchoice == int(0):
    print("Félicitation, vous avez gagné")