import Journée


class Championnat():
    """
    Classe définissant le championnat
    """
    def __init__(self, nom, liste_clubs):
        self.nom = nom
        self.liste_clubs = liste_clubs
        self.clubs = []
        self.journees = 14
        self.journees_liste = []
        self.liste_scores = []

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, copie):
        """
        Méthode permettant le remplissage du championnat avec les clubs participant.

        copie : paramètre permettant de spécifier si le championnat doit être relancé avec les mêmes équipes ou non.
        """
        if copie == True:
            for c in self.liste_clubs:
                c.remplissage_copie_bdd()
                self.clubs.append(c)
        else:
            for c in self.liste_clubs:
                c.remplissage_bdd()
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
            self.journees_liste.append(j)
            print("=====================================================")
        self.score_final()  # Création de la liste des scores
        self.tableau_score()  # Affichage du score final
        self.classement_buteurs()  # Enregistrement du classement des buteurs
        self.classement_gardiens()  # Enregistrement du classement des gardiens

    def tableau_score(self):
        """
        Fonction permettant d'afficher le tableau des scores en fin de championnat et de l'enregistrer dans un fichier.
        """
        # Affichage personnalisé pour le gagnant.
        fichier_score = open("C:\WorkspacePython\LeFoot\Fichiers\\fichier des scores finaux.txt", 'wt')
        c = self.liste_scores[0]
        print(f"{c} remporte {self.nom} avec {c.score} points et {c.nb_buts} buts marqués !")
        fichier_score.write(f"{c} remporte {self.nom} avec {c.score} points et {c.nb_buts} buts marqués !\n")
        # Affichage des scores des autres clubs dans l'ordre.
        for c in self.liste_scores[1::]:  # On parcourt la liste privée du gagnant
            print(f"{c} fini le championnat avec {c.score} points et {c.nb_buts} buts marqués.")
            fichier_score.write(f"{c} fini le championnat avec {c.score} points et {c.nb_buts} buts marqués.\n")

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

    def classement_buteurs(self):
        """
        Fonction permettant de classer tous les buteurs du championnat par ordre décroissant de buts.
        Enregistre le classement dans un fichier texte.
        """
        buteurs = []
        for c in self.clubs:
            for j in c:
                if j.poste == "Attaquant":
                    buteurs.append(j)
        buteurs.sort(key=self.triage_buts, reverse=True)
        # Enregistrement des données en colonnes pour pouvoir faire un affichage propre sur l'interface.
        classement = open("C:\WorkspacePython\LeFoot\Fichiers\\classement buteurs.txt", 'wt')
        nom = open("C:\WorkspacePython\LeFoot\Fichiers\\nom buteurs.txt", 'wt')
        club = open("C:\WorkspacePython\LeFoot\Fichiers\\club buteurs.txt", 'wt')
        buts = open("C:\WorkspacePython\LeFoot\Fichiers\\buts buteurs.txt", 'wt')
        classement.write("CLASSEMENT \n\n")
        nom.write("NOM \n\n")
        club.write("CLUB \n\n")
        buts.write("BUTS \n\n")
        for i, j in enumerate(buteurs, start=1):
            classement.write(f"#{i}\n")
            nom.write(f"{j.nom}\n")
            club.write(f"{j.club}\n")
            buts.write(f"{j.nb_buts}\n")
        classement.close()
        nom.close()
        club.close()
        buts.close()

    def triage_buts(self, joueur):
        """
        Méthode permettant le triage des joueurs suivant leur nombre de buts.
        """
        return joueur.nb_buts

    def classement_gardiens(self):
        """
        Méthode permettant de classer tous les gardiens du championnat par ordre décroissant d'arrêts.
        Enregistre le classement dans un fichier texte.
        """
        gardiens = []
        for c in self.clubs:
            for j in c:
                if j.poste == "Gardien":
                    gardiens.append(j)
        gardiens.sort(key=self.triage_arrets, reverse=True)
        # Enregistrement des données en colonnes pour pouvoir faire un affichage propre sur l'interface.
        classement = open("C:\WorkspacePython\LeFoot\Fichiers\\classement gardiens.txt", 'wt')
        nom = open("C:\WorkspacePython\LeFoot\Fichiers\\nom gardiens.txt", 'wt')
        club = open("C:\WorkspacePython\LeFoot\Fichiers\\club gardiens.txt", 'wt')
        buts = open("C:\WorkspacePython\LeFoot\Fichiers\\arrets gardiens.txt", 'wt')
        classement.write("CLASSEMENT \n\n")
        nom.write("NOM \n\n")
        club.write("CLUB \n\n")
        buts.write("ARRETS \n\n")
        for i, j in enumerate(gardiens, start=1):
            classement.write(f"#{i}\n")
            nom.write(f"{j.nom}\n")
            club.write(f"{j.club}\n")
            buts.write(f"{j.nb_arrets}\n")
        classement.close()
        nom.close()
        club.close()
        buts.close()

    def triage_arrets(self, joueur):
        """
        Méthode permettant le triage des joueurs suivant leur nombre d'arrêts.
        """
        return joueur.nb_arrets

    def creation_fiche_clubs(self, final=True):
        """
        Méthode permettant de créer toutes les fiches des clubs participant au championnat.

        final : paramètre spécifiant si la fiche est créée à la fin du championnat ou non.
        """
        for c in self.clubs:
            c.fiche_club(final)