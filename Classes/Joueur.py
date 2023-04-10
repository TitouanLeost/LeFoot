

class Joueur():
    """
    Classe renseignant toutes les informations propres à un joueur
    """
    def __init__(self, nom, note, club):
        self.nom = nom
        self.note = note
        self.club = club


class Gardien(Joueur):
    def __init__(self, nom, note, club):
        super().__init__(nom, note, club)
        self.poste = "Gardien"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note}) | {self.club}"


class Attaquant(Joueur):
    def __init__(self, nom, note, club):
        super().__init__(nom, note, club)
        self.poste = "Attaquant"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note}) | {self.club}"


class Milieu(Joueur):
    def __init__(self, nom, note, club):
        super().__init__(nom, note, club)
        self.poste = "Milieu"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note}) | {self.club}"


class Defenseur(Joueur):
    def __init__(self, nom, note, club):
        super().__init__(nom, note, club)
        self.poste = "Defenseur"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note}) | {self.club}"

