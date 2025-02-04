class Student:
    def __init__(self, nom, prenom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroEtudiant = numero
        self.__nombreCredit = 0
        self.__level = Student._student_eval(self)

    def add_credits(self):
        while True:
            try:
                ajout = int(input("Combien de crédits en plus ? : "))
            except ValueError:
                print("Rentré un nombre s'il vous plait")

            if ajout <= 0:
                print("Rentré un nombre positif supérieur à 0 s'il vous plait")
            else:
                self.__nombreCredit = self.__nombreCredit + ajout
                self.__level = Student._student_eval(self)
                break

    def get_credit(self):
        return self.__nombreCredit
    
    def _student_eval(self):
        if self.__nombreCredit >= 90:
            return "Excellent"
        elif self.__nombreCredit >= 80 and self.__nombreCredit < 90:
            return "Très bien"
        elif self.__nombreCredit >= 70 and self.__nombreCredit < 80:
            return "Bien"
        elif self.__nombreCredit >= 60 and self.__nombreCredit < 70:
            return "Passable"
        elif self.__nombreCredit < 60 :
            return "Insuffisant"
        
    def student_info(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("id =", self.__numeroEtudiant)
        print("Niveau =", self.__level)

Personne1 = Student( "Doe", "John", 145)
Personne1.add_credits()
Personne1.add_credits()
Personne1.add_credits()
print ("Le nombre de crédit de", Personne1.__prenom, Personne1.__nom, "est de", Personne1.get_credit())
Personne1.student_info()