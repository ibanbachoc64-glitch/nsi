import turtle
import random
import formes



def choix_couleur():
    return{
    "fenetres" : ["#FFD166","#BFC7CE","#4A90E2","#A7C7E7"],
    "building" : random.choice(["#1E1E1E","#E5E5E5","#4B4E57","#C0C5CE"]),
    "bureaux" : random.choice(["#D8D2C2","#B8A99A","#5DA9C5","#9FA6B2"]),
    "habitation" : random.choice(["#8B3A3A","#F5E6D3","#A0522D","#A3B18A"])}





def fenetre_barres(x,y,largeur,couleur_barres,hauteur):
    #les bandes verticales, entre les bandes, penser à ajouter 
    largeur_barre = largeur/10
    ecart_barres = formes.divise_coord(largeur,3)
    b1=formes.Rectangle(x+(ecart_barres-largeur_barre/2),y,largeur_barre,hauteur)
    b1.dessine().colorier_rectangle(couleur_barres)
    b2=formes.Rectangle(x+(ecart_barres*2-largeur_barre/2),y,largeur_barre,hauteur)  #on a crée les barres, mtn il faut créer les fenêtres
    b2.dessine().colorier_rectangle(couleur_barres)
    

class fenetres:
    def __init__(self,largeurbd,hauteurbd,x,y,couleurs):
        self.hauteurbd=hauteurbd
        self.largeurbd=largeurbd
        self.x=x
        self.y=y
        self.typefenetres= random.randint(1,3)
        self.couleurs = couleurs

        

    