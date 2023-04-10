
class Championnat():
    """
    Classe définissant le championnat
    """
    def __init__(self, nom):
        self.nom = nom
        self.clubs = []

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, liste):
        """
        Méthode permettant le remplissage du championnat avec les clubs participant.

        liste : liste des clubs participants
        """
        for c in liste:
            self.clubs.append(c)