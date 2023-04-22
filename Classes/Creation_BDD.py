import sqlite3
import random as rd
import prenoms as pr


def creation_bdd():
    """
    Fonction permettant la création de la BDD contenant les joueurs participant au championnat.
    Deux tables sont crées:
    joueurs permet de sauvegarder les joueurs du championnat
    reserve_joueurs permet de remplir les effectifs des clubs. A la fin du remplissage, reserve_joueurs est vide.
    """
    con = sqlite3.connect("C:\WorkspacePython\LeFoot\BDD\BDD_joueurs.db")  # Mise en place d'une connexion
    cur = con.cursor()  # Création du curseur
    cur.execute("CREATE TABLE joueurs(id, prénom, nom, poste, note)")  # Création de la table joueurs
    cur.execute("CREATE TABLE reserve_joueurs(id, prénom, nom, poste, note)")  # Création de la table reserve_joueurs
    # On enregistre les informations des joueurs dans une liste data.
    data = []
    for i in range(1, 25):
        data.append((i, pr.get_prenom(), pr.get_nom(), "Attaquant", rd.randint(20, 100)))
    for i in range(25, 49):
        data.append((i, pr.get_prenom(), pr.get_nom(), "Défenseur", rd.randint(20, 100)))
    for i in range(49, 81):
        data.append((i, pr.get_prenom(), pr.get_nom(), "Milieu", rd.randint(20, 100)))
    for i in range(81, 89):
        data.append((i, pr.get_prenom(), pr.get_nom(), "Gardien", rd.randint(20, 100)))
    # On ajoute les valeurs de data dans nos deux BDD.
    cur.executemany("INSERT INTO joueurs VALUES(?, ?, ?, ?, ?)", data)
    con.commit()
    cur.executemany("INSERT INTO reserve_joueurs VALUES(?, ?, ?, ?, ?)", data)
    con.commit()




