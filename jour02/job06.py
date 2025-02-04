class Commande:
    def __init__(self):
        self.__numero = 0
        self.__status_commande = "En cours"
        self.__total = 0
        self.__liste = []

    def ajouterCommande(self):
        commande = []
        commande.append(input("Quelle est la commande ? : ").lower())
        commande.append(self.__status_commande)
        commande.append(input("Quelle est le prix de la commande ? : ").lower())
        self.__numero += 1
        commande.append(self.__numero)
        self.__liste.append(commande)

    def annulerCommande(self):
        annuler = input("Quelle est la commande à annuler ? :").lower()
        for i in self.__liste:
            if annuler == self.__liste[i][0]:
                self.__liste[i][1] = "Annuler"
                break
        if i == len(self.__liste):
            print("Cette commande existe pas...")

    def commandeFini(self):
        terminer = input("Quelle est la commande à annuler ? :").lower()
        for i in self.__liste:
            if terminer == self.__liste[i][0]:
                self.__liste[i][1] = "Terminée"
                break
        if i == len(self.__liste):
            print("Cette commande existe pas...")

    def __payer(self):
        for i in self.__liste:
            self.__total = self.__total + self.__liste[i][2] * 1.20
        print("prix total de la commande : ", self.__total, "€")
    
    def afficherCommande(self):
        print(self.__liste)
        Commande.__payer(self)

resto = Commande()
resto.ajouterCommande()
resto.ajouterCommande()
resto.afficherCommande()