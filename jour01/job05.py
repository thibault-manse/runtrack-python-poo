class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def afficherLesPoint(self):
        print(self.x, self.y)

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self):
        self.x = int(input("Valeur de x : "))
    
    def changerY(self):
        self.y = int(input("Valeur de y : "))

geo = Point()

geo.afficherLesPoint()
geo.changerX()
geo.changerY()
geo.afficherX()
geo.afficherY()
geo.afficherLesPoint()