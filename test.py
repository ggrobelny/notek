# Chargement du module tkinter
from tkinter import * # pour Python2 ce serait Tkinter

# Construction de la fenêtre principale «window»
window = Tk()
window.title('Simple exemple')
# Construction d'un simple bouton
qb = Button(window, text='Quitter', command=window.quit)

# Placement du bouton dans «window»
qb.pack()

# Lancement de la «boucle principale»
window.mainloop()