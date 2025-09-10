import formes
import esthetique
import random

class building:
    def __init__(self,largeur,hauteur,couleur,x,y,typeb):  #couleur est une liste 
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = x #coin supérieur gauche
        self.y = y
        self.typeb = typeb
     
    
    def dessine_mur_porteurs(self):
        formes.Rectangle(self.x,self.y,self.largeur,self.hauteur).dessine().colorier(self.couleur[typeb])
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
    x,y = 0,0 #changer ca plus tard
    n1= random.randint(5,8)
    for i in range(n1): #on crée les tours de derriere, il faudra voir combien on en met
        couleurs = esthetique.choix_couleur()
        largeur,hauteur = random.randint(150,250),random.randint(350,550)
        building(largeur,hauteur,couleurs,x,y,"building").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
    n2 = random.randint(7,9)
    for i in range(n2):
        couleurs = esthetique.choix_couleur()
        largeur,hauteur = random.randint(),random.randint() #changer les valeurs
        building(largeur,hauteur,x,y,couleurs,x,y,"bureaux").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
    n3 = random.randint(10,14)
    for i in range(n3):
        couleurs = esthetique.choix_couleur()
        largeur,hauteur = random.randint(),random.randint() #changer les valeurs
        building(largeur,hauteur,x,y,couleurs,x,y,"habitation").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
