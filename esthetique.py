import turtle
import random
import formes



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
    turtle.beginfill()
    for i in range(2):
        turtle.fd(largeur)
        turtle.right(90)
        turtle.fd(hauteur)
        turtle.right(90)
    turtle.end_fill()


def fenetre_barres(x,y,largeur,colorsList,hauteur):
    #les bandes verticales, entre les bandes, penser à ajouter 
    largeur_barre = largeur/10
    ecart_barres = formes.divise_coord(largeur,3)
    formes.rectangle(x+(ecart_barres-largeur_barre/2),y,largeur_barre,hauteur)
    