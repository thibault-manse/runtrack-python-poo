class Livre():
    def __init__(self, titre, auteur, page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page

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

livre = Livre("Le petit prince", "Antoine de Saint-Exupéry", 150)
titre, auteur, page = livre.get_livre()
print(titre)
print(auteur)
print(page)
livre.modifier_livre()
titre, auteur, page = livre.get_livre()
print(titre)
print(auteur)
print(page)