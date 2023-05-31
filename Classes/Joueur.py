import random as rd


class Joueur():
    """
    Classe renseignant toutes les informations propres à un joueur
    """
    def __init__(self, prenom, nom, note, club):
        self.prenom = prenom
        self.nom = nom
        self.note_originale = note
        self.note = note  # Note modifiée après blessure
        self.club = club
        self.etat = 0  # Etat physique dépendant d'une blessure (évolue entre 0 et 3)
        self.carton = 0  # self.carton = 1 ou 2 si le joueur a respectivement un carton jaune ou rouge
        self.cpt_carton = 0  # Nombre de journées depuis l'application du dernier carton


    def blessure(self, f):
        """
        Méthode simulant la blessure d'un joueur.

        f : fichier dans lequel on enregistre les données.
        """
        if self.etat == 0:  # Si le joueur n'est pas encore blessé
            # On détermine le degré de sa blessure.
            lb = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
            rd.shuffle(lb)
            degre_blessure = lb[0]
        elif self.etat == 1:  # Si le joueur a déjà une blessure légère
            # On détermine le degré de sa nouvelle blessure.
            lb = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
            rd.shuffle(lb)
            degre_blessure = lb[0]
        elif self.etat >= 2:  # Si le joueur a une blessure importante
            # Il obtient donc une blessure de niveau 3, la plus grave.
            degre_blessure = 3
        # Mise à jour de l'état du joueur.
        self.etat = degre_blessure
        # En cas de blessure, la note du joueur est réduite de 10, 20 ou 30% de la note originale.
        self.note = (1 - (self.etat / 10)) * self.note_originale
        print(f"{self.nom} s'est blessé (degré de la blessure : {degre_blessure})\n"
              f". Note originale : {self.note_originale} /// Note : {self.note : .2}")
        f.write(f"<font color='#127EC6'><b>{self.prenom[0]}.{self.nom}</b> ({self.club}) s'est blessé "
                f"(degré de la blessure : {degre_blessure})</font><br>")

    def faute(self, f):
        """
        Méthode simulant une faute.

        f : fichier dans lequel on enregistre les données.
        """
        # On détermine si le joueur reçoit un carton jaune (1) ou un carton rouge (2).
        lf = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        rd.shuffle(lf)
        if self.carton == 0:  # Si le joueur n'a pas encore de carton
            self.carton = lf[0]
            if lf[0] == 1:
                print(f"{self.nom} reçoit un carton jaune")
                f.write(f"<font color='#FFC600'><b>{self.prenom[0]}.{self.nom} ({self.club})</b> "
                        f"reçoit un carton jaune</font><br>")
            else:
                print(f"{self.nom} reçoit un carton rouge")
                f.write(f"<font color='#FF0000'><b>{self.prenom[0]}.{self.nom} ({self.club})</b> "
                        f"reçoit un carton rouge</font><br>")
        elif self.carton == 1:  # Si le joueur a déjà un carton jaune
            # Le joueur reçoit nécessairement un carton rouge.
            self.carton = 2
            self.cpt_carton = 0  # On remet le compteur de matchs avec cartons à zéro
            if lf[0] == 1:  # S'il a obtenu le carton rouge à cause d'un second carton jaune
                print(f"{self.nom} reçoit un second carton jaune et a donc un carton rouge")
                f.write(f"<font color='#FF0000'><b>{self.prenom[0]}.{self.nom} ({self.club})</b> "
                        f"reçoit un second carton jaune et a donc un carton rouge</font><br>")
            else:  # Sinon, il a directement obtenu un carton rouge
                print(f"{self.nom} reçoit un carton rouge")
                f.write(f"<font color='#FF0000'><b>{self.prenom[0]}.{self.nom} ({self.club})</b> "
                        f"reçoit un carton rouge</font><br>")

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


    def reinitialisation_cartons(self):
        """
        Méthode réinitialisant les cartons obtenus par le joueur lors d'un match
        """
        # Remise à zéro des cartons jaunes à la fin de la journée.
        if self.carton == 1:
            self.carton = 0
            self.cpt_carton = 0  # On remet le compteur à zéro
            print(f"{self.nom} n'a plus son carton jaune.")
        # Remise à zéro des cartons rouges s'ils ont été appliqués depuis 5 matchs.
        elif self.carton == 2:
            if self.cpt_carton == 5:
                self.carton = 0
                self.cpt_carton = 0  # On remet le compteur à zéro
                print(f"{self.nom} n'a plus son carton rouge.")
            else:
                self.cpt_carton += 1

class Gardien(Joueur):
    """
    Classe permettant la création d'un gardien.
    """
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Gardien"
        self.nb_arrets = 0
        self.tentatives_arrets = 0
        self.efficacite = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale})"

    def arret(self):
        self.nb_arrets += 1

    def calcul_efficacite(self):
        if self.tentatives_arrets != 0:
            self.efficacite = self.nb_arrets / self.tentatives_arrets
        else:
            self.efficacite = 0


class Attaquant(Joueur):
    """
    Classe permettant la création d'un attaquant.
    """
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Attaquant"
        self.nb_buts = 0
        self.nb_tirs = 0
        self.efficacite = 0

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale})"

    def but(self):
        self.nb_buts += 1

    def calcul_efficacite(self):
        if self.nb_tirs != 0:
            self.efficacite = self.nb_buts / self.nb_tirs
        else:
            self.efficacite = 0


class Milieu(Joueur):
    """
    Classe permettant la création d'un milieu.
    """
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Milieu"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale})"


class Defenseur(Joueur):
    """
    Classe permettant la création d'un défenseur.
    """
    def __init__(self, prenom, nom, note, club):
        super().__init__(prenom, nom, note, club)
        self.poste = "Défenseur"

    def __str__(self):
        return f"{self.prenom[0]}.{self.nom}, {self.poste} ({self.note_originale})"

