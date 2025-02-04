class Livre():
    def __init__(self, titre, auteur, page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page
        self.__disponible = True
        self.bibliothèque = [[self.__titre, self.__auteur, self.__page]]

    def get_livre(self):
        livre = self.__titre, self.__auteur, self.__page
        return livre
    
    def modifier_livre(self):
        self.__titre = input("Rentré un nouveau titre : ")
        self.__auteur = input("Rentré un nouvel auteur : ")
        while True:
            try :
                self.__page = int(input("Rentré un nouveau titre : "))
            except ValueError:
                print("Rentré un nombre entier pour le nombre de page")

            if self.__page <= 0:
                print("rentré un nombre de page correct")
            else : 
                break

    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if Livre.verification(self):
            self.__disponible = False
            return True
        else:
            return False
    
    def rendre(self):
        if not Livre.verification(self):
            self.__disponible = True
            return True
        else:
            return False