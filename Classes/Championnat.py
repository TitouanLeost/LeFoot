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
        # Liste des couleurs associées aux clubs.
        self.liste_couleur = ['#FF5733', '#F89107', '#88D30C', '#0DE915', '#0BC9DA', '#850BDA', '#BF0CCA', '#EE0899']
        self.donnees_analyse = [[0, 0], [0, 0], [0, 0], [0, 0], []]  # Liste contenant les données des analyses

    def __str__(self):
        return f"{self.nom}"

    def remplissage(self, copie):
        """
        Méthode permettant le remplissage du championnat avec les clubs participant.

        copie : paramètre permettant de spécifier si le championnat doit être relancé avec les mêmes équipes ou non.
        """
        if copie == True:
            for i, c in enumerate(self.liste_clubs):
                c.remplissage_copie_bdd()
                c.couleur = self.liste_couleur[i]
                self.clubs.append(c)
        else:
            for i, c in enumerate(self.liste_clubs):
                c.remplissage_bdd()
                c.couleur = self.liste_couleur[i]
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
            self.score_journee()  # Création de la liste des scores
            self.tableau_score_log(i)  # Enregistrement du tableau des scores
            self.journees_liste.append(j)
            print("=====================================================")
        self.tableau_score()  # Affichage du score final
        self.classement_buteurs()  # Enregistrement du classement des buteurs
        self.classement_gardiens()  # Enregistrement du classement des gardiens
        self.analyse()  # Analyse du championnat

    def tableau_score(self):
        """
        Fonction permettant d'afficher le tableau des scores en fin de championnat.
        """
        f = open("C:\WorkspacePython\LeFoot\Fichiers\\fichier des scores finaux.txt", 'wt') # titouan
        # f = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\fichier des scores finaux.txt", 'wt')
        c = self.liste_scores[0]
        # Affichage personnalisé pour le gagnant.
        print(f"{c} remporte {self.nom} avec {c.score} points et {c.nb_buts} buts marqués !")
        f.write(f"{c} remporte {self.nom} avec {c.score} points et {c.nb_buts} buts marqués !")
        # Affichage des scores des autres clubs dans l'ordre.
        for c in self.liste_scores[1::]:  # On parcourt la liste privée du gagnant
            print(f"{c} fini le championnat avec {c.score} points et {c.nb_buts} buts marqués.")
            f.write(f"{c} fini le championnat avec {c.score} points et {c.nb_buts} buts marqués.")

    def tableau_score_log(self, num):
        """
        Fonction permettant d'enregistrer le tableau des scores en fin de championnat.

        num : numéro de la journée.
        """
        # Enregistrement des données en colonnes pour pouvoir faire un affichage propre sur l'interface.
        # Titouan
        classement = open(f"C:\WorkspacePython\LeFoot\Fichiers\\classement clubs journée {num}.txt", 'wt')
        nom = open(f"C:\WorkspacePython\LeFoot\Fichiers\\nom clubs journée {num}.txt", 'wt')
        victoires = open(f"C:\WorkspacePython\LeFoot\Fichiers\\victoires clubs journée {num}.txt", 'wt')
        defaites = open(f"C:\WorkspacePython\LeFoot\Fichiers\\défaites clubs journée {num}.txt", 'wt')
        nuls = open(f"C:\WorkspacePython\LeFoot\Fichiers\\nuls clubs journée {num}.txt", 'wt')
        buts = open(f"C:\WorkspacePython\LeFoot\Fichiers\\buts clubs journée {num}.txt", 'wt')
        encaisses = open(f"C:\WorkspacePython\LeFoot\Fichiers\\encaissés clubs journée {num}.txt", 'wt')
        points = open(f"C:\WorkspacePython\LeFoot\Fichiers\\points clubs journée {num}.txt", 'wt')
        # Hadrien
        # classement = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\classement clubs journée {num}.txt", 'wt')
        # nom = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\nom clubs journée {num}.txt", 'wt')
        # victoires = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\victoires clubs journée {num}.txt", 'wt')
        # defaites = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\défaites clubs journée {num}.txt", 'wt')
        # nuls = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\nuls clubs journée {num}.txt", 'wt')
        # buts = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\buts clubs journée {num}.txt", 'wt')
        # encaisses = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\encaissés clubs journée {num}.txt", 'wt')
        # points = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\points clubs journée {num}.txt", 'wt')
        # Ecriture de la première ligne de chaques colonnes.
        classement.write("CLASSEMENT\n\n")
        nom.write("NOM\n\n")
        victoires.write("VICTOIRES\n\n")
        defaites.write("DEFAITES\n\n")
        nuls.write("NULS\n\n")
        buts.write("BUTS\n\n")
        encaisses.write("ENCAISSES\n\n")
        points.write("POINTS\n\n")
        # Remplissage des colonnes.
        for i, c in enumerate(self.liste_scores, start=1):
            classement.write(f"#{i}\n")
            nom.write(f"{c}\n")
            victoires.write(f"{c.nb_victoires}\n")
            defaites.write(f"{c.nb_defaites}\n")
            nuls.write(f"{c.nb_nuls}\n")
            buts.write(f"{c.nb_buts}\n")
            encaisses.write(f"{c.nb_buts_encaisses}\n")
            points.write(f"{c.score}\n")
        classement.close()
        nom.close()
        victoires.close()
        defaites.close()
        nuls.close()
        buts.close()
        encaisses.close()
        points.close()

    def score_journee(self):
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
        # Titouan
        classement = open("C:\WorkspacePython\LeFoot\Fichiers\\classement buteurs.txt", 'wt')
        nom = open("C:\WorkspacePython\LeFoot\Fichiers\\nom buteurs.txt", 'wt')
        club = open("C:\WorkspacePython\LeFoot\Fichiers\\club buteurs.txt", 'wt')
        buts = open("C:\WorkspacePython\LeFoot\Fichiers\\buts buteurs.txt", 'wt')
        # Hadrien
        # classement = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\classement buteurs.txt", 'wt')
        # nom = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\nom buteurs.txt", 'wt')
        # club = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\club buteurs.txt", 'wt')
        # buts = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\buts buteurs.txt", 'wt')
        # Ecriture de la première ligne de chaques colonnes.
        classement.write("CLASSEMENT \n\n")
        nom.write("NOM \n\n")
        club.write("CLUB \n\n")
        buts.write("BUTS \n\n")
        # Remplissage des colonnes.
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
        # Titouan
        classement = open("C:\WorkspacePython\LeFoot\Fichiers\\classement gardiens.txt", 'wt')
        nom = open("C:\WorkspacePython\LeFoot\Fichiers\\nom gardiens.txt", 'wt')
        club = open("C:\WorkspacePython\LeFoot\Fichiers\\club gardiens.txt", 'wt')
        buts = open("C:\WorkspacePython\LeFoot\Fichiers\\arrets gardiens.txt", 'wt')
        # Hadrien
        # classement = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\classement gardiens.txt", 'wt')
        # nom = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\nom gardiens.txt", 'wt')
        # club = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\club gardiens.txt", 'wt')
        # buts = open("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\arrets gardiens.txt", 'wt')
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

    def analyse(self):
        """
        Méthode réalisant quelques analyses sur le championnat.
        """
        for c in self.clubs:
            for j in c:
                # On garde le gardien le plus efficace.
                if j.poste == "Gardien":
                    j.calcul_efficacite()
                    if j.efficacite > self.donnees_analyse[0][1]:
                        self.donnees_analyse[0] = [j, j.efficacite]  # On enregistre le gardien le plus efficace
                # On garde l'attaquant le plus efficace.
                elif j.poste == "Attaquant":
                    j.calcul_efficacite()
                    if j.efficacite > self.donnees_analyse[1][1]:
                        self.donnees_analyse[1] = [j, j.efficacite]  # On enregistre l'attaquant le plus efficace
            # On enregistre le clubs ayant l'attaque la plus efficace.
            if c.attaques_reussies > self.donnees_analyse[2][1]:
                self.donnees_analyse[2] = [c, c.attaques_reussies]
            # On enregistre le clubs ayant la défense la plus efficace.
            if c.defenses_reussies > self.donnees_analyse[3][1]:
                self.donnees_analyse[3] = [c, c.defenses_reussies]
            # On enregistre le nombre de cartons obtenus chaques clubs.
            self.donnees_analyse[4].append(c.nb_cartons)
        print(self.donnees_analyse)  # Debug
