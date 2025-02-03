class Produit:
    def __init__(self):
        self.nom = ""
        self.prixHT = 0
        self.TVA = 1.20

    def changerNom(self):
        self.nom = input("Rentrez le nom du produit : ")
        return self.nom

    def changerPrix(self):
        self.prixHT = int(input("Rentrez le prix du produit : "))
        return self.prixHT

    def CalculerPrixTTC(self):
        result = self.prixHT * self.TVA
        return result
    
    def afficher(self):
        nom = Produit.changerNom(self)
        prix = Produit.changerPrix(self)
        nouveau_prix = Produit.CalculerPrixTTC(self)
        info_produit = nom, prix, nouveau_prix
        return info_produit

produit = Produit()
nom, prix, tva = produit.afficher()
print(nom)
print(prix)
print(tva)

nom, prix, tva = produit.afficher()
print(nom)
print(prix)
print(tva)