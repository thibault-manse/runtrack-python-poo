class Cercle:
    def __init__(self):
        self.rayon = 0

    def changerRayon(self):
        self.rayon = int(input("Rentré un rayon pour le cercle : "))

    def circonference(self):
        result = (2*self.rayon) * 3.14
        print("Circonférence du cercle :", result)

    def air(self):
        result = 3.14 * (self.rayon ** 2)
        print("Air du cercle :", result)

    def diametre(self):
        result = self.rayon * 2
        print("Diamètre du cercle :", result)

    def afficherInfos(self):
        print("Rayon du cercle :", self.rayon)
        Cercle.diametre(self)
        Cercle.circonference(self)
        Cercle.air(self)

cercle = Cercle()
cercle.changerRayon()
cercle.afficherInfos()
cercle.changerRayon()
cercle.afficherInfos()