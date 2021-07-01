# %%
from math import *
from random import *
from tkinter import *
import os
import time

# TODO finir bouton vitesse (utiliser get pour récupérer la valeur) et continuer bouton pourcentage vie (j'ai juste apporté des mofications dans la fonction initialiser mais ça fonctionne pas bien)
# TODO Mettre en place les boutons restants boutons échelles (utiliser get pour récupérer la valeur)
# TODO améliorer la déclaration des dimensions de notre fenêtre

fenetre = Tk()
fenetre.title("Le jeu de la vie")

#Les couleurs c'est pour visualiser les frames
frame_jeu_de_vie = Frame(fenetre, width=600, height=600, bg = "Green")
frame_jeu_de_vie.grid(row = 0, column = 0, sticky = "nsew", rowspan = 2)

canvas = Canvas(frame_jeu_de_vie, width=600, height=600, bg = "Orange")
#canvas = Canvas(fenetre, width=side*ligne, height=side*colonne)

#Le canevas remplit bien toute la frame, c'est le grille de jeu qu'il faut redimensionner
canvas.pack(expand = 1, fill=BOTH)

frame_menu_haut = Frame(fenetre,width = 200, height = 300, bg = "Grey")
frame_menu_haut.grid(row = 0, column = 1,sticky = "nsew")

frame_menu_bas = Frame(fenetre,width = 200, height = 300, bg = "Red")
frame_menu_bas.grid(row = 1, column = 1,sticky = "sew")

#M=[]
ligne= 25
colonne= 25

def initialiser(pourcentage_vie=1): # on voit bien que c'est broken il faudrait tout avoir en rouge
    x = 0 # valeur fixée arbitrairement
    y = 0 # valeur fixée arbitrairement
    global ligne
    global colonne
    global rectangles
    global M
    M = []
    rectangles = []
    global cmpt_vie 
    cmpt_vie = 0

    for i in range(ligne):
        M.append([]) # Liste de liste qui contient les valeurs des cellules (1:vivante et 0:morte)
        rectangles.append([]) # Liste de liste qui contient tous les rectangles
        for j in range(colonne):
            # pourcentage_vie

            if cmpt_vie<pourcentage_vie*colonne*ligne: # le problème vient de là
                rand = randint(0,1)
            else:
                rand = 0

            if (rand==1):
                cmpt_vie+=1

            rect = canvas.create_rectangle(x, y, x+20, y+20, fill="white") # (x,y) les coordonnées du coin supérieur gauche et (x+10, y+10) celles du coin inférieur droit.
            rectangles[i].append(rect)
            M[i].append(rand)
            x += 22 # l'ordonnée est fixé à 10, on incrémente "l'abscisse" uniquement (2ème boucle for)
        # on est dans la 1ere boucle for
        x = 0 # on fixe l'abscisse
        y += 22 # on incrémente l'ordonnée
    afficher_damier()
    




def afficher_damier(): #TODO mettre vitesse peut être en param
    #time.sleep(vitesse)
    #os.system("clear")
    for i in range(ligne):
        for j in range(colonne):
            if M[i][j]==1:
                couleur = "red"
            else:
                couleur = "white" # mettre le end car /n par défaut
            canvas.itemconfig(rectangles[i][j], fill=couleur)

        #print("\n")



def nb_voisin (i,j):
        global ligne
        global colonne
        nb_voisin=0
        
        if M[i][(j+1)%colonne]!=0:
            nb_voisin+=1

        if M[i][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if M[(i+1)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1
        
        if M[(i+1)%ligne][j]!=0:
            nb_voisin+=1

        if M[(i+1)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][j]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        return nb_voisin

def nouvelle_generation():
        global ligne
        global colonne
        global t
        global M
        voisin=0
        vecteur=[]
        x=0
        y=0

        # calculer le damier de la nouvelle génération en appliquant les règles

        for i in range(ligne):
            vecteur.append([])
            for j in range (colonne):
                voisin=nb_voisin(i,j)
                if voisin==2:
                    vecteur[i].append(M[i][j])
                    continue
                if voisin==3:
                    vecteur[i].append(1)
                    continue
                vecteur[i].append(0)
        # copier le temp dans le principale        
        M=vecteur.copy()
        afficher_damier()
        global ID_nouvelle_generation
        ID_nouvelle_generation = fenetre.after(200, nouvelle_generation)



def arreter():
    fenetre.after_cancel(ID_nouvelle_generation)

def quitter():
    fenetre.destroy()


#initialiser()

Initialiser = Button(frame_menu_haut, text="Initialiser", command=initialiser, fg = "blue", width =11)
Initialiser.grid(row = 2, column = 0, sticky = "se")

Lancer = Button(frame_menu_haut, text="Lancer", command=nouvelle_generation, fg = "blue", width = 11)
Lancer.grid(row = 0, column = 0)

Arreter = Button(frame_menu_haut, text="Arreter", command = arreter, fg = "blue", width = 11)
Arreter.grid(row = 1, column = 0)

Quitter = Button(frame_menu_bas, text="Quitter", command = quitter, fg = "blue", width = 11)
Quitter.grid(row = 3, column = 0)

Taille = Scale(frame_menu_bas, orient='horizontal', from_=0, to=100, resolution=1, label='Taille de la grille',fg = "blue")
Taille.grid(row = 0, column = 0)

Vie = Scale(frame_menu_bas, orient='horizontal', from_=0, to=100, resolution=1, label='% de vie', fg = "blue")
Vie.grid(row = 1, column = 0)

#FIXME
def vitesse():
    global Vitesse
    #afficher_damier(10-Vitesse.get()) # si c'est 0 on sleep 10s si la vitesse est de 10 on sleep de 0s

Vitesse = Scale(frame_menu_bas, orient='horizontal', from_=0, to=10, resolution=1, label='Vitesse',command = vitesse, fg = "blue")
Vitesse.grid(row = 2, column = 0)

#fenetre.after(500, life)
fenetre.mainloop()


