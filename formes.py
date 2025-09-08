import turtle 

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
    rectangle(xhaut,yhaut,cote,cote)

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



if __name__==("__main__"):
    carre(200,0,0)
    rectangle(-200,200,200,400)