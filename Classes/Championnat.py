import Journée
class Championnat():
    """
    Classe définissant le championnat
    """
    def __init__(self, nom):
        self.nom = nom
        self.clubs = []
        #self.journees = []

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, liste):
        """
        Méthode permettant le remplissage du championnat avec les clubs participant.

        liste : liste des clubs participants
        """
        for c in liste:
            self.clubs.append(c)

    # def nb_journees(self):
    #     for i in range(1, len(self.clubs)-1):
    #         j = Journée.Journee(i, self.nom)
    #         self.journees.append(j)