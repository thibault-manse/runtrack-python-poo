class Voiture():
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__réservoir = 50

    def modifierVoiture(self):
        self.__marque = input("Rentré la marque de la voiture : ")
        self.__modele = input("Rentré le modele de la voiture : ")
        try:
            self.__annee = int(input("Rentré l'année de la voiture : "))
        except ValueError:
            print("Valeur incorrect")

        try:
            self.__kilometrage = int(input("Rentré le kilométrage de la voiture : "))
        except ValueError:
            print("Valeur incorrect")

    def get_Voiture(self):
        voiture = self.__marque, self.__modele, self.__annee, self.__kilometrage
        return voiture
    
    def demarrer(self):
        if Voiture.__verifier_plein(self) > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__réservoir