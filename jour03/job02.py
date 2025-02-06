class CompteBanquaire:
    def __init__(self, numero, nom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__solde = solde
        self.decouvert = False

    def afficher(self):
        print(self.__nom)
        print(self.__numero)

    def afficherSolde(self):
        print(self.__solde)

    def versement(self, montant = 0):
        versement = 0
        if montant == 0:
            versement = int(input("Quelle montant voulez vous versez ? : "))
        if versement <= 0 and montant <= 0:
            print("Valeur incorrect")
        else :
            if versement > 0:
                self.__solde += versement
            elif montant > 0:
                self.__solde += montant
            if self.__solde > 0:
                self.decouvert = False

    def retrait(self):
        retrait = int(input("Quelle montant voulez vous retirer ? : "))
        if retrait <= 0:
            print("Valeur incorrect")
        else :
            self.__solde -= retrait
            if self.__solde <= 0:
                self.decouvert = True
                CompteBanquaire.agios(self)

    def agios(self):
        self.__solde -= 10

    def virement(self, compte):
        montant = int(input("Quelle est le motant du virement ? : "))
        if montant <= 0:
            print("Valeur incorrect")
        else :
            self.__solde -= montant
            compte.versement(montant)
            if self.__solde <= 0:
                self.decouvert = True
                CompteBanquaire.agios(self)

Baptiste = CompteBanquaire(45234589652, "Baptiste", 1200)
Jean = CompteBanquaire(45233359252, "Jean", -40)
Baptiste.afficher()
Baptiste.afficherSolde()
Jean.afficher()
Jean.afficherSolde()

Baptiste.virement(Jean)
Baptiste.afficherSolde()
Jean.afficherSolde()