class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.status = "A faire"
        self.tache = [self.titre, self.description, self.status]


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self):
        for i in self.taches:
            print(i)
        val = int(input("Rentré le numero de la tache que vous vous supprimer (min 1): "))
        if val > len(self.taches) or val <= 0:
            print("Valeur impossible")
        else:
            del self.taches[val - 1]

    def marquerCommeFinie(self):
        for i in self.taches:
            print(i)
        val = int(input("Rentré le numero de la tache que vous avez terminer (min 1): "))
        if val > len(self.taches) or val <= 0:
            print("Valeur impossible")
        else:
            self.taches[val - 1][2] = "Terminer"

    def filtrerListe(self):
        valeur = int(input("Rentré sois 1 pour afficher les tache en cours ou 2 pour afficher les taches terminer : "))
        if valeur != 1 and valeur != 2:
            print("valeur impossible")
        else:
            if valeur == 1:
                for i in self.taches:
                    for j in i:
                        if j == "A faire":
                            print(i)

            elif valeur == 2:
                for i in self.taches:
                    for j in i:
                        if j == "Terminer":
                            print(i)

    def afficherListe(self):
        for i in self.taches:
            print(i)


laTache = Tache("Test", "ceci est un test")
liste = ListeDeTaches()

liste.ajouterTache(laTache.tache)
laTache = Tache("Test2", "ceci est un 2eme test")
liste.ajouterTache(laTache.tache)
laTache = Tache("Test3", "ceci est un 3eme test")
liste.ajouterTache(laTache.tache)
liste.marquerCommeFinie()
liste.filtrerListe()