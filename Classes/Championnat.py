import Journée
import numpy as np
class Championnat():
    """
    Classe définissant le championnat
    """
    def __init__(self, nom):
        self.nom = nom
        self.clubs = []
        self.journees = 14
        self.liste_scores = []

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
        """
        Fonction permettant de simuler le déroulement complet du championnat.
        """
        nb_j = self.journees
        for i in range(1, nb_j+1):
            # Simulation des journées
            j = Journée.Journee(i, self)
            j.deroulement()
            print("=====================================================")
        self.score_final()  # Création de la liste des scores
        self.tableau_score()  # Affichage du score final


    def tableau_score(self):
        """
        Fonction permettant d'afficher le tableau des scores en fin de championnat.
        """
        # Affichage personnalisé pour le gagnant
        c = self.liste_scores[0]
        print(f"{c} remporte {self.nom} avec {c.score} points et {c.nb_buts} buts marqués !")
        for c in self.liste_scores[1::]:  # On parcourt la liste privée du gagnant
            print(f"{c} fini le championnat avec {c.score} points et {c.nb_buts} buts marqués.")


    def score_final(self):
        """
        Fonction permettant de créer la liste des clubs rangée par ordre décroissant de score puis de buts en cas
        d'égalité des scores.
        """
        self.liste_scores = []  # On s'assure que la liste est bien vide
        for c in self.clubs:
            self.liste_scores.append(c)
        self.liste_scores.sort(key=self.triage, reverse=True)  # Appelle à la fonction triage pour gérer le tri


    def triage(self, club):
        """
        Fonction permettant le triage des clubs en fonction de leur score puis de leur nombre de buts.
        """
        return club.score, club.nb_buts