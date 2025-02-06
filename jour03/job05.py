import random

class Personnage:
    def __init__(self, nom, bot, niveau = 1):
        self.nom = nom
        self.vie = (125 * niveau) / 1.25
        self.ia = bot
        self.mana = 90 + (niveau * 10)
        self.objetPV = 1
        self.objetMP = 1

    def attaque(self):
        if not self.ia:
            choix = int(input("1-Attaqué 2-Defense 3-Spécial 4-Objet : "))
        elif self.ia:
            choix = random.randint(1, 3)

        critique = random.randint(1, 8)
        if choix == 1:
            if critique == 8:
                print(self.nom, "lance une attaque très efficace ! 20 Dammage")
                self.mana += 10
                return 20
            else :
                print(self.nom, "lance une attaque ! 10 Dammage")
                self.mana += 5
                return 10
        elif choix == 2:
            if critique == 8:
                print(self.nom, "préfère ce proteger... Ca defense semble impététrable. +25 PV")
                self.vie += 25
                return 0
            else:
                print(self.nom, "préfère ce proteger. +10 PV")
                self.vie += 10
                return 0
        elif choix == 3:
            if critique == 8:
                if self.mana >= 25:
                    print(self.nom, "lance une attaque spécial qui semble dévastatrice !! 40 Dammage")
                    self.mana -= 25
                    return 40
                else :
                    print(self.nom, "n'a pas assez de mana... Une attaque simple est donc lancer. 10 Dammage")
                    self.mana += 2
                    return 10
            else:
                if self.mana >= 25:
                    print(self.nom, "lance une attaque spécial ! 25 Dammage")
                    self.mana -= 25
                    return 25
                else :
                    print(self.nom, "n'a pas assez de mana... Une attaque simple est donc lancer. 10 Dammage")
                    self.mana += 2
                    return 10
        elif choix == 4:
            potion = int(input("1- PV 2-MP"))
            if potion == 1:
                if self.objetPV <= 0:
                    print("Vous avez plus der potion...")
                    Personnage.attaque(self)
                else :
                    print("Vous utilisez une potion. +30PV")
                    self.objetPV -= 1
                    self.vie += 30
                    Personnage.attaque(self)
            elif potion == 2:
                if self.objetMP <= 0:
                    print("Vous avez plus d'elixir...")
                    Personnage.attaque(self)
                else:
                    print("Vous utilisez une elixir. +40MP")
                    self.objetMP -= 1
                    self.mana += 40
                    Personnage.attaque(self)
            return 0

class Jeu:
    def __init__(self):
        pass

    def choisirNiveau(self):
        niveau = int(input("Difficulté : 1-Normal 2-Difficile 3-Ange Maudit : "))
        return niveau
    
    def lancerJeu(self):
        difficulté = 1
        joueur1 = Personnage("Cloud", False, difficulté)
        difficulté = Jeu.choisirNiveau(self)
        joueur1.objetPV *= difficulté
        joueur1.objetMP *= difficulté - 1
        joueur2 = Personnage("Sephiroth", True, difficulté)
        while joueur1.vie > 0 or joueur2.vie > 0:
            attaque = 0
            print(joueur1.nom, joueur1.vie, "PV", joueur1.mana, "MP", joueur1.objetPV, "potion(s)", joueur1.objetMP, "Elixir(s)")
            print(joueur2.nom, joueur2.vie, "PV", joueur2.mana, "MP")
            attaque = joueur1.attaque()
            joueur2.vie -= attaque
            if joueur2.vie <= 0:
                print("Vous avez gagné !")
                break
            attaque = joueur2.attaque()
            joueur1.vie -= attaque
            if joueur1.vie <= 0:
                print("Vous avez perdu...")
            print(" ")

combat = Jeu()
combat.lancerJeu()