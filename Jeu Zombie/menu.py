from tkinter import *

menu = Tk()


menu.title("Zombie")
menu.geometry("1920x1080")

canv = Canvas(menu, width=1200, height=675, bg='green')
#canv.grid(row=0, column=0)
#c = Canvas(menu,)
canv.pack()

fond = PhotoImage(file="Fondzombie3.gif")
canv.create_image(600, 337.5, image=fond)


# bouton cliquable (50, 50)
#canv = Canvas(menu, width=128, height=128, bg='blue')
#canv.pack()
image_button = PhotoImage (file="quitter.gif")
#canv.create_image(64, 64, image=image_button)
bouton_quitter = Button(menu, image=image_button, command=menu.quit)
bouton_quitter.pack()

Label(menu, text="Anthony").pack()

menu.mainloop()