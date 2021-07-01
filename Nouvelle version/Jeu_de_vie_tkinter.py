# %%
from math import *
from random import *
from tkinter import *
from random import shuffle

"""

    Implémentation des frames et canvas
    
"""
 
fenetre = Tk()
fenetre.title("Le jeu de la vie")

global dimension_frame
dimension_frame = 600

frame_jeu_de_vie = Frame(fenetre, width=dimension_frame, height=dimension_frame)
# frame située à gauche de l'écran
frame_jeu_de_vie.grid(row = 0, column = 0, sticky = "nsew", rowspan = 2)

canvas = Canvas(frame_jeu_de_vie, width=dimension_frame, height=dimension_frame, bg = "grey")
canvas.pack(expand = 1, fill=BOTH)

frame_menu_haut = Frame(fenetre,width = 200, height = 300)
# frame située en haut à droite de l'écran
frame_menu_haut.grid(row = 0, column = 1,sticky = "nsew")

frame_menu_bas = Frame(fenetre,width = 200, height = 300)
# frame située en bas à droite de l'écran
frame_menu_bas.grid(row = 1, column = 1,sticky = "sew")


"""
    Implémentation des fonctions pour réaliser le jeu de la vie
"""


def initialiser():
    """
    Déclaration et intialisation des variables
    """
    x = 0 #abcisse
    y = 0 #ordonnée
    global ligne
    global colonne
    global rectangles
    global grille
    grille = [] # liste vide
    rectangles = [] # liste vide
    

    """
    Initialisation à 0 de notre grille
    """
    ligne = colonne = Taille.get()
    grille = [[0 for i in range(ligne)] for j in range(colonne)] # on initialise à 0 la grille, toutes les cellules sont mortes

    """
    Gestion du pourcentage de vie
    """
    nombre_cellules_en_vie=ligne*colonne*(Vie.get()/100)

    combinaisons_coordonnees = [] # stocke toutes les combinaisons de coordonnées possibles, sous forme d'une liste de tuples
    for i in range(ligne):
        for j in range(colonne):
            combinaisons_coordonnees.append((i, j)) # on ajoute à notre liste, le tuple contenant les coordonnées
    
    shuffle(combinaisons_coordonnees) # permet de mélanger la liste de tuple (coordonnées) de façon aléatoire

    for i in range(int(nombre_cellules_en_vie)): # on caste nombre_cellules_en_vie en tant que entier 
        i, j = combinaisons_coordonnees.pop() # la méthode pop permet de retourner le dernier tuple de la liste, on récupère ce tuple dans deux variables différentes
        grille[i][j] = 1 # cellule vivante

    """
    On dessine les rectangles (les cellules) de notre grille en prenant en compte la taille de la grille
    """
    for i in range(ligne):
        rectangles.append([]) # Liste de liste qui contient tous les rectangles
        
        for j in range(colonne):
            # dimension_frame/ligne est la dimension des côtés de nos rectangles qui varie en fonction de la taille de la grille sélectionnée
            rect = canvas.create_rectangle(x, y, x+(dimension_frame/ligne), y+(dimension_frame/ligne), fill="white") # (x,y) les coordonnées du coin supérieur gauche et (x+10, y+10) celles du coin inférieur droit.
            rectangles[i].append(rect) # ajout de l'élément rect dans notre liste de liste
            x += (dimension_frame/ligne) # l'ordonnée est fixé, on incrémente "l'abscisse" uniquement 
        
        x = 0 # on fixe l'abscisse à 0
        y += (dimension_frame/ligne) # on incrémente l'ordonnée
    
    afficher_grille()
    



def afficher_grille(): 
    for i in range(ligne):
        for j in range(colonne):
            if grille[i][j]==1:
                couleur = "red"
            else:
                couleur = "white"
            canvas.itemconfig(rectangles[i][j], fill=couleur) # on remplit les rectangles avec la couleur définie au préalable



"""
Aucune modification a apportée dans cette fonction nb_voisin c'est-à-dire aucune fonction tkinter n'a été appelée ici
"""

