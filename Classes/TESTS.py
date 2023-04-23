import unittest
import Club as Cl
import Journée as J
import Championnat as Ch
from Joueur import *


sb = Cl.Club("Stade Brestois 29", "Philippe")
sr = Cl.Club("Stade Rennais FC", "Catherine")
se = Cl.Club("AS Saint-Etienne", "Etienne")
gu = Cl.Club("En Avant Guingamp", "Joel")
fs = Cl.Club("FC Silmi", "Félix")
cc = Cl.Club("Cagliari Calcio", "Charlie")
sc = Cl.Club("SM Caen", "Jacob")
rl = Cl.Club("RC Lens", "Simone")

A1 = Attaquant("Kévin", 72, sb)
A2 = Attaquant("Kevine", 83, sb)
A3 = Attaquant("Keveen", 64, sb)
A4 = Attaquant("Paul", 26, sr)
A5 = Attaquant("Pol", 74, sr)
A6 = Attaquant("Paulo", 98, sr)
A7 = Attaquant("Jose", 53, se)
A8 = Attaquant("Jause", 48, se)
A9 = Attaquant("Jeauze", 98, se)
A10 = Attaquant("Kylian", 39, gu)
A11 = Attaquant("Kilian", 72, gu)
A12 = Attaquant("Kilyane", 53, gu)
A13 = Attaquant("William", 34, fs)
A14 = Attaquant("Wyliam", 65, fs)
A15 = Attaquant("Williameuh", 78, fs)
A16 = Attaquant("Gabriel", 65, cc)
A17 = Attaquant("Gabryelle", 93, cc)
A18 = Attaquant("Guabriaile", 67, cc)
A19 = Attaquant("Dylan", 53, sc)
A20 = Attaquant("Dilane", 48, sc)
A21 = Attaquant("Dit Lan", 98, sc)
A22 = Attaquant("Nicolas", 78, rl)
A23 = Attaquant("Niquola", 53, rl)
A24 = Attaquant("Nickaula", 76, rl)

G1 = Gardien("Timothée", 100, sb)
G2 = Gardien("Didier", 88, sr)
G3 = Gardien("Godefroy", 65, se)
G4 = Gardien("Armand", 79, gu)
G5 = Gardien("Théo", 32, fs)
G6 = Gardien("Nolan", 57, cc)
G7 = Gardien("Zack", 78, sc)
G8 = Gardien("Loic", 90, rl)

D1 = Defenseur("Philippe", 63, sb)
D2 = Defenseur("Philipe", 73, sb)
D3 = Defenseur("filipe", 35, sb)
D4 = Defenseur("Patrick", 77, sr)
D5 = Defenseur("Patrique", 89, sr)
D6 = Defenseur("Pastric", 92, sr)
D7 = Defenseur("Guy", 97, se)
D8 = Defenseur("Gui", 73, se)
D9 = Defenseur("Pierre", 85, se)
D10 = Defenseur("Patrick", 12, gu)
D11 = Defenseur("Patrique", 53, gu)
D12 = Defenseur("Pastric", 94, gu)
D13 = Defenseur("Andrew", 76, fs)
D14 = Defenseur("Endrou", 85, fs)
D15 = Defenseur("Handroo", 45, fs)
D16 = Defenseur("Mattéo", 67, cc)
D17 = Defenseur("Mathéo", 69, cc)
D18 = Defenseur("Mataieau", 83, cc)
D19 = Defenseur("Ryan", 28, sc)
D20 = Defenseur("Raillan", 55, sc)
D21 = Defenseur("Ryaneuh", 63, sc)
D22 = Defenseur("Christian", 94, rl)
D23 = Defenseur("Kristien", 73, rl)
D24 = Defenseur("Qrisstianh", 68, rl)

