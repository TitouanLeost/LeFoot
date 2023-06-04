import unittest
from unittest import mock
from unittest.mock import MagicMock

from Joueur import Joueur, Gardien, Attaquant, Milieu, Defenseur
from Journée import Journee
from Championnat import Championnat
from Club import Club


class TestJoueur(unittest.TestCase):

    def test_joueur_creation(self):
        '''
        test qui s'assure que de la bonne création d'un joueur
        '''
        joueur = Joueur("John", "Doe", 8.2, "Club 1")
        self.assertEqual(joueur.prenom, "John")
        self.assertEqual(joueur.nom, "Doe")
        self.assertEqual(joueur.note, 8.2)
        self.assertEqual(joueur.club, "Club 1")

    def test_gardien_creation(self):
        '''
        test qui s'assure de la bonne création d'un gardien
        '''
        gardien = Gardien("Jason", "Boullier", 8.5, "Club 2")
        self.assertEqual(gardien.prenom, "Jason")
        self.assertEqual(gardien.nom, "Boullier")
        self.assertEqual(gardien.note, 8.5)
        self.assertEqual(gardien.club, "Club 2")
        self.assertEqual(gardien.poste, "Gardien")
        self.assertEqual(gardien.nb_arrets, 0)

    def test_attaquant_creation(self):
        '''
        test qui s'assure de la bonne création d'un attaquant
        '''
        attaquant = Attaquant("Akim", "Jawad", 7.8, "Club 3")
        self.assertEqual(attaquant.prenom, "Akim")
        self.assertEqual(attaquant.nom, "Jawad")
        self.assertEqual(attaquant.note, 7.8)
        self.assertEqual(attaquant.club, "Club 3")
        self.assertEqual(attaquant.poste, "Attaquant")
        self.assertEqual(attaquant.nb_buts, 0)

    def test_milieu_creation(self):
        '''
        test qui s'assure de la bonne création d'un milieu
        '''
        milieu = Milieu("Pierre", "Bonzi", 7.2, "Club 4")
        self.assertEqual(milieu.prenom, "Pierre")
        self.assertEqual(milieu.nom, "Bonzi")
        self.assertEqual(milieu.note, 7.2)
        self.assertEqual(milieu.club, "Club 4")
        self.assertEqual(milieu.poste, "Milieu")

    def test_defenseur_creation(self):
        '''
        test qui s'assure de la bonne création d'un défenseur
        '''
        defenseur = Defenseur("Virgil", "Dupont", 6.9, "Club 5")
        self.assertEqual(defenseur.prenom, "Virgil")
        self.assertEqual(defenseur.nom, "Dupont")
        self.assertEqual(defenseur.note, 6.9)
        self.assertEqual(defenseur.club, "Club 5")
        self.assertEqual(defenseur.poste, "Défenseur")

    def test_gardien_arret(self):
        '''
        test qui s'assure que lorsque le gardien fait un arret, celui-ci
        soit bien comptabilisé
        '''
        gardien = Gardien("Jason", "Boullier", 8.5, "Club 2")
        gardien.arret()
        self.assertEqual(gardien.nb_arrets, 1)

    def test_attaquant_but(self):
        '''
        test qui s'assure que lorsque l'attaquant marque, celui-ci
        soit bien comptabilisé
        '''
        attaquant = Attaquant("Akim", "Jawad", 7.8, "Club 3")
        attaquant.but()
        self.assertEqual(attaquant.nb_buts, 1)



