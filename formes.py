import turtle 
import esthetique
#les docstr sont faites avec l'extension autodocstr de python sur vsc

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

def carre(cote,xhaut,yhaut):
    """_summary_

    Args:
        cote (int): longueur du coté
        xhaut (_type_): point de départ des abscisses, situé à gauche
        yhaut (_type_): point de départ des ordonnées, situé en haut du carré
    """
    c = Rectangle(xhaut,yhaut,cote,cote)
    c.dessine()

class Rectangle:
    def __init__(self,xdebut,ydebut,largeur,hauteur):
        self.xdebut = xdebut
        self.ydebut =ydebut
        self.largeur = largeur
        self.hauteur = hauteur

    def dessine(self):
        trait(self.xdebut, self.ydebut, self.xdebut +self.largeur, self.ydebut)                
        trait(self.xdebut +self.largeur, self.ydebut, self.xdebut+ self.largeur, self.ydebut -self.hauteur)  
        trait(self.xdebut +self.largeur, self.ydebut- self.hauteur, self.xdebut, self.ydebut- self.hauteur)  
        trait(self.xdebut, self.ydebut - self.hauteur, self.xdebut, self.ydebut) 

    def colorier_rectangle(self,couleur):
        turtle.penup()
        turtle.goto(self.xdebut,self.ydebut)
        turtle.pendown()
        turtle.fillcolor(couleur)
        turtle.beginfill()
        for i in range(2):
            turtle.fd(self.largeur)
            turtle.right(90)
            turtle.fd(self.hauteur)
            turtle.right(90)
        turtle.end_fill()




"""def grille(largeur,hauteur):
        for i in range:
            if largeur -10*i %i != 0:
               nb_colonnes = i            #les -10 sont des valeurs hypothétiques, il faudra par la suite les remplacer par de vraies valeurs
            if hauteur - 10*i %i != 0:      #les -10 correspondent à longueur barre/2
               nb_lignes = i
        return nb_colonnes,nb_lignes"""


def divise_coord(val_divise,nb_divise):
    if val_divise !=0:
        return val_divise/nb_divise
    return 0

def nb_fenetres(val,taille_fenetre,ecart):
    v = val/taille_fenetre
    return val/v*ecart

