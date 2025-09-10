import turtle
import random
import formes



def choix_couleur():
    return{
    "fenetres" : ["#FFD166","#BFC7CE","#4A90E2","#A7C7E7"],
    "building" : random.choice(["#1E1E1E","#E5E5E5","#4B4E57","#C0C5CE"]),
    "bureaux" : random.choice(["#D8D2C2","#B8A99A","#5DA9C5","#9FA6B2"]),
    "habitation" : random.choice(["#8B3A3A","#F5E6D3","#A0522D","#A3B18A"])}

  

class fenetres:
    def __init__(self,largeurbd,hauteurbd,x,y,couleurs):
        self.hauteurbd=hauteurbd
        self.largeurbd=largeurbd
        self.x=x
        self.y=y
        self.typefenetres= random.randint(1,3)
        self.couleurs = couleurs

    def dessine(self):
        pass

    def fenetre_barres(self,couleur_barres,couleur_fenetres):
        #les bandes verticales, entre les bandes, penser à ajouter 
        largeur_barre = self.largeurbd/10
        hauteur_f,largeur_f = 15,7   #je ne connais pas encore les dimensions que nous allons utiliser
        demarcation = 5
        ecart_barres = formes.divise_coord(self.largeurbd,3)
        nbfenvert = formes.nb_fenetres(self.hauteurbd,hauteur_f,demarcation)
        nbfenhor=formes.nb_fenetres(self.largeurbd,largeur_f,demarcation)
        if ecart_barres!=0:
            formes.Rectangle(self.x+(ecart_barres-largeur_barre/2),self.y,largeur_barre,self.largeurbd).dessine().colorier(couleur_barres)
            formes.Rectangle(self.x+(ecart_barres*2-largeur_barre/2),self.y,largeur_barre,self.hauteurbd).dessine().colorier(couleur_barres)  #on a crée les barres, mtn il faut créer les fenêtres
            x,y = self.x+ecart_barres+largeur_barre/2+demarcation+largeur_f/2, self.y - demarcation
            for i in range(nbfenvert):
                for j in range(nbfenhor):
                    formes.Rectangle(x,y,largeur_f,hauteur_f).dessine().colorier(couleur_fenetres)
                    x+=demarcation
                y-=hauteur_f+demarcation #a chaque fois que l'on a rempli une ligne, on descend de la hauteur de la fenetre+demarcation
        else:
            pass #check des erreurs

    def baies_vitrees(self,couleur_baie):
        hauteur_f,largeur_f = self.largeurbd/25,(6/8)*self.largeurbd
        joint = hauteur_f/5
        nbfen = formes.nb_fenetres(self.hauteurbd,hauteur_f,joint)
        y= self.hauteurbd-joint
        for i in range(nbfen):
            formes.Rectangle(self.x+(self.largeurbd/2)-largeur_f,y,largeur_f,hauteur_f).dessine().colorier(couleur_baie)
            y-= hauteur_f+joint
    def miriade_fenetres(self,couleur_fenetres):
        h,l = self.largeurbd/75,self.largeurbd/100
        demarc_hor,demarc_vert = l/5,h/5
        nbfenhor = formes.nb_fenetres(self.largeur,l,demarc_hor)
        nbfen_vert = formes.nb_fenetres(self.hauteur,h,demarc_vert)
        x,y = self.x+demarc_hor+(l/2),self.y-demarc_vert
        for i in range(nbfen_vert):
            for j in range(nbfenhor):
                formes.Rectangle(x,y,l,h).dessine().colorier()
    