import sqlite3
import random as rd
from Joueur import *

class Club(list):
    """
    Classe gérant les informations relatives au club et contenant la liste des joueurs.
    """
    def __init__(self, nom, entraineur):
        self.nom = nom
        self.entraineur = entraineur
        self.couleur = '#000000'  # Couleur du club sur l'interface
        self.equipe = []  # Equipe active du club (dont sont retirés les joueurs expulsés à la suite d'un carton rouge)
        self.score = 0  # Nombre de points marqués par le club lors du championnat
        self.liste_score = []  # Liste des points marqués au total par journées
        self.nb_buts = 0
        self.nb_buts_encaisses = 0
        self.nb_victoires = 0
        self.nb_defaites = 0
        self.nb_nuls = 0
        self.nb_cartons = 0
        self.attaques_reussies = 0  # Attaques ayant percées la défense adverse
        self.defenses_reussies = 0  # Attaques adverses ayant été repoussées par la défense du club
        self.note_club = 0  # Note globale du club
        self.note_equipe = 0  # Note de l'équipe active
        self.match_realise_dom = []
        self.match_realise_ext = []


    def __str__(self):
        return f"{self.nom}"


    def remplissage_bdd(self):
        """
        Méthode permettant le remplissage des effectifs du club à partir de la BDD reserve_joueurs. Ces effectifs
        sont également sauvegardés dans une autre BDD afin de pouvoir les remettre dans le club au prochain
        championnat.
        """
        # Mise en place de la connexion avec la database.
        con = sqlite3.connect("C:\WorkspacePython\LeFoot\BDD\BDD_joueurs.db") # titouan
        # con = sqlite3.connect("C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\BDD_joueurs.db")
        # Mise en place de la connexion avec la database de sauvegarde.
        con2 = sqlite3.connect(f"C:\WorkspacePython\LeFoot\BDD\BDD_{self.nom}.db") # titouan
        # con2 = sqlite3.connect(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\BDD_{self.nom}.db")
        cur = con.cursor()  # Création du curseur.
        cur2 = con2.cursor()
        cur2.execute("CREATE TABLE effectif(id, prénom, nom, poste, note)")  # Création de la table de sauvegarde

        # Création de listes aléatoires contenant les futurs attaquants, défenseurs, milieux et gardiens du club.
        attaquant = cur.execute("SELECT DISTINCT * FROM reserve_joueurs "
                                "WHERE poste == 'Attaquant' ORDER BY random() LIMIT 3")
        at = attaquant.fetchall()
        defenseur = cur.execute("SELECT DISTINCT * FROM reserve_joueurs "
                                "WHERE poste == 'Défenseur' ORDER BY random() LIMIT 3")
        de = defenseur.fetchall()
        milieu = cur.execute("SELECT DISTINCT * FROM reserve_joueurs "
                             "WHERE poste == 'Milieu' ORDER BY random() LIMIT 4")
        mi = milieu.fetchall()
        gardien = cur.execute("SELECT DISTINCT * FROM reserve_joueurs "
                              "WHERE poste == 'Gardien' ORDER BY random() LIMIT 1")
        ga = gardien.fetchall()

        # Ajout des joueurs précédemment sélectionnés dans les effectifs du club.
        # On retire ensuite les joueurs sélectionnés de la BDD reserve_joueurs.
        for j in at:
            joueur = Attaquant(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            # Sauvegarde des joueurs dans la table associée au club.
            data = (j[0], j[1], j[2], j[3], j[4])
            cur2.execute("INSERT INTO effectif(id, prénom, nom, poste, note) VALUES(?, ?, ?, ?, ?)", data)
            con.commit()
            con2.commit()
        for j in de:
            joueur = Defenseur(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            # Sauvegarde des joueurs dans la table associée au club.
            data = (j[0], j[1], j[2], j[3], j[4])
            cur2.execute("INSERT INTO effectif(id, prénom, nom, poste, note) VALUES(?, ?, ?, ?, ?)", data)
            con.commit()
            con2.commit()
        for j in mi:
            joueur = Milieu(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            # Sauvegarde des joueurs dans la table associée au club.
            data = (j[0], j[1], j[2], j[3], j[4])
            cur2.execute("INSERT INTO effectif(id, prénom, nom, poste, note) VALUES(?, ?, ?, ?, ?)", data)
            con.commit()
            con2.commit()
        for j in ga:
            joueur = Gardien(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            # Sauvegarde des joueurs dans la table associée au club.
            data = (j[0], j[1], j[2], j[3], j[4])
            cur2.execute("INSERT INTO effectif(id, prénom, nom, poste, note) VALUES(?, ?, ?, ?, ?)", data)
            con.commit()
            con2.commit()
        # On remplit la liste "équipe" qui correspond aux joueurs actifs
        for j in self:
            self.equipe.append(j)


    def remplissage_copie_bdd(self):
        """
        Méthode permettant de copier les effectifs d'un club entre deux championnats pour simuler de nouveau
        le même championnat.
        """
        con = sqlite3.connect(f"C:\WorkspacePython\LeFoot\BDD\BDD_{self.nom}.db") # titouan
        # con = sqlite3.connect(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\BDD_{self.nom}.db")
        cur = con.cursor()

        # On sélectionne tous les joueurs de la table en les séparant par poste.
        attaquant = cur.execute("SELECT * FROM effectif WHERE poste == 'Attaquant'")
        at = attaquant.fetchall()
        defenseur = cur.execute("SELECT * FROM effectif WHERE poste == 'Défenseur'")
        de = defenseur.fetchall()
        milieu = cur.execute("SELECT * FROM effectif WHERE poste == 'Milieu'")
        mi = milieu.fetchall()
        gardien = cur.execute("SELECT * FROM effectif WHERE poste == 'Gardien'")
        ga = gardien.fetchall()

        for j in at:
            joueur = Attaquant(j[1], j[2], j[4], self.nom)
            self.append(joueur)
        for j in de:
            joueur = Defenseur(j[1], j[2], j[4], self.nom)
            self.append(joueur)
        for j in mi:
            joueur = Milieu(j[1], j[2], j[4], self.nom)
            self.append(joueur)
        for j in ga:
            joueur = Gardien(j[1], j[2], j[4], self.nom)
            self.append(joueur)
        # On remplit la liste "équipe" qui correspond aux joueurs actifs
        for j in self:
            self.equipe.append(j)


    def victoire(self):
        self.score += 3
        self.nb_victoires += 1


    def nul(self):
        self.score += 1
        self.nb_nuls += 1


    def ajout_match_realise(self, club, e):
        """
        Méthode ajoutant les clubs qui ont joué contre le club à domicile ou à l'extérieur.

        club : club contre qui le match a été joué.
        e: e="dom" si le match s'est fait à domicile. e="ext" si le match s'est fait à l'extérieur.
        """
        if e == "dom":
            self.match_realise_dom.append(club)
        elif e == "ext":
            self.match_realise_ext.append(club)


    def liste_joueurs(self, fichier):
        """
        Méthode permettant l'enregistrement de la composition du club dans un fichier.

        fichier : fichier où enregistrer les données pour les afficher.
        """
        fichier.write(f"Le club {self.nom} dispose des joueurs suivants :\n")
        for j in self:
            fichier.write(f"   > {j}\n")
        fichier.write("\n")
        fichier.write(f"L'entraineur est {self.entraineur}\n")

    def classement_buteurs_club(self):
        """
        Méthode permettant de classer les buteurs du club par ordre décroissant de buts.
        Renvoie la liste triée des buteurs.
        """
        buteurs = []
        for j in self:
            if j.poste == "Attaquant" and j.nb_buts != 0:  # On prend tous les attaquants ayant marqué
                buteurs.append(j)
        return sorted(buteurs, key=self.triage, reverse=True)  # Utilisation de la fonction triage pour trier la liste


    def triage(self, joueur):
        """
        Fonction permettant le triage en fonction du nombre de buts.
        """
        return joueur.nb_buts


    def calcul_note_club_log(self, fichier):
        """
        Méthode permettant le calcul de la note du club et son enregistrement dans un fichier.

        fichier : fichier où enregistrer les données pour les afficher.
        """
        cpt = 0
        self.note_club = 0  # On remet la note à 0 pour être sûr
        if len(self) != 0:
            # Pour chaque joueur du club, on ajoute sa note à celle du club.
            for j in self:
                self.note_club += j.note
                cpt += 1
            self.note_club = self.note_club/cpt  # On divise par le nombre de joueur pour faire une moyenne
            fichier.write(f"La note du club {self.nom} est : {self.note_club:.1f}\n")
        else:
            fichier.write(f"Il n'y a aucun joueur dans le club {self.nom}\n")


    def calcul_note_club(self):
        """
        Méthode permettant le calcul de la note du club.
        """
        cpt = 0
        self.note_club = 0  # On remet la note à 0 pour être sûr
        if len(self) != 0:
            # Pour chaque joueur du club, on ajoute sa note à celle du club.
            for j in self:
                self.note_club += j.note
                cpt += 1
            self.note_club = self.note_club/cpt  # On divise par le nombre de joueur pour faire une moyenne
            print(f"La note du club {self.nom} est : {self.note_club:.1f}")
        else:
            print(f"Il n'y a aucun joueur dans le club {self.nom}")

    def calcul_note_equipe(self):
        """
        Méthode permettant le calcul de la note de l'équipe active.
        """
        self.note_equipe = 0  # On remet la note à 0 pour être sûr
        # Pour chaque joueur de l'équipe active, on ajoute sa note à celle de l'équipe.
        for j in self.equipe:
            self.note_equipe += j.note
        self.note_equipe = self.note_equipe/11  # On divise par 11 pour faire une moyenne
        print(f"La note de l'équipe active du club {self.nom} est : {self.note_equipe:.1f}")

    def fiche_club(self, final):
        """
        Fonction enregistrant les données du club (joueurs, entraineur, nom et note du club).

        final : paramètre spécifiant si la fiche est créée à la fin du championnat ou non.
        """
        fichier_club = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {self.nom}.txt", 'wt') #titouan
        # fichier_club = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\fiche de {self.nom}.txt", 'wt')
        self.liste_joueurs(fichier_club)
        self.calcul_note_club_log(fichier_club)
        buteurs = self.classement_buteurs_club()
        fichier_club.write("\n")
        # Si on veut afficher la fiche du club à la fin du championnat, on ajoute le classement des buteurs et le
        # nombre d'arrêts du gardien.
        if final == True:
            fichier_club.write(f"Les meilleurs buteurs de {self.nom} sont :\n")
            for j in buteurs:
                fichier_club.write(f"    {j.prenom[0]}.{j.nom} avec {j.nb_buts} buts\n")
            fichier_club.write("\n")
            fichier_club.write(f"{self[-1].prenom[0]}.{self[-1].nom} a arrêté {self[-1].nb_arrets} tirs.\n")
        fichier_club.close()