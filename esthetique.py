import random
import formes
import turtle

def couleur_hex():
    col = random.randrange(2,2**24)  #https://www.geeksforgeeks.org/python/create-random-hex-color-code-using-python/
    return hex(col)

def choix_couleur():
    return{
    "fenetres" : ["#FFD166","#BFC7CE","#4A90E2","#A7C7E7"],
    "toits" : ["#2C2C2C","#1B263B","#0D1B2A","#3E4C59","#2F1C1C","#2C3E50"],
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
        self.couleurs = couleurs #c'est juste la case du dictionnaire "fenetre"

    def dessine(self):
        if self.typefenetres == 1:
            couleur1, couleur2 =couleur_hex() ,random.choice(self.couleur)  
            self.fenetre_barres(couleur1,couleur2)
        elif self.typefenetres==2:
            couleur = random.choice(self.couleur)
            self.baies_vitrees(couleur)
        elif self.typefenetres == 3:
            couleur = random.choice(self.couleur)
            self.miriade_fenetres(couleur)

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
                x=self.x+ecart_barres+largeur_barre/2+demarcation+largeur_f/2
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
                formes.Rectangle(x,y,l,h).dessine().colorier(couleur_fenetres)
                X+=demarc_hor
            x= self.x+demarc_hor+(l/2),self.y-demarc_vert
            y-=h+demarc_vert
    

class toit1:
    def __init__(self,largeur,x,y,couleur):   #je ne sais pas encore à quoi correspondent les x et y demander a iban
        self.largeur = largeur
        self.x,self.y = x,y
        self.couleur = couleur
        choix_h = [self.largeur/4,self.largeur/3,self.largeur/6,self.largeur/2]
        self.hauteur = random.choice(choix_h)

    def dessine(self):
            formes.trait(self.x,self.y,self.x + self.largeur ,self.y)
            formes.trait(self.x+self.largeur, self.y, self.x + self.largeur/2, self.y + self.hauteur)
            formes.trait(self.x+self.largeur/2, self.y + self.hauteur, self.x, self.y)
            return self


    def colorie(self):
            couleur = random.choice(self.couleur)  #c'est la liste des couleurs de toits, on en choisit un 
            turtle.fillcolor(couleur)
            turtle.begin_fill()
            toit1(self.x,self.y,self.largeur,self.hauteur/2)
            turtle.end_fill()

class toit2:
    def __init__(self,x,y,largeur,couleur):
        self.x,self.y = x,y
        self.largeur = largeur
        self.couleur = couleur
    def dessine(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.pendown()
            turtle.setheading(90)
            turtle.circle(-self.largeur/2, 180)
            turtle.setheading(0)
            return self
    def colorie(self):
        couleur = random.choice(self.couleur)
        turtle.fillcolor(couleur)
        turtle.begin_fill()

        toit2(self.x,self.y,self.largeur)
        turtle.end_fill()

class toit3:
    def __init__(self,x,y,hauteurbd,largeur,couleur):
        self.x,self.y = x,y
        self.hauteurbd = hauteurbd
        self.hauteur = hauteurbd/4 #valeur provisoire
        self.couleur = couleur
        self.largeur= largeur

    def dessine(self,hauteur):
        nombre_marches =  4
        largeur_marche = self.largeur / (nombre_marches * 2)
        hauteur_marche = hauteur / nombre_marches
        x,y = self.x,self.y
        #on monte a gauche
        for i in range(nombre_marches):

            formes.trait(x, y, x + largeur_marche, y)
            x += largeur_marche

            formes.trait(x, y, x, y + hauteur_marche)
            y += hauteur_marche
        #on descend a droite
        for i in range(nombre_marches):

            formes.trait(x, y, x, y - hauteur_marche)
            y -= hauteur_marche

            formes.trait(x, y, x + largeur_marche, y)
            x += largeur_marche
        return self
    
    def colorie(self):
        couleur = random.choice(self.couleur)
        turtle.fillcolor(couleur)
        turtle.begin_fill()

        self.dessine(self.hauteur/2)

        turtle.end_fill()

