class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        print("L'age de l'animal :", self.age)
        self.age += 1
        print("L'année est passé, il a maintenant :", self.age)

    def nommer(self):
        self.prenom = input("Rentré le nom de l'animal : ")
        print("L'animal se nomme", self.prenom, "ans")

chien = Animal()
chien.nommer()
chien.vieillir()
chien.vieillir()