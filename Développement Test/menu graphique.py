"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# -----------------DEBUT FENETRE 1 ----------------
# On crée une fenêtre, racine de notre interface
fenetre = Tk()
# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine

champ_label = Label(fenetre, text="Salut c'est Anthony")

bouton_quitter = Button(fenetre, text="Continuer", command=fenetre.quit)
bouton_quitter.pack()

var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack() 

var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
var_case.get()


# On affiche le label dans la fenêtre
champ_label.pack()


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
# -----------------FIN FENETRE 1 ----------------

# -----------------DEBUT FENETRE 2 ----------------
fenetre2 = Tk()

ligne_select = var_texte
champ_label = Label(fenetre, text="Salut c'est Anthony")

champ_label2 = Label(fenetre2, text=ligne_select)

boutton_var_case = Button(fenetre2, text=var_case.get())
boutton_var_case.pack()

bouton_quitter2 = Button(fenetre2, text="Continuer", command=fenetre2.quit)
bouton_quitter2.pack()

liste = Listbox(fenetre2)
liste.pack()

liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")

fenetre2.mainloop()
# -----------------FIN FENETRE 2 ----------------

# -----------------DEBUT FENETRE 3 ----------------
fenetre3 = Tk()

selection = liste.curselection()
boutton_var_case2 = Button(fenetre3, text=selection)
boutton_var_case2.pack()
bouton_quitter3 = Button(fenetre3, text="Quitter", command=fenetre3.quit)
bouton_quitter3.pack()
fenetre3.mainloop()

# -----------------FIN FENETRE 3 ----------------
 
#------------------DEBUT FENETRE 4---------------

fenetre