def nb_voisin (i,j):
        global ligne
        global colonne
        nb_voisin=0
        
        if grille[i][(j+1)%colonne]!=0:
            nb_voisin+=1

        if grille[i][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if grille[(i+1)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1
        
        if grille[(i+1)%ligne][j]!=0:
            nb_voisin+=1

        if grille[(i+1)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        if grille[(i-1+ligne)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if grille[(i-1+ligne)%ligne][j]!=0:
            nb_voisin+=1

        if grille[(i-1+ligne)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        return nb_voisin

"""
gestion de la nouvelle generation de la grille en prenant en compte la vitesse de la generation
"""
def nouvelle_generation():
        global ligne
        global colonne
        global grille
        voisin=0
        vecteur=[]
        x=0
        y=0

        vitesse = Vitesse.get() # on récupère la valeur retournée par l'échelle de la vitesse
        
        # calculer la grille de la nouvelle génération en appliquant les règles vues en TD

        for i in range(ligne):
            vecteur.append([])
            for j in range (colonne):
                voisin=nb_voisin(i,j)
                if voisin==2:
                    vecteur[i].append(grille[i][j])
                    continue
                if voisin==3:
                    vecteur[i].append(1)
                    continue
                vecteur[i].append(0)
        # copier le vecteur temporaire dans le principale        
        grille=vecteur.copy()
        afficher_grille()
        # utile pour la fonction arreter
        global ID_nouvelle_generation
        ID_nouvelle_generation = fenetre.after(1001 - 10*vitesse, nouvelle_generation) # permet de mettre un delai pour passer à la génération suivante, varie en fonction de la vitesse



def arreter():
    fenetre.after_cancel(ID_nouvelle_generation) # on s'arrrete à la dernière génération exécutée

def quitter():
    fenetre.destroy() # on quitte le programme, la commande tkinter se ferme


"""
Implémentation des boutons (button)
"""

# on fait appel à la fonction initialiser
Initialiser = Button(frame_menu_haut, text="Initialiser", command=initialiser, fg = "blue",bg="#BDC3C7",width = 20,relief=RAISED)
Initialiser.grid(row = 2, column = 0, sticky = "se")

Lancer = Button(frame_menu_haut, text="Lancer", command=nouvelle_generation, fg = "blue",bg="#BDC3C7", width = 20, relief=RAISED)
Lancer.grid(row = 0, column = 0)

Arreter = Button(frame_menu_haut, text="Arreter", command = arreter, fg = "blue",bg="#BDC3C7", width = 20,relief=RAISED)
Arreter.grid(row = 1, column = 0)

Quitter = Button(frame_menu_bas, text="Quitter", command = quitter, fg = "blue",bg="#BDC3C7", width = 20,relief=RAISED)
Quitter.grid(row = 3, column = 0)


"""
Implémentation des échelles (scale)
"""

Taille = Scale(frame_menu_bas, orient='horizontal', from_=0, to=100, resolution=1, label="Taille de la grille",fg = "blue", width = 20)
Taille.set(30)
Taille.grid(row = 0, column = 0, sticky = "ew")


Vitesse = Scale(frame_menu_bas, orient='horizontal', from_=0, to=100, resolution=1, label='Vitesse',width = 20,command = lambda val: print(val), fg = "blue")
# lambda val: print(val) permet d'afficher en temps réel sur le terminal la valeur prise par l'échelle (simple outil de vérification)
Vitesse.set(5)
Vitesse.grid(row = 2, column = 0, sticky = "ew")


Vie = Scale(frame_menu_bas, orient='horizontal', from_=0, to=100, resolution=1, label='% de vie', fg = "blue",width = 20,command = lambda val: print(val))
# lambda val: print(val) permet d'afficher en temps réel sur le terminal la valeur prise par l'échelle (simple outil de vérification)
Vie.set(20)
Vie.grid(row = 1, column = 0, sticky = "ew")



fenetre.mainloop()


