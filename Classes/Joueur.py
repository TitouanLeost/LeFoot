

class Joueur():
    """
    Classe renseignant toutes les informations propres à un joueur
    """
    def __init__(self, prenom, nom, note, club):
        self.prenom = prenom
        self.nom = nom
        self.note = note
        self.club = club


class Gardien(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Gardien"
        self.nb_arrets = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note}) | {self.club}"

    def arret(self):
        self.nb_arrets += 1


class Attaquant(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Attaquant"
        self.nb_buts = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note}) | {self.club}"

    def but(self):
        self.nb_buts += 1


class Milieu(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Milieu"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note}) | {self.club}"


class Defenseur(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Défenseur"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note}) | {self.club}"

