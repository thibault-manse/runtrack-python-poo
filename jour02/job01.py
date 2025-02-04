class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def get_Rectangle(self):
        rectangle = self.longueur, self.largeur
        return rectangle
    
    def modifierLargeur(self):
        self.largeur = int(input("Rentré une largeur : "))

    def modifierLongueur(self):
        self.longueur = int(input("Rentré une longueur : "))

rectangle = Rectangle(12, 5)
l, L = rectangle.get_Rectangle()
print("Longueur :", l)
print("Largeur :", L)
rectangle.modifierLongueur()
rectangle.modifierLargeur()
l, L = rectangle.get_Rectangle()
print("Longueur :", l)
print("Largeur :", L)