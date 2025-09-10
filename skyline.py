import formes
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
        formes.Rectangle(self.x,self.y,self.largeur,self.hauteur).dessine().colorier(self.couleur["building"])
        return self

    def creation_fenetre(self):
        esthetique.fenetres(self.hauteur,self.x,self.y,self.couleur["fenetres"]).dessine()
        return self

    def ajout_toit(self):
        typetoit = random.randint(1,3)
        if typetoit == 1:
            esthetique.toit1(self.largeur,self.x,self.y,self.couleur["toits"]).dessine().colorie()
        elif typetoit==2:
            esthetique.toit2(self.x,self.y,self.largeur,self.couleur["toits"]).dessine().colorie()
        elif typetoit==3:
            esthetique.toit3(self.x,self.y,self.hauteur,self.largeur,self.couleur["toits"])

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