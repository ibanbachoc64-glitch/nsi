import turtle
import random
from formes import *
import time

def choix_couleur():
    return{
    "fenetres" : random.choice(["#FFD166","#BFC7CE","#4A90E2","#A7C7E7"]),
    "building" : random.choice(["#1E1E1E","#E5E5E5","#4B4E57","#C0C5CE"]),
    "bureaux" : random.choice(["#D8D2C2","#B8A99A","#5DA9C5","#9FA6B2"]),
    "habitation" : random.choice(["#8B3A3A","#F5E6D3","#A0522D","#A3B18A"])}


def colorier_rectangle(x,y,couleur,largeur,hauteur):

    turtle.fillcolor(couleur)
    turtle.begin_fill()

    rectangle(x,y,largeur,hauteur)

    turtle.end_fill()


def choix_toit():
    return random.randint(1,3)


def colorier_toit(x,y,couleur,largeur,hauteur, choix):
    '''
    x,y = int = coords
    largeur = int = largeur rectangle
    hauteur = int = hauteur rectangle
    couleur = str = couleur du building et du toit
    choix = int = choix du type de toit
    '''


    if choix == 1:
        turtle.fillcolor(couleur)
        turtle.begin_fill()

        toit1(x,y,largeur,hauteur/2)

        turtle.end_fill()

    elif choix == 2:

        turtle.fillcolor(couleur)
        turtle.begin_fill()

        toit2(x,y,largeur)

        turtle.end_fill()

    else:

        turtle.fillcolor(couleur)
        turtle.begin_fill()

        toit3(x,y,largeur,hauteur/2)

        turtle.end_fill()






def building(x,y, largeur, hauteur, couleur,choix):
    '''
    x,y = int = coords
    largeur = int = largeur rectangle
    hauteur = int = hauteur rectangle
    couleur = str = couleur du building et du toit
    choix = int = choix du type de toit
    '''

    colorier_rectangle(x,y,couleur,largeur,hauteur)
    colorier_toit(x,y,couleur, largeur, hauteur,choix)





#building(0,0,100,50, "#FFD166", 3)


def main(x,y,n):

    '''
    creer la ligne de building, qui demarre en x y, prend aussi en parametre le plan n.
    x = int = coords x
    y = int = coords y
    n = int = numero du plan
    '''

    position(x,y)

    largeur = random.randint(50,100)
    hauteur = random.randint(50,150)

    couleur = choix_couleur()
    choix = choix_toit()

    building(x,y,largeur,hauteur,couleur['building'],choix)

main(-200,0,1)


if __name__==("__main__"):

    pass


