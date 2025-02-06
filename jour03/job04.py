class Joueur:
    def __init__(self, nom, numero, position, but, passe, jaune, rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombre_but = but
        self.passe_decisif = passe
        self.carton_jaune = jaune
        self.carton_rouge = rouge
        self.description = [self.nom, self.numero, self.position, self.nombre_but, self.passe_decisif, self.carton_jaune, self.carton_rouge]

    def marquerUnBut(self):
        self.nombre_but += 1
        return self.nombre_but

    def effectuerUnePasseDecisive(self):
        self.passe_decisif += 1
        return self.effectuerUnePasseDecisive

    def recevoirUnCartonJaune(self):
        self.carton_jaune += 1
        return self.recevoirUnCartonJaune

    def recevoirUnCartonRouge(self):
        self.carton_rouge += 1
        return self.carton_rouge

    def afficherStatistique(self):
        print(self.nom)
        print(self.numero)
        print(self.position)
        print(self.nombre_but)
        print(self.passe_decisif)
        print(self.carton_jaune)
        print(self.carton_rouge)

class Equipe:
    def __init__(self, nom):
        self.listeJoueur =[]
        self.nomEquipe = nom

    def ajouterJoueur(self, joueur):
        self.listeJoueur.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for i in self.listeJoueur:
            print(i)

    def mettreAJourStatistiquesJoueur(self):
        for i in self.listeJoueur:
            print(i)
        val = int(input("Quelle joueur voulez vous mettre a jour ses infos ? (min 1): "))
        if val <= 0 or val >len(self.listeJoueur):
            print("valeur impossible")
        else :
            val2 = int(input("But ? Passe décisive ? Carton jaune ? Rouge ?"))
            if val2 != 1 and val2 != 2 and val2 != 3 and val2 != 4:
                print("valeur impossible")
            else:
                if val2 == 1:
                    self.listeJoueur[val - 1][3] += 1
                elif val2 == 2:
                    self.listeJoueur[val - 1][4] += 1
                elif val2 == 3:
                    self.listeJoueur[val - 1][5] += 1
                elif val2 == 4:
                    self.listeJoueur[val - 1][6] += 1 

equipe1 = Equipe("Equipe1")

Jean = Joueur("Jean", 12, "Gardien", 0, 0, 0, 0)

Billy = Joueur("Billy", 6, "Attaquant", 11, 4, 1, 0)

equipe1.ajouterJoueur(Jean.description)
equipe1.ajouterJoueur(Billy.description)

equipe1.mettreAJourStatistiquesJoueur()
equipe1.afficherStatistiquesJoueurs()