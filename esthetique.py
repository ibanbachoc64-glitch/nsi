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

def colorier_toit1(x,y,couleur,largeur,hauteur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    toit1(x,y,largeur,hauteur/2)

    turtle.end_fill()

def colorier_toit2(x,y,largeur,couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    toit2(x,y,largeur)

    turtle.end_fill()

def colorier_toit3(x,y,couleur,largeur,hauteur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    toit3(x,y,largeur,hauteur/2)

    turtle.end_fill()

def choixtoit():
    return random.randint(3,3)



def building(x,y):
    position(-200,0)
    largeur = random.randint(50,100)
    hauteur = random.randint(50,150)

    choix = choixtoit()
    couleur = choix_couleur()

    colorier_rectangle(x,y,couleur['building'],largeur,hauteur)

    if choix == 1:
        colorier_toit1(x,y,couleur['building'],largeur,hauteur)
    elif choix == 2:
        colorier_toit2(x,y,largeur,couleur['building'])
    else: # c'est le 3
        colorier_toit3(x,y,couleur['building'],largeur,hauteur)


if __name__==("__main__"):

    #en haut a gauche
    colorier_toit1(-400,100,"#FFD166",100,50)
    #en bas a gauche
    colorier_toit1(-400,-100,"#FFD166",150,100)
    #en haut a droite
    colorier_toit1(400,100,"#FFD166",200,150)

    time.sleep(2)
    turtle.clearscreen()

    position(-400,100)
    #en haut a gauche
    colorier_toit2(-400,100,100,"#FFD166",)

    position(-400,-100)
    #en bas a gauche
    colorier_toit2(-400,-100,150,"#FFD166",)

    position(400,100)
    #en haut a droite
    colorier_toit2(400,100,200,"#FFD166",)

    time.sleep(2)
    turtle.clearscreen()


    position(-400,100)
    #en haut a gauche
    colorier_toit3(-400,100,"#FFD166",100,50)

    position(-400,-100)
    #en bas a gauche
    colorier_toit3(-400,-100,"#FFD166",150,100)

    position(400,100)
    #en haut a droite
    colorier_toit3(400,100,"#FFD166",300,150)

    time.sleep(2)
    turtle.clearscreen()

    for i in range(3):
        building(0,0)
        time.sleep(1)
        turtle.clearscreen()


