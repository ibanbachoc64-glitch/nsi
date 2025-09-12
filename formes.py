import turtle
import random
import time

def position(x,y):
    '''
    Déplace le stylo à la position (x, y) sans tracer de ligne
    x = int
    y = int
    '''
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.down()


def trait(xdebut,ydebut,xfin,yfin):
    """_summary_

    Args:
        xdebut (int): coordonnée des abscisses de départ du trait
        ydebut (int): coordonnée des ordonnées de départ du trait
        xfin (int): abscisse de fin du trait
        yfin (int): ordonnée de fin du trait
    """

    turtle.penup()
    turtle.goto(xdebut,ydebut)
    turtle.pendown()
    turtle.goto(xfin,yfin)

def carre(xhaut,yhaut,cote):
    """_summary_

    Args:
        cote (int): longueur du coté
        xhaut (_type_): point de départ des abscisses, situé à gauche
        yhaut (_type_): point de départ des ordonnées, situé en haut du carré
    """
    #commence dans le coin haut gauche
    trait(xhaut,yhaut,xhaut+cote,yhaut)
    trait(xhaut+cote,yhaut,xhaut+cote,yhaut-cote)
    trait(xhaut+cote,yhaut-cote,xhaut,yhaut-cote)
    trait(xhaut,yhaut-cote,xhaut,yhaut)

def rectangle(xdebut,ydebut,largeur,hauteur):
    """_summary_

    Args:
        xdebut (_int_): abscisse de départ
        ydebut (_int_): ordonnée de départ
        largeur (_int_): largeur du rectangle
        hauteur (_int_): hauteur voulue pour le rectangle
    """
    #commence dans le coin gauche du rectangle (haut)
    trait(xdebut, ydebut, xdebut +largeur, ydebut)
    trait(xdebut +largeur, ydebut, xdebut+ largeur, ydebut -hauteur)
    trait(xdebut +largeur, ydebut- hauteur, xdebut, ydebut- hauteur)
    trait(xdebut, ydebut - hauteur, xdebut, ydebut)


def toit1(xdebut,ydebut,largeur, hauteur):
    """
    Trace un triangle équilatéral au coords x et y, avec une largeur et une hauteur
    xdebut = coords x = int
    ydebut = coordsy = int
    largeur = largeur du triangle = int
    hauteur = hauteur du sommet = int

    """
    trait(xdebut,ydebut,xdebut + largeur ,ydebut)
    trait(xdebut+largeur, ydebut, xdebut + largeur/2, ydebut + hauteur)
    trait(xdebut+largeur/2, ydebut + hauteur, xdebut, ydebut)

def toit2(x,y,largeur):
    """
    Trace un demi cercle de rayon largeur/2
    x = int = x du coin superieur gauche
    y = int = y du coin superieur gauche
    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(-largeur/2, 180)


    turtle.setheading(0)




def toit3(x_base, y_base, largeur, hauteur):

    nombre_marches =  4
    largeur_marche = largeur / (nombre_marches * 2)
    hauteur_marche = hauteur / nombre_marches
    
    x = x_base
    y = y_base

    #on monte a gauche
    for i in range(nombre_marches):
        trait(x, y, x + largeur_marche, y)
        x += largeur_marche
        
        trait(x, y, x, y + hauteur_marche)
        y += hauteur_marche
        
    #on descend a droite
    for i in range(nombre_marches):
        trait(x, y, x, y - hauteur_marche)
        y -= hauteur_marche
        
        trait(x, y, x + largeur_marche, y)
        x += largeur_marche

if __name__==("__main__"):
    #test toit1
    #en haut a gauche
    toit1(-400,200,50,25)

    #en bas a gauche
    toit1(-400,-200,100,50)

    #en haut a droite
    toit1(400,200,150,100)

    time.sleep(2)
    turtle.clearscreen()

    #test toit2
    #en haut a gauche
    toit2(-400,200,50)

    #en bas a gauche
    toit2(-400,-200,100)

    #en haut a droite
    toit2(400,200,150)

    time.sleep(2)
    turtle.clearscreen()

    #test toit3
    #en haut a gauche
    toit3(-400,200,50,25)

    #en bas a gauche
    toit3(-400,-200,100,50)

    #en haut a droite
    toit3(400,200,150,100)

    time.sleep(2)
    turtle.clearscreen()


    #test rectangle
    #en haut a gauche
    rectangle(-400,200,50,25)

    #en bas a gauche
    rectangle(-400,-200,100,50)

    #en haut a droite
    rectangle(400,200,150,100)

    time.sleep(2)
    turtle.clearscreen()
    #test carre

    #en haut a gauche
    carre(-400,200,50)

    #en bas a gauche
    carre(-400,-200,100)

    #en haut a droite
    carre(400,200,150)



