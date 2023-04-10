
class Journee():
    """
    Classe contenant les informations d'une journée de match.
    """
    def __init__(self, num, championnat):
        self.num = num
        self.matchs = []
        self.clubs = championnat.clubs

    def __str__(self):
        return f"Journée n°{self.num}"

    def match(self):
        c1 = self.clubs[0]
        c2 = self.clubs[1]
        c1.note_club()
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

    def score_journee(self):
        for c in self.clubs:
            print(f"{c} termine la journée avec un score de {c.score}")