import turtle
import random

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
    crayon = turtle.Turtle()
    crayon.penup()
    crayon.goto(xdebut,ydebut)
    crayon.pendown()
    crayon.goto(xfin,yfin)



def toit1(xdebut,ydebut,largeur, hauteur):
    """
    Trace un triangle équilatéral sur une base de longueur x
    x = int = longueur de la largeur du rectangle
    REFAIRE DOCSTR
    """
    trait(xdebut,ydebut,xdebut + largeur ,ydebut)
    trait(xdebut+largeur, ydebut, largeur/2, ydebut + hauteur)
    trait(largeur/2, ydebut + hauteur, xdebut, ydebut)

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



def toit3(xdebut,ydebut,xfin,yfin,hauteur):
    """
    Trace un trapeze isocele de base x et de hauteur x/2
    x = int = largeur du trapzez
    """
    trait(xdebut,ydebut,xfin,yfin)
    trait(xfin, yfin, xdebut*(2/3),ydebut+hauteur)



def carre(cote,xhaut,yhaut):
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






if __name__==("__main__"):
        #test toit1
    position(-400, 300) #en haut a gauche
    toit1(20)
    position(-400, -300) #en bas a gauche
    toit1(50)
    position(300,300) #en haut a droite
    toit1(100)

    turtle.clearscreen()

    #test toit2
    position(-400, 300) #en haut a gauche
    toit2(20)
    position(-400, -300) #en bas a gauche
    toit2(50)
    position(300,300) #en haut a droite
    toit2(100)

    turtle.clearscreen()

    #test rectangle
    position(-400, 300) #en haut a gauche
    rectangle(10,20)
    position(-400, -300) #en bas a gauche
    rectangle(20,40)
    position(400,300) #en haut a droite
    rectangle(30,60)

    turtle.clearscreen()
    #test carre
    position(-400, 300) #en haut a gauche
    carre(10)
    position(-400, -300) #en bas a gauche
    carre(20)
    position(400,300) #en haut a droite
    carre(30)

    turtle.clearscreen()
