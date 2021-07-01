import tkinter as tk
from tkinter import *

import os
import time
#TODO remplacer fenetre par root

fenetre = Tk()

fenetre.title("SR01 jeu de la vie")

frameMenu = Frame(fenetre, borderwidth = 10)
frameMenu.config(width = 150, height = 400)

frameMenu.pack(side = RIGHT)

#frameMenu.pack(side = RIGHT)
#frameMenu.grid(column = 0,row = 0, sticky = E)

frameMenu.update_idletasks()


#can1 = Canvas(frameMenu,width = frameMenu.winfo_width(), height = frameMenu.winfo_height(), bg = "grey")
#can1.pack()

lancerButton = Button(frameMenu,text = "lancer")
lancerButton.pack()
#lancerButton.grid(row = 1, column = 1)

initialiserButton = Button(frameMenu,text = "initialisation")
initialiserButton.pack()
#initialiserButton.grid(row = 2, column = 1)

#can1.grid(row= 1, column = 1, rowspan = 10)

frame2 = Frame(fenetre, borderwidth = 10)



fenetre.mainloop()


