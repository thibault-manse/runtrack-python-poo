class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        print("Vous partez à gauche")
        self.x -= 1
    
    def droite(self):
        print("Vous partez à droite")
        self.x += 1

    def bas(self):
        print("Vous partez en bas")
        self.y += 1

    def haut(self):
        print("Vous partez en haut")
        self.y -= 1

    def position(self):
        coordonner = f"{self.x} {self.y}"
        return coordonner
    
Benjamin = Personnage()
Benjamin.droite()
Benjamin.droite()
Benjamin.droite()
Benjamin.haut()
Benjamin.haut()
Benjamin.gauche()
Benjamin.bas()
Benjamin.droite()
print(Benjamin.position())