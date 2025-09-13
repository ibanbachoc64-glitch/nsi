import turtle
import random
import time

#doc string faite à l'aide de chat GPT, en donnant la fonction en prompt et en demandant de generer une doc string.

#Analyse: les docs strings sont trés précise donc on trouve l'utilisation de l'IA pertinante dans ce contexte.

def position(x,y):
    """
    Déplace le curseur de la tortue à la position spécifiée sans tracer de ligne.

    Paramètres
    ----------
    x : int ou float
        Coordonnée horizontale de la position cible.
    y : int ou float
        Coordonnée verticale de la position cible.

    Effets
    ------
    - Soulève le stylo pour éviter de tracer pendant le déplacement.
    - Déplace la tortue aux coordonnées (x, y).
    - Réinitialise l’orientation de la tortue à 0° (vers la droite).
    - Repose le stylo pour permettre un tracé ultérieur.
    """
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.down()


def trait(xdebut,ydebut,xfin,yfin):
    """
    Trace un segment entre deux points donnés.

    Paramètres
    ----------
    xdebut : int ou float
        Coordonnée en abscisse du point de départ du trait.
    ydebut : int ou float
        Coordonnée en ordonnée du point de départ du trait.
    xfin : int ou float
        Coordonnée en abscisse du point d’arrivée du trait.
    yfin : int ou float
        Coordonnée en ordonnée du point d’arrivée du trait.

    Effets
    ------
    - Soulève le stylo.
    - Déplace la tortue au point de départ (xdebut, ydebut).
    - Abaisse le stylo.
    - Trace un segment jusqu’au point d’arrivée (xfin, yfin).
    """

    turtle.penup()
    turtle.goto(xdebut,ydebut)
    turtle.pendown()
    turtle.goto(xfin,yfin)

def carre(xhaut,yhaut,cote):
    """
    Trace un carré à partir du coin supérieur gauche.

    Paramètres
    ----------
    xhaut : int ou float
        Coordonnée en abscisse du coin supérieur gauche du carré.
    yhaut : int ou float
        Coordonnée en ordonnée du coin supérieur gauche du carré.
    cote : int ou float
        Longueur du côté du carré.

    Effets
    ------
    - Utilise la fonction `trait` pour tracer successivement les 4 côtés.
    - Le tracé commence au coin supérieur gauche (xhaut, yhaut).
    """
    #commence dans le coin haut gauche
    trait(xhaut,yhaut,xhaut+cote,yhaut)
    trait(xhaut+cote,yhaut,xhaut+cote,yhaut-cote)
    trait(xhaut+cote,yhaut-cote,xhaut,yhaut-cote)
    trait(xhaut,yhaut-cote,xhaut,yhaut)

def rectangle(xdebut,ydebut,largeur,hauteur):
    """
    Trace un rectangle à partir du coin supérieur gauche.

    Paramètres
    ----------
    xdebut : int ou float
        Coordonnée en abscisse du coin supérieur gauche du rectangle.
    ydebut : int ou float
        Coordonnée en ordonnée du coin supérieur gauche du rectangle.
    largeur : int ou float
        Largeur du rectangle (longueur horizontale).
    hauteur : int ou float
        Hauteur du rectangle (longueur verticale).

    Effets
    ------
    - Utilise la fonction `trait` pour tracer successivement les 4 côtés.
    - Le tracé commence au coin supérieur gauche (xdebut, ydebut).
    """
    #commence dans le coin gauche du rectangle (haut)
    trait(xdebut, ydebut, xdebut +largeur, ydebut)
    trait(xdebut +largeur, ydebut, xdebut+ largeur, ydebut -hauteur)
    trait(xdebut +largeur, ydebut- hauteur, xdebut, ydebut- hauteur)
    trait(xdebut, ydebut - hauteur, xdebut, ydebut)


def toit1(xdebut,ydebut,largeur, hauteur):
    """
    Trace un toit triangulaire (triangle isocèle) à partir de la base horizontale.

    Paramètres
    ----------
    xdebut : int ou float
        Coordonnée en abscisse du point de départ (coin gauche de la base).
    ydebut : int ou float
        Coordonnée en ordonnée du point de départ (coin gauche de la base).
    largeur : int ou float
        Largeur de la base du triangle.
    hauteur : int ou float
        Hauteur du sommet du triangle par rapport à la base.

    Effets
    ------
    - Trace la base horizontale du triangle.
    - Trace les deux côtés reliant la base au sommet.
    """
    trait(xdebut,ydebut,xdebut + largeur ,ydebut)
    trait(xdebut+largeur, ydebut, xdebut + largeur/2, ydebut + hauteur)
    trait(xdebut+largeur/2, ydebut + hauteur, xdebut, ydebut)

def toit2(x,y,largeur):
    """
    Trace un toit en demi-cercle à partir du coin supérieur gauche.

    Paramètres
    ----------
    x : int ou float
        Coordonnée en abscisse du coin supérieur gauche du rectangle englobant le demi-cercle.
    y : int ou float
        Coordonnée en ordonnée du coin supérieur gauche du rectangle englobant le demi-cercle.
    largeur : int ou float
        Largeur du demi-cercle (le rayon est égal à largeur / 2).

    Effets
    ------
    - Déplace la tortue au point (x, y).
    - Trace un demi-cercle de rayon `largeur / 2` orienté vers le haut.
    - Réinitialise l’orientation de la tortue à 0° (vers la droite).
    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(-largeur/2, 180)


    turtle.setheading(0)




def toit3(x_base, y_base, largeur, hauteur):
    """
    Trace un toit en escalier composé d'un nombre fixe de marches.

    Paramètres
    ----------
    x_base : int ou float
        Coordonnée en abscisse du coin inférieur gauche de la base du toit.
    y_base : int ou float
        Coordonnée en ordonnée du coin inférieur gauche de la base du toit.
    largeur : int ou float
        Largeur totale du toit.
    hauteur : int ou float
        Hauteur totale du toit.

    Effets
    ------
    - Divise le toit en `nombre_marches` marches (par défaut 4).
    - Trace les marches en montant sur le côté gauche, puis en redescendant du côté droit.
    - Utilise la fonction `trait` pour tracer chaque segment.
    """
    nb_marches =  4
    largeur_marche = largeur / (nb_marches * 2)
    hauteur_marche = hauteur / nb_marches


    x = x_base
    y = y_base

    #on monte a gauche
    for i in range(nb_marches):

        trait(x, y, x + largeur_marche, y)
        x += largeur_marche

        trait(x, y, x, y + hauteur_marche)
        y += hauteur_marche

    #on descend a droite
    for i in range(nb_marches):

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

    time.sleep(1)
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