M1 = Milieu("Michel", 57, sb)
M2 = Milieu("Michelle", 82, sb)
M3 = Milieu("Micheleu", 75, sb)
M4 = Milieu("Mishell", 80, sb)
M5 = Milieu("Jean", 63, sr)
M6 = Milieu("Jan", 92, sr)
M7 = Milieu("Gean", 78, sr)
M8 = Milieu("Jhan", 38, sr)
M9 = Milieu("Jo", 57, se)
M10 = Milieu("Geo", 82, se)
M11 = Milieu("Jau", 75, se)
M12 = Milieu("Jaw", 80, se)
M13 = Milieu("Jacque", 63, gu)
M14 = Milieu("Jacques", 92, gu)
M15 = Milieu("Geake", 78, gu)
M16 = Milieu("Jac", 38, gu)
M17 = Milieu("Robert", 74, fs)
M18 = Milieu("Raubair", 83, fs)
M19 = Milieu("Rohbère", 94, fs)
M20 = Milieu("Larousse", 42, fs)
M21 = Milieu("Alexandre", 76, cc)
M22 = Milieu("Alexendre", 46, cc)
M23 = Milieu("Halaixandre", 82, cc)
M24 = Milieu("Alécsandre", 22, cc)
M25 = Milieu("Justin", 77, sc)
M26 = Milieu("Justain", 90, sc)
M27 = Milieu("Juste Un", 66, sc)
M28 = Milieu("Bridou", 48, sc)
M29 = Milieu("Tom", 86, rl)
M30 = Milieu("Tomme", 49, rl)
M31 = Milieu("Tome", 68, rl)
M32 = Milieu("Tommmmmmmmmmme", 67, rl)

sb.remplissage([A1,A2,A3,G1,D1,D2,D3,M1,M2,M3,M4])
sr.remplissage([A4,A5,A6,G2,D4,D5,D6,M5,M6,M7,M8])
se.remplissage([A7,A8,A9,G3,D7,D8,D9,M9,M10,M11,M12])
gu.remplissage([A10,A11,A12,G4,D10,D11,D12,M13,M14,M15,M16])
fs.remplissage([A13,A14,A15,G5,D13,D14,D15,M17,M18,M19,M20])
cc.remplissage([A16,A17,A18,G6,D16,D17,D18,M21,M22,M23,M24])
sc.remplissage([A19,A20,A21,G7,D19,D20,D21,M25,M26,M27,M28])
rl.remplissage([A22,A23,A24,G8,D22,D23,D24,M29,M30,M31,M32])

class TestChampionnat(unittest.TestCase):
    def test_var(self):
        c = Ch.Championnat("ligue1")
        self.assertIsInstance(c.clubs, list) # on regardre si c'est bien une liste
        self.assertEqual(c.journees, 14) # on regarde si il y a bien 14 journées (toutes les équipes se rencontrent 2 fois

    def test_dom_ext(self):
        club = Cl.Club("Stade Brestois 29", "Philippe")
        dom = 0
        ext = 0
        for i in range (len(club.match_realise_dom)):
            dom += 1
        for j in range (len(club.match_realise_ext)):
            ext +=1
        self.assertEqual(dom, 7) # on regarde si il y a bien eu 7 matchs joué à domicile
        self.assertEqual(ext, 7) # et 7 matchs joué à l'éxterieur


class TestJournee(unittest.TestCase):
    def test_resultat(self):
        champ = Ch.Championnat("ligue1")
        max_but = champ.liste_scores[0] # problème car la liste n'est pas encore remplis. Je sais pas où on récupére les buts
        for i in range (7):
            if champ.liste_scores[i] > max_but:
                max_but = champ.liste_scores[i]
        self.assertTrue(max_but<8) # on regarde si le score est réaliste (pas plus de 8 buts pour une équipe)




class TestClub(unittest.TestCase):
    def test_note(self):
        noteC = Cl.Club("Stade Brestois 29", "Philippe")
        self.assertTrue(noteC.note_club<85 and noteC.note_club>55) #on regarde si les notes des clubs sont réalistes (ni trop élevée, ni trop faible)

if __name__ == '__main__':
    unittest.main()