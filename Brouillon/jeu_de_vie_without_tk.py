# %%
from math import *
from random import *

import os
import time


M=[]
ligne= 50
colonne= 50

def initialiser():
    global ligne
    global colonne
    for i in range(ligne):
        M.append([])
        for j in range(colonne):
            rand = randrange(2)
            M[i].append(rand)
    #print("M:",M)
    # pas besoin
    #for i in M:
        #print(i)



def afficher_damier():
    os.system("clear")
    for i in range(ligne):
        for j in range(colonne):
            if M[i][j]==1:
                print("*", end="");
            else:
                print(" ",end="") # mettre le end car /n par défaut
        print("\n")



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



# Programme principal

initialiser()

#for i in range(2):
while 1:
    time.sleep(1)
    afficher_damier()
    nouvelle_generation()

# %%
