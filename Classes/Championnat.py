import Journée
import numpy as np
class Championnat():
    """
    Classe définissant le championnat
    """
    def __init__(self, nom):
        self.nom = nom
        self.clubs = []
        self.journees = 7

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, liste):
        """
        Méthode permettant le remplissage du championnat avec les clubs participant.

        liste : liste des clubs participants
        """
        for c in liste:
            self.clubs.append(c)

    def simuler(self):
        nb_j = self.journees
        for i in range(1, nb_j+1):
            j = Journée.Journee(i, self)
            j.deroulement()
            print("----------------------------------------")