class TestClub(unittest.TestCase):

    def setUp(self):
        self.club = Club("Mon Club", "Entraîneur")

    def test_victoire(self):
        '''
        teste le fait qu'une victoire rapporte 3 points lorsque le score de l'équipe vainqueur est supérieur au
        score de l'équipe perdante
        '''
        self.club1 = Club("Mon Club 1", "Entraîneur 1")
        self.club2 = Club("Mon Club 2", "Entraîneur 2")
        self.club1.victoire()
        self.assertEqual(self.club1.score, 3)
        self.assertTrue(self.club1.score > self.club2.score)

    def test_nul(self):
        '''
        teste le fait qu'un match nul rapporte 1 points à chaque équipe lorsque leurs scores sont égaux
        '''
        self.club.nul()
        self.assertEqual(self.club.score, 1)

    def test_ajout_match_realise(self):
        '''
        teste le fait que les matchs soientt bien enregistrés et que l'on enregistre bien qui joue à domicile
        ou à l'extérieur
        '''
        # Test the method to add the clubs played against to the club's match records
        self.club.ajout_match_realise("Club 1", "dom")
        self.club.ajout_match_realise("Club 2", "ext")
        self.assertEqual(len(self.club.match_realise_dom), 1)
        self.assertEqual(len(self.club.match_realise_ext), 1)
        self.assertIn("Club 1", self.club.match_realise_dom)
        self.assertIn("Club 2", self.club.match_realise_ext)

    def test_taille(self):
        '''
        teste le remplissage d'un club avec des joueurs et s'assure qu'une équipe est bien constitué de 11 joueurs
        '''
        self.club1 = Club("Mon Club 1", "Entraîneur 1")
        self.club2 = Club("Mon Club 2", "Entraîneur 2")
        self.championnat = Championnat("ligue 3", [self.club1, self.club2])
        self.club1.remplissage_bdd()
        self.assertEqual(len(self.club1.equipe),11)




class TestJournée(unittest.TestCase):

    def setUp(self):
        self.club1 = Club("Club 1", "entraineur 1")
        self.club2 = Club("Club 2", "entraineur 2")
        self.club3 = Club("Club 3", "entraineur 3")
        self.club4 = Club("Club 4", "entraineur 4")
        self.club5 = Club("Mon Club 5", "Entraîneur 5")
        self.club6 = Club("Mon Club 6", "Entraîneur 6")
        self.club7 = Club("Mon Club 7", "Entraîneur 7")
        self.club8 = Club("Mon Club 8", "Entraîneur 8")
        self.championnat = Championnat("ligue 3",[self.club1, self.club2, self.club3, self.club4, self.club5, self.club6,self.club7, self.club8])

        # Création d'une journée de match
        self.journee = Journee(1, self.championnat)

    def test_initialistaion(self):
        '''
        teste le fait que les variables interessantes soient bien initialisés à chaque début de journée
        '''
        self.assertEqual(self.journee.num, 1)
        self.assertEqual(len(self.journee.matchs), 0)
        self.assertEqual(len(self.journee.joueurs_cartons), 0)
        self.assertEqual(len(self.journee.joueurs_blessures), 0)


class TestChampionnat(unittest.TestCase):
    def setUp(self):
        self.club1 = mock.MagicMock()
        self.club2 = mock.MagicMock()
        self.club3 = mock.MagicMock()
        self.clubs = [self.club1, self.club2, self.club3]
        self.championnat = Championnat("Ligue 1", self.clubs)

    def test_remplissage(self):
        '''
        teste le fait que le championnat posséde bien les clubs que l'on souhaite
        '''
        self.club1.remplissage_bdd.return_value = None
        self.club2.remplissage_bdd.return_value = None
        self.club3.remplissage_bdd.return_value = None

        self.championnat.remplissage(False)

        self.assertEqual(len(self.championnat.clubs), 3)
        self.club1.remplissage_bdd.assert_called_once()
        self.club2.remplissage_bdd.assert_called_once()
        self.club3.remplissage_bdd.assert_called_once()


    def test_triage_buts(self):
        '''
        teste le triage des buts
        '''
        joueur = mock.MagicMock()
        joueur.nb_buts = 10

        result = self.championnat.triage_buts(joueur)

        self.assertEqual(result, 10)



if __name__ == '__main__':
    unittest.main()