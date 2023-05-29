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




'''sb = Cl.Club("Stade Brestois 29", "Philippe")
sr = Cl.Club("Stade Rennais FC", "Catherine")
se = Cl.Club("AS Saint-Etienne", "Etienne")
gu = Cl.Club("En Avant Guingamp", "Joel")
fs = Cl.Club("FC Silmi", "Félix")
cc = Cl.Club("Cagliari Calcio", "Charlie")
sc = Cl.Club("SM Caen", "Jacob")
rl = Cl.Club("RC Lens", "Simone")

A1 = Attaquant("Kévin","a", 72, sb)
A2 = Attaquant("Kevine", "b", 83, sb)
A3 = Attaquant("Keveen", "c", 64, sb)
A4 = Attaquant("Paul", "d", 26, sr)
A5 = Attaquant("Pol", "e", 74, sr)
A6 = Attaquant("Paulo", "f", 98, sr)
A7 = Attaquant("Jose", "g", 53, se)
A8 = Attaquant("Jause", "h", 48, se)
A9 = Attaquant("Jeauze", "i", 98, se)
A10 = Attaquant("Kylian", "j", 39, gu)
A11 = Attaquant("Kilian", "k", 72, gu)
A12 = Attaquant("Kilyane", "l", 53, gu)
A13 = Attaquant("William", "m", 34, fs)
A14 = Attaquant("Wyliam", "n", 65, fs)
A15 = Attaquant("Williameuh", "o", 78, fs)
A16 = Attaquant("Gabriel", "p", 65, cc)
A17 = Attaquant("Gabryelle", "q", 93, cc)
A18 = Attaquant("Guabriaile", "r", 67, cc)
A19 = Attaquant("Dylan", "s", 53, sc)
A20 = Attaquant("Dilane", "t", 48, sc)
A21 = Attaquant("Dit Lan", "u", 98, sc)
A22 = Attaquant("Nicolas", "v", 78, rl)
A23 = Attaquant("Niquola", "w", 53, rl)
A24 = Attaquant("Nickaula", "x", 76, rl)

G1 = Gardien("Timothée", "a", 100, sb)
G2 = Gardien("Didier", "b", 88, sr)
G3 = Gardien("Godefroy", "c", 65, se)
G4 = Gardien("Armand", "d", 79, gu)
G5 = Gardien("Théo", "e", 32, fs)
G6 = Gardien("Nolan", "f", 57, cc)
G7 = Gardien("Zack", "g", 78, sc)
G8 = Gardien("Loic", "h", 90, rl)

D1 = Defenseur("Philippe", "a", 63, sb)
D2 = Defenseur("Philipe", "b", 73, sb)
D3 = Defenseur("filipe", "c", 35, sb)
D4 = Defenseur("Patrick", "d", 77, sr)
D5 = Defenseur("Patrique", "e", 89, sr)
D6 = Defenseur("Pastric", "f", 92, sr)
D7 = Defenseur("Guy", "g", 97, se)
D8 = Defenseur("Gui", "h", 73, se)
D9 = Defenseur("Pierre", "i", 85, se)
D10 = Defenseur("Patrick", "j", 12, gu)
D11 = Defenseur("Patrique", "k", 53, gu)
D12 = Defenseur("Pastric", "l", 94, gu)
D13 = Defenseur("Andrew", "m", 76, fs)
D14 = Defenseur("Endrou", "n", 85, fs)
D15 = Defenseur("Handroo", "o", 45, fs)
D16 = Defenseur("Mattéo", "p", 67, cc)
D17 = Defenseur("Mathéo", "q", 69, cc)
D18 = Defenseur("Mataieau", "r", 83, cc)
D19 = Defenseur("Ryan", "s", 28, sc)
D20 = Defenseur("Raillan", "t", 55, sc)
D21 = Defenseur("Ryaneuh", "u", 63, sc)
D22 = Defenseur("Christian", "v", 94, rl)
D23 = Defenseur("Kristien", "w", 73, rl)
D24 = Defenseur("Qrisstianh", "x", 68, rl)

M1 = Milieu("Michel", "a", 57, sb)
M2 = Milieu("Michelle", "b", 82, sb)
M3 = Milieu("Micheleu", "c", 75, sb)
M4 = Milieu("Mishell", "d", 80, sb)
M5 = Milieu("Jean", "e", 63, sr)
M6 = Milieu("Jan", "f", 92, sr)
M7 = Milieu("Gean", "g", 78, sr)
M8 = Milieu("Jhan", "h", 38, sr)
M9 = Milieu("Jo", "i", 57, se)
M10 = Milieu("Geo", "j", 82, se)
M11 = Milieu("Jau", "k", 75, se)
M12 = Milieu("Jaw", "l", 80, se)
M13 = Milieu("Jacque", "m", 63, gu)
M14 = Milieu("Jacques", "n", 92, gu)
M15 = Milieu("Geake", "o", 78, gu)
M16 = Milieu("Jac", "p", 38, gu)
M17 = Milieu("Robert", "q", 74, fs)
M18 = Milieu("Raubair", "r", 83, fs)
M19 = Milieu("Rohbère", "s", 94, fs)
M20 = Milieu("Larousse", "t", 42, fs)
M21 = Milieu("Alexandre", "u", 76, cc)
M22 = Milieu("Alexendre", "v", 46, cc)
M23 = Milieu("Halaixandre", "w", 82, cc)
M24 = Milieu("Alécsandre", "x", 22, cc)
M25 = Milieu("Justin", "y", 77, sc)
M26 = Milieu("Justain", "z", 90, sc)
M27 = Milieu("Juste Un", "aa", 66, sc)
M28 = Milieu("Bridou", "bb", 48, sc)
M29 = Milieu("Tom", "cc", 86, rl)
M30 = Milieu("Tomme", "dd", 49, rl)
M31 = Milieu("Tome", "ee", 68, rl)
M32 = Milieu("Tommmmmmmmmmme", "ff", 67, rl)

sb.remplissage_BDD()
sr.remplissage_BDD()
se.remplissage_BDD()
gu.remplissage_BDD()
fs.remplissage_BDD()
cc.remplissage_BDD()
sc.remplissage_BDD()
rl.remplissage_BDD()

class TestChampionnat(unittest.TestCase):
    def test_var(self):
        c = Ch.Championnat("ligue1",[sb,sr,se,gu,fs,cc,sc,rl])
        c.simuler()
        self.assertIsInstance(c.clubs, list) # on regardre si c'est bien une liste
        self.assertEqual(c.journees, 14) # on regarde si il y a bien 14 journées (toutes les équipes se rencontrent 2 fois

    def test_dom_ext(self): # il faut remplir le championnat
        club = Cl.Club("Stade Brestois 29", "Philippe")
        c = Ch.Championnat("ligue1",[sb,sr,se,gu,fs,cc,sc,rl])
        c.simuler()
        dom = 0
        ext = 0
        for i in range (len(club.match_realise_dom)):
            dom += 1
        for j in range (len(club.match_realise_ext)):
            ext +=1
        self.assertEqual(dom, 7) # on regarde si il y a bien eu 7 matchs joué à domicile
        self.assertEqual(ext, 7) # et 7 matchs joué à l'éxterieur


class TestJournee(unittest.TestCase):
    def test_resultat(self): # il faut remplir le championnat
        champ = Ch.Championnat("ligue1",[sb,sr,se,gu,fs,cc,sc,rl])
        champ.simuler()
        max_but = champ.liste_scores[0] # problème car la liste n'est pas encore remplis. Je sais pas où on récupére les buts
        for i in range (7):
            if champ.liste_scores[i] > max_but:
                max_but = champ.liste_scores[i]
        self.assertTrue(max_but<8) # on regarde si le score est réaliste (pas plus de 8 buts pour une équipe)

    # def test_score(self):


    # def test_points(self):
        



class TestClub(unittest.TestCase): # il faut remplir le championnat
    def test_note(self):
        noteC = Cl.Club("Stade Brestois 29", "Philippe")
        champ = Ch.Championnat("ligue1",[sb,sr,se,gu,fs,cc,sc,rl])
        champ.simuler()
        self.assertTrue(noteC.note_club<85 and noteC.note_club>55) #on regarde si les notes des clubs sont réalistes (ni trop élevée, ni trop faible)'''

if __name__ == '__main__':
    unittest.main()