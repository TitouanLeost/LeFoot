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
        self.assertTrue(noteC.note_club<85 and noteC.note_club>55) #on regarde si les notes des clubs sont réalistes (ni trop élevée, ni trop faible)

if __name__ == '__main__':
    unittest.main()