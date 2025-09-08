from formes import *
import esthetique
import random

class building:
    def __init__(self,largeur,hauteur,couleur,x,y):  #couleur est une liste 
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = x #coin supérieur gquche
        self.y = y
     
    
    def dessine_mur_porteurs(self):
        rectangle(self.x,self.y,self.largeur,self.hauteur)
    
    def peinture_murs(self):
        esthetique.colorier_rectangle(self.x,self.y,self.couleur["building"],self.largeur,self.hauteur)

    def peinture_fenetre(self,x,y,largeur,hauteur):
        esthetique.colorier_rectangle(x,y,random.choice(self.couleur["fenetres"]),largeur,hauteur)

    def creation_fenetre(self):
        col,lig = grille(self.largeur,self.hauteur)
        type_fenetre = random.randint(1,3)
        match type_fenetre:  #cette structure a été trouvée sur w3schools.com, avec pour recherche initiale une structure de type switch en c et en go (non existente en python)
            case 1:
                #la baie vitrée
                pass
            case 2:
                print("fenetre 2, la miriade.")
            case 3:
                esthetique.fenetre_barres()

    def ajout_toit(self):
        type_toit = random.randint(0,3)
        match type_toit: #changer vers des if elif car python ne prend pas match
            case 0:
                pass #on laisse un building rectangulaire
            case 1:
                toit1()  #changer les arguments
            case 2:
                toit2() #changer les args
            case 3:
                toit3() #changer les args

def main():
    x = 0
    for i in range(5): #on crée les tours de derriere, il faudra voir combien on en met
        couleurs = esthetique.choix_couleur()
        largeur,hauteur = random.randint(100,200),random.randint(400,500) #il faudra changer ces valeurs
        y = hauteur
        b = building(largeur,hauteur,couleurs[0],x,y)
        b.dessine_mur_porteurs()
        b.peinture_murs()
        b.creation_fenetre()