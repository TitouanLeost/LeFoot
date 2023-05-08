import Club as Cl
import Journée as J
import Championnat as Ch
from Joueur import *
import unittest

sb = Cl.Club("Stade Brestois 29", "Philippe")
sr = Cl.Club("Stade Rennais FC", "Catherine")
se = Cl.Club("AS Saint-Etienne", "Etienne")
gu = Cl.Club("En Avant Guingamp", "Joel")
fs = Cl.Club("FC Silmi", "Félix")
cc = Cl.Club("Cagliari Calcio", "Charlie")
sc = Cl.Club("SM Caen", "Jacob")
rl = Cl.Club("RC Lens", "Simone")


sb.remplissage_BDD()
sr.remplissage_BDD()
se.remplissage_BDD()
gu.remplissage_BDD()
fs.remplissage_BDD()
cc.remplissage_BDD()
sc.remplissage_BDD()
rl.remplissage_BDD()


class TestJournee(unittest.TestCase):
    def Test_resultat(self):
        Jour = J.Journee
        self.assertTrue(max(Jour.but_c1,Jour.but_c2)<7) # on regarde si le score est réaliste (pas plus de 7 buts par matchs)




class TestChampionnat(unittest.TestCase):
    def Test_dom_ext(self):
        club = Ch.Championnat()
        Jour = Ch.Championnat()
        self.assertIsInstance(club.clubs, list)
        self.assertEqual(Jour.journees, 14)

    def Test_club(self):
        champ = Ch.Championnat("champ", [sb, sr, se, gu, fs, cc, sc, rl])
        self.assertIs()



class TestClub(unittest.TestCase):
    def Test_note(self):
        noteC = Cl.Club()
        self.assertTrue(noteC.note_club<85 and noteC.note_club>55) #on regarde si les notes des clubs sont réalistes (ni trop élevée, ni trop faible)

if __name__ == '__main__':
    rl.Test_note()