import unittest
from unittest.mock import MagicMock
from unittest import mock
from Joueur import Joueur, Gardien, Attaquant, Milieu, Defenseur
from Journée import Journee
from Championnat import Championnat
from io import StringIO
from Club import Club


class TestJoueur(unittest.TestCase):

    def test_joueur_creation(self):
        joueur = Joueur("John", "Doe", 8.2, "Club 1")
        self.assertEqual(joueur.prenom, "John")
        self.assertEqual(joueur.nom, "Doe")
        self.assertEqual(joueur.note, 8.2)
        self.assertEqual(joueur.club, "Club 1")

    def test_gardien_creation(self):
        gardien = Gardien("Jason", "Boullier", 8.5, "Club 2")
        self.assertEqual(gardien.prenom, "Jason")
        self.assertEqual(gardien.nom, "Boullier")
        self.assertEqual(gardien.note, 8.5)
        self.assertEqual(gardien.club, "Club 2")
        self.assertEqual(gardien.poste, "Gardien")
        self.assertEqual(gardien.nb_arrets, 0)

    def test_attaquant_creation(self):
        attaquant = Attaquant("Akim", "Jawad", 7.8, "Club 3")
        self.assertEqual(attaquant.prenom, "Akim")
        self.assertEqual(attaquant.nom, "Jawad")
        self.assertEqual(attaquant.note, 7.8)
        self.assertEqual(attaquant.club, "Club 3")
        self.assertEqual(attaquant.poste, "Attaquant")
        self.assertEqual(attaquant.nb_buts, 0)

    def test_milieu_creation(self):
        milieu = Milieu("Pierre", "Bonzi", 7.2, "Club 4")
        self.assertEqual(milieu.prenom, "Pierre")
        self.assertEqual(milieu.nom, "Bonzi")
        self.assertEqual(milieu.note, 7.2)
        self.assertEqual(milieu.club, "Club 4")
        self.assertEqual(milieu.poste, "Milieu")

    def test_defenseur_creation(self):
        defenseur = Defenseur("Virgil", "Dupont", 6.9, "Club 5")
        self.assertEqual(defenseur.prenom, "Virgil")
        self.assertEqual(defenseur.nom, "Dupont")
        self.assertEqual(defenseur.note, 6.9)
        self.assertEqual(defenseur.club, "Club 5")
        self.assertEqual(defenseur.poste, "Défenseur")

    def test_gardien_arret(self):
        gardien = Gardien("Jason", "Boullier", 8.5, "Club 2")
        gardien.arret()
        self.assertEqual(gardien.nb_arrets, 1)

    def test_attaquant_but(self):
        attaquant = Attaquant("Akim", "Jawad", 7.8, "Club 3")
        attaquant.but()
        self.assertEqual(attaquant.nb_buts, 1)



class TestClub(unittest.TestCase):

    def setUp(self):
        self.club = Club("Mon Club", "Entraîneur")

    def test_victoire(self):
        # Test the method to increase the club's score after a victory
        self.club.victoire()
        self.assertEqual(self.club.score, 3)

    def test_nul(self):
        # Test the method to increase the club's score after a draw
        self.club.nul()
        self.assertEqual(self.club.score, 1)

    def test_ajout_match_realise(self):
        # Test the method to add the clubs played against to the club's match records
        self.club.ajout_match_realise("Club 1", "dom")
        self.club.ajout_match_realise("Club 2", "ext")
        self.assertEqual(len(self.club.match_realise_dom), 1)
        self.assertEqual(len(self.club.match_realise_ext), 1)
        self.assertIn("Club 1", self.club.match_realise_dom)
        self.assertIn("Club 2", self.club.match_realise_ext)



class TestJournée(unittest.TestCase):

    def setUp(self):
        # Création d'un championnat fictif avec 4 clubs
        self.club1 = Club("Club 1", "entraineur 1")
        self.club2 = Club("Club 2", "entraineur 2")
        self.club3 = Club("Club 3", "entraineur 3")
        self.club4 = Club("Club 4", "entraineur 4")
        self.clubs = [self.club1, self.club2, self.club3, self.club4]
        self.championnat = Championnat("ligue 3", self.clubs)

        # Création d'une journée de match
        self.journee = Journee(1, self.championnat)

    def test_initialistaion(self):
        # Vérification de l'initialisation des attributs
        self.assertEqual(self.journee.num, 1)
        self.assertEqual(len(self.journee.matchs), 0)
        self.assertEqual(len(self.journee.joueurs_cartons), 0)
        self.assertEqual(len(self.journee.joueurs_blessures), 0)

    '''def test_dom_ext(self):  # il faut remplir le championnat
        self.championnat = Championnat("ligue1", [sb, sr, se, gu, fs, cc, sc, rl])
        self.championnat.simuler()
        dom = 0
        ext = 0
        for i in range(len(club.match_realise_dom)):
            dom += 1
        for j in range(len(club.match_realise_ext)):
            ext += 1
        self.assertEqual(dom, 7)  # on regarde si il y a bien eu 7 matchs joué à domicile
        self.assertEqual(ext, 7)  # et 7 matchs joué à l'éxterieur'''

class TestChampionnat(unittest.TestCase):
    def setUp(self):
        self.club1 = mock.MagicMock()
        self.club2 = mock.MagicMock()
        self.club3 = mock.MagicMock()
        self.clubs = [self.club1, self.club2, self.club3]
        self.championnat = Championnat("Ligue 1", self.clubs)

    def test_remplissage(self):
        self.club1.remplissage_bdd.return_value = None
        self.club2.remplissage_bdd.return_value = None
        self.club3.remplissage_bdd.return_value = None

        self.championnat.remplissage(False)

        self.assertEqual(len(self.championnat.clubs), 3)
        self.club1.remplissage_bdd.assert_called_once()
        self.club2.remplissage_bdd.assert_called_once()
        self.club3.remplissage_bdd.assert_called_once()

    def test_simuler(self):
        journee1 = mock.MagicMock()
        journee2 = mock.MagicMock()
        self.championnat.journees_liste = [journee1, journee2]
        self.championnat.score_final = mock.MagicMock()
        self.championnat.tableau_score = mock.MagicMock()
        self.championnat.classement_buteurs = mock.MagicMock()

        self.championnat.simuler()

        self.assertEqual(self.championnat.score_final.call_count, 1)
        self.assertEqual(self.championnat.tableau_score.call_count, 1)
        self.assertEqual(self.championnat.classement_buteurs.call_count, 1)

    def test_triage_buts(self):
        joueur = mock.MagicMock()
        joueur.nb_buts = 10

        result = self.championnat.triage_buts(joueur)

        self.assertEqual(result, 10)

    def test_tableau_score(self):
        self.championnat.liste_scores = [self.club1, self.club2, self.club3]
        self.championnat.liste_scores[0].__str__.return_value = "Club1"
        self.championnat.liste_scores[0].score = 20
        self.championnat.liste_scores[0].nb_buts = 50
        self.championnat.liste_scores[1].__str__.return_value = "Club2"
        self.championnat.liste_scores[1].score = 18
        self.championnat.liste_scores[1].nb_buts = 40
        self.championnat.liste_scores[2].__str__.return_value = "Club3"
        self.championnat.liste_scores[2].score = 16
        self.championnat.liste_scores[2].nb_buts = 35

        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            self.championnat.tableau_score()

            mock_open.assert_called_once_with(
                "C:\WorkspacePython\LeFoot\Fichiers\\fichier des scores finaux.txt", 'wt'
            )
            file_handle = mock_open()
            file_handle.write.assert_called()
            self.assertEqual(file_handle.write.call_count, 3)

            expected_calls = [
                mock.call("Club1 remporte Ligue 1 avec 20 points et 50 buts marqués !\n"),
                mock.call("Club2 fini le championnat avec 18 points et 40 buts marqués.\n"),
                mock.call("Club3 fini le championnat avec 16 points et 35 buts marqués.\n")
            ]
            file_handle.write.assert_has_calls(expected_calls, any_order=True)
            file_handle.close()
            self.assertEqual(file_handle.close.call_count, 1)




'''sb = Club("Stade Brestois 29", "Philippe")
sr = Club("Stade Rennais FC", "Catherine")
se = Club("AS Saint-Etienne", "Etienne")
gu = Club("En Avant Guingamp", "Joel")
fs = Club("FC Silmi", "Félix")
cc = Club("Cagliari Calcio", "Charlie")
sc = Club("SM Caen", "Jacob")
rl = Club("RC Lens", "Simone")

sb.remplissage_BDD()
sr.remplissage_BDD()
se.remplissage_BDD()
gu.remplissage_BDD()
fs.remplissage_BDD()
cc.remplissage_BDD()
sc.remplissage_BDD()
rl.remplissage_BDD()'''


if __name__ == '__main__':
    unittest.main()