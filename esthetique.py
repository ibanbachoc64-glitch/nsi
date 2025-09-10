import turtle
import random
from formes import *


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

def choixtoit():
    return random.randint(1,2)



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



