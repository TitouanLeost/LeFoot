import random as rd

class Joueur():
    """
    Classe renseignant toutes les informations propres à un joueur
    """
    def __init__(self, prenom, nom, note, club):
        self.prenom = prenom
        self.nom = nom
        self.note_originale = note
        self.note = note
        self.club = club
        self.etat = 0
        self.carton = 0


    def blessure(self):
        """
        Méthode simulant la blessure d'un joueur
        """
        if self.etat == 0:  # Si le joueur n'est pas encore blessé
            # On détermine le degré de sa blessure
            lb = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
            rd.shuffle(lb)
            degre_blessure = lb[0]
        elif self.etat == 1:  # Si le joueur a déjà une blessure légère
            # On détermine le degré de sa nouvelle blessure
            lb = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
            rd.shuffle(lb)
            degre_blessure = lb[0]
        elif self.etat >= 2:  # Si le joueur a une blessure importante
            # On détermine le degré de sa blessure
            degre_blessure = 3
        # Maj de l'état du joueur.
        self.etat = degre_blessure
        # En cas de blessure, la note du joueur est réduite de 10, 20 ou 30% de la note originale.
        self.note = (1 - (self.etat / 10)) * self.note_originale
        print(f"{self.nom} s'est blessé (degré de la blessure : {degre_blessure})\n"
              f". Note originale : {self.note_originale} /// Note : {self.note}")

    def faute(self):
        """
        Méthode simulant une faute
        """
        if self.carton == 0:  # Si le joueur n'a pas encore de carton
            # On détermine si le joueur reçoit un carton jaune (1) ou un carton rouge (2).
            lf = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
            rd.shuffle(lf)
            self.carton = lf[0]
        elif self.carton == 1:  # Si le joueur a déjà un carton jaune
            # Le joueur reçoit nécessairement un carton rouge.
            self.carton = 2
        if self.carton == 1:
            print(f"{self.nom} reçoit un carton jaune.")
        elif self.carton == 2:
            print(f"{self.nom} reçoit un carton rouge.")

    def recuperation(self):
        """
        Méthode simulant la récupération d'un joueur
        """
        proba_recup = rd.random()
        # Le joueur a 40% de chance de se remettre d'un niveau de blessure.
        if proba_recup > 0.6:
            self.etat = max(0, self.etat - 1)
            # On remet à jour la note du joueur si son état s'améliore.
            self.note = (1 - (self.etat / 10)) * self.note_originale
            print(f"{self.nom} a récupéré de sa blessure (etat : {self.etat} /// note : {self.note})")


class Gardien(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Gardien"
        self.nb_arrets = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale}) | {self.club}"

    def arret(self):
        self.nb_arrets += 1


class Attaquant(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Attaquant"
        self.nb_buts = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale}) | {self.club}"

    def but(self):
        self.nb_buts += 1


class Milieu(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Milieu"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale}) | {self.club}"


class Defenseur(Joueur):
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Défenseur"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale}) | {self.club}"

