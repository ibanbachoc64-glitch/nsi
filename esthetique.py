import turtle
import random
from formes import *


def choix_couleur():
    return{
    "fenetres" : ["#FFD166","#BFC7CE","#4A90E2","#A7C7E7"],
    "building" : random.choice(["#1E1E1E","#E5E5E5","#4B4E57","#C0C5CE"]),
    "bureaux" : random.choice(["#D8D2C2","#B8A99A","#5DA9C5","#9FA6B2"]),
    "habitation" : random.choice(["#8B3A3A","#F5E6D3","#A0522D","#A3B18A"])}


def colorier_rectangle(x,y,couleur,largeur,hauteur):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(largeur)
        turtle.right(90)
        turtle.fd(hauteur)
        turtle.right(90)
    turtle.end_fill()

def choixtoit():
    return random.randint(1,2)

def building(x,y):
    largeur = random.randint(20,50)
    hauteur = random.randint(50,100)
    rectangle(x,y,largeur,hauteur)
    couleur = choix_couleur()
    if choixtoit() == 1:
        toit1(x,y, largeur, hauteur/2)
    elif choixtoit() == 2:
        toit2(x,y, largeur)

    colorier_rectangle(x,y,couleur['building'],largeur,hauteur)

