class Club():
    """
    Classe gérant les informations relatives au club.
    """
    def __init__(self, nom, entraineur):
        self.nom = nom
        self.entraineur = entraineur
        self.joueurs = []
        self.score = 0
        self.note = 0

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, liste):
        for j in liste:
            self.joueurs.append(j)

    def liste_joueurs(self):
        """
        Méthode permettant l'affichage de la composition du club.
        """
        print(f"Le club {self.nom} dispose des joueurs suivants :")
        for j in self.joueurs:
            print(j)
        print(f"L'entraineur est {self.entraineur}")

    def note_club(self):
        cpt = 0
        self.note = 0
        if len(self.joueurs) != 0:
            for j in self.joueurs:
                self.note += j.note
                cpt += 1
            print(f"La note du club {self.nom} est : {self.note/cpt:.1f}")
        else:
            print(f"Il n'y a aucun joueur dans le club {self.nom}")

    def victoire(self):
        self.score += 2

    def nul(self):
        self.score += 1

    def affichage_score(self):
        print(f"{self.nom} à un score de {self.score}")