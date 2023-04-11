import numpy as np

class Journee():
    """
    Classe contenant les informations d'une journée de match.
    """
    def __init__(self, num, championnat):
        self.num = num
        self.matchs = []
        self.clubs_complet = championnat.clubs.copy()  # liste contenant tous les clubs participant au championnat
        self.clubs = championnat.clubs.copy()  # Liste contenant les clubs n'ayant pas encore joué sur la journée

    def __str__(self):
        return f"Journée n°{self.num}"

    def match(self):
        """
        Fonction permettant le déroulement d'un match
        """
        c1 = self.clubs.pop()
        match_realise = False
        i = 0
        while match_realise == False:
            c2 = self.clubs[i]
            if c2 not in c1.match_realise:  # On vérifie que c1 et c2 ne se sont pas encore rencontrés
                del self.clubs[i]
                c1.ajout_match_realise(c2)
                c2.ajout_match_realise(c1)
                match_realise = True
                c1.note_club()  # On affiche les notes des clubs juste pour vérifier
                c2.note_club()
                if c1.note > c2.note:
                    print(f"{c1} remporte le match contre {c2} !")
                    c1.victoire()
                elif c2.note > c1.note:
                    print(f"{c2} remporte le match contre {c1} !")
                    c2.victoire()
                else:
                    print(f"{c1} et {c2} font un match nul")
                    c1.nul()
                    c2.nul()
            else:
                i += 1

    def score_journee(self):
        for c in self.clubs_complet:
            print(f"{c} termine la journée {self.num} avec un score de {c.score}")

    def deroulement(self):
        """
        Fonction simulant le déroulement d'une journée
        """
        while len(self.clubs) > 0:
            self.match()
        self.score_journee()