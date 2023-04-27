import sqlite3
import random as rd
from Joueur import *

class Club(list):
    """
    Classe gérant les informations relatives au club et contenant la liste des joueurs
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



    def remplissage_BDD(self):
        """
        Méthode permettant le remplissage des effectifs du club à partir de la BDD reserve_joueurs.
        """
        # con = sqlite3.connect("C:\WorkspacePython\LeFoot\BDD\BDD_joueurs.db")  # Mise en place de la connexion avec la database.
        con = sqlite3.connect("C:\Users\hadrien dupuy\Desktop\ENSTA B\1A\2.4 projets\Projet informatique\BDD_joueurs.db")
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
            joueur = Attaquant(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            con.commit()
        for j in de:
            joueur = Defenseur(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            con.commit()
        for j in mi:
            joueur = Milieu(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            con.commit()
        for j in ga:
            joueur = Gardien(j[1], j[2], j[4], self.nom)
            self.append(joueur)
            cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
            con.commit()


    def victoire(self):
        self.score += 3


    def nul(self):
        self.score += 1


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
        Fonction permettant de classer les buteurs du club par ordre décroissant de buts.
        Renvoie la liste triée des buteurs.
        """
        buteurs = []
        for j in self:
            if j.poste == "Attaquant" and j.nb_buts != 0:  # On prend tous les attaquants ayant marqué
                attaquant = j
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
            for j in self:
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
        if len(self) != 0:
            for j in self:
                self.note_club += j.note
                cpt += 1
            self.note_club = self.note_club/cpt
            print(f"La note du club {self.nom} est : {self.note_club:.1f}")
        else:
            print(f"Il n'y a aucun joueur dans le club {self.nom}")


    def affichage_score(self):
        print(f"{self.nom} à un score de {self.score}")



    def fiche_club(self):
        """
        Fonction enregistrant les données du club (joueurs, entraineur, nom et note du club).
        """
        fichier_club = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {self.nom}", 'wt')
        self.liste_joueurs(fichier_club)
        self.calcul_note_club_log(fichier_club)
        buteurs = self.classement_buteurs_club()
        fichier_club.write("\n")
        fichier_club.write(f"Les meilleurs buteurs de {self.nom} sont :\n")
        for j in buteurs:
            fichier_club.write(f"    {j.prenom[0]}.{j.nom} avec {j.nb_buts} buts\n")
        fichier_club.write("\n")
        fichier_club.write(f"{self[-1].prenom[0]}.{self[-1].nom} a arrêté {self[-1].nb_arrets} tirs.\n")
        fichier_club.close()