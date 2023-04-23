import Club as Cl
import Journée as Jour
import Championnat as Ch
import Joueur as Joue
import unittest

"""
Ceci est un test
"""
print("test")

class TestClub(unittest.TestCase):
    def Test_note(self):
        at = Joue.Attaquant()
        noteC = Cl.Club()
        self.assertTrue(noteC.note_club<85 and noteC.note_club>55) #on regarde si les notes des clubs sont réalistes (ni trop élevée, ni trop faible)

if __name__ == '__main__':
    unittest.main()