class Joueur():
    """
    Classe renseignant toutes les informations propres à un joueur
    """
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note



class Gardien(Joueur):

    def __init__(self, nom, note):
        super().__init__(nom, note)
        self.poste = "Gardien"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note})"



class Attaquant(Joueur):

    def __init__(self, nom, note):
        super().__init__(nom, note)
        self.poste = "Attaquant"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note})"



class Milieu(Joueur):

    def __init__(self, nom, note):
        super().__init__(nom, note)
        self.poste = "Milieu"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note})"



class Defenseur(Joueur):

    def __init__(self, nom, note):
        super().__init__(nom, note)
        self.poste = "Defenseur"

    def __str__(self):
        return f"{self.nom}, {self.poste} ({self.note})"



J1 = Attaquant("Bob", 95)
J2 = Gardien("Jean Claude", 20)
J3 = Milieu("Micheline", 32)
print(J1)
print(J2)
print(J3)
print(J1.note)
print(J3.poste)