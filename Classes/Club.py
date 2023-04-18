import sqlite3
import random as rd
from Joueur import *

class Club():
    """
    Classe gérant les informations relatives au club.
    """
    def __init__(self, nom, entraineur):
        self.nom = nom
        self.entraineur = entraineur
        self.joueurs = []
        self.score = 0
        self.nb_buts = 0
        self.note_club = 0
        self.match_realise_dom = []
        self.match_realise_ext = []


    def __str__(self):
        return f"{self.nom}"


    def remplissage(self, liste):
        """
        Méthode permettant le remplissage du club avec des joueurs.

        liste : liste des joueurs à ajouter au club
        """
        for j in liste:
            self.joueurs.append(j)


    def remplissage_BDD(self):
        """
        Méthode permettant le remplissage des effectifs du club à partir de la BDD reserve_joueurs.
        """
        con = sqlite3.connect("C:\WorkspacePython\LeFoot\BDD\BDD_joueurs.db")  # Mise en place de la connexion avec la database.
        cur = con.cursor()  # Création du curseur.
        # Création de listes aléatoires contenant les futurs attaquants, défenseurs, milieux et gardiens du club.
        attaquant = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Attaquant' ORDER BY random() LIMIT 3")
        at = attaquant.fetchall()
        defenseur = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Défenseur' ORDER BY random() LIMIT 3")
        de = defenseur.fetchall()
        milieu = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Milieu' ORDER BY random() LIMIT 4")
        mi = milieu.fetchall()
        gardien = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Gardien' ORDER BY random() LIMIT 1")
        ga = gardien.fetchall()
        # Ajout des joueurs précédemment sélectionnés dans les effectifs du club.
        # On retire ensuite les joueurs sélectionnés de la BDD.
        for j in at:
            joueur = Attaquant(j[2], j[4], self.nom)
            self.joueurs.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
        for j in de:
            joueur = Defenseur(j[2], j[4], self.nom)
            self.joueurs.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
        for j in mi:
            joueur = Milieu(j[2], j[4], self.nom)
            self.joueurs.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
        for j in ga:
            joueur = Gardien(j[2], j[4], self.nom)
            self.joueurs.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])


    def liste_joueurs(self, fichier):
        """
        Méthode permettant l'enregistrement de la composition du club dans un fichier.

        fichier : fichier où enregistrer les données pour les afficher.
        """
        fichier.write(f"Le club {self.nom} dispose des joueurs suivants :\n")
        for j in self.joueurs:
            fichier.write(f"{j}\n")
        fichier.write(f"L'entraineur est {self.entraineur}\n")


    def calcul_note_club_log(self, fichier):
        """
        Méthode permettant le calcul de la note du club et son enregistrement dans un fichier.

        fichier : fichier où enregistrer les données pour les afficher.
        """
        cpt = 0
        self.note_club = 0  # On remet la note à 0 pour être sûr
        if len(self.joueurs) != 0:
            for j in self.joueurs:
                self.note_club += j.note
                cpt += 1
            self.note_club = self.note_club/cpt
            fichier.write(f"La note du club {self.nom} est : {self.note_club:.1f}\n")
        else:
            fichier.write(f"Il n'y a aucun joueur dans le club {self.nom}\n")


    def calcul_note_club(self):
        """
        Méthode permettant le calcul de la note du club.
        """
        cpt = 0
        self.note_club = 0  # On remet la note à 0 pour être sûr
        if len(self.joueurs) != 0:
            for j in self.joueurs:
                self.note_club += j.note
                cpt += 1
            self.note_club = self.note_club/cpt
            print(f"La note du club {self.nom} est : {self.note_club:.1f}")
        else:
            print(f"Il n'y a aucun joueur dans le club {self.nom}")


    def victoire(self):
        self.score += 2


    def nul(self):
        self.score += 1


    def affichage_score(self):
        print(f"{self.nom} à un score de {self.score}")


    def ajout_match_realise(self, club, e):
        """
        Fonction ajoutant les clubs qui ont joué contre le club à domicile ou à l'extérieur.

        club : club contre qui le match a été joué.
        e: e="dom" si le match s'est fait à domicile. e="ext" si le match s'est fait à l'extérieur.
        """
        if e == "dom":
            self.match_realise_dom.append(club)
        elif e == "ext":
            self.match_realise_ext.append(club)

    def fiche_club(self):
        """
        Fonction enregistrant les données du club (joueurs, entraineur, nom et note du club).
        """
        fichier_club = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {self.nom}", 'wt')
        self.liste_joueurs(fichier_club)
        self.calcul_note_club_log(fichier_club)
        fichier_club.close()