

#mon premier programme
import subprocess
import os 
os.system("cls") 
username = input('Quel est ton pseudo ? \n => ')
print(username)
#username => variable temporaire le temps de fusionner


reponse=0
while reponse!="fin" and reponse!="exit":
    os.system("cls")
    print('\n --------------------------------------')
    print(' - Bienvenue',username,'dans notre Jeux de Ouf   -')
    print(' -                                    -')
    print(' -    => 1 : Substraction             -')
    print(' -    => 2 : Aleatory                 -')
    print(' -                                    -')
    print(' - tapez "fin" ou "exit" pour sortir  -')
    print(' --------------------------------------') 
    reponse = input("- A quel jeu veux-tu jouer ? \n => ")
    if reponse == "1":
        print('\n      Tu as choisi de jouer a Substraction')
        lance_prog=input(" Tape 'Entrée' pour lancer le jeu")
        subprocess.call(["python.exe", "Jeu1.py"])
    elif reponse == "2":
        print('\n      Tu as choisi de jouer a Aleatory')
        lance_prog=input(" Tape 'Entrée' pour lancer le jeu")
        subprocess.call(["python.exe", "Jeu2.py"])
    elif reponse!="fin" and reponse!="exit":
        print('\n      ERREUR : Numero de jeux inconnu !')
        lance_prog=input(" Tape 'Entrée' pour continuer")
os.system("cls") 
print('\n --------------------------------------')
print(' - A bientot ',username,'dans notre Jeux de Ouf   -')
print(' --------------------------------------\n')
