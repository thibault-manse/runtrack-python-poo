class Personne:
    def __init__(self):
        self.prenom = ""
        self.nom = ""

    def SePresenter(self):
        self.prenom = input("Rentrez votre prénom : ")
        self.nom = input("Rentrez votre nom : ")
        nom_complet = f"{self.prenom} {self.nom}"
        return nom_complet
    
personne = Personne()
nom_complet = personne.SePresenter()
print("Je suis", nom_complet)