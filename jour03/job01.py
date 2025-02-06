class Ville:
    def __init__(self, nom, habitant):
        self.__nom = nom
        self.__habitant = habitant

    def nombreHabitant(self):
        print("Nombre d'habitant de", self.__nom, ":", self.__habitant)

    def augmentationHabitant(self):
        self.__habitant += 1

Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.augmentationHabitant()

Paris.nombreHabitant()
Marseille.nombreHabitant()
John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloé", 18, Marseille)
John.ajouterPopulation()
Myrtille.ajouterPopulation()
Chloe.ajouterPopulation()
Paris.nombreHabitant()
Marseille.nombreHabitant()