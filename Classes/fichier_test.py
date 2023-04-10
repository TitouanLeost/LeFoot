from Joueur import *
import Club
import Journée
import Championnat


# lefoot = Club.Club("lefoot", "Didier")
# oui = Club.Club("oui", "Marcel")
# J1 = Attaquant("Bob", 95, lefoot)
# J2 = Gardien("Jean Claude", 20, lefoot)
# J3 = Milieu("Micheline", 32, lefoot)
# print(J1)
# print(J2)
# print(J3)
# print(J1.note)
# print(J3.poste)
# print(J2.nom)
# print(lefoot.nom, lefoot.entraineur)
# lefoot.remplissage([J1,J2,J3])
# lefoot.liste_joueurs()
# lefoot.note_club()
# oui.note_club()

sb = Club.Club("Stade Brestois", "Philippe")
sr = Club.Club("Stade Rennais", "Catherine")

A1 = Attaquant("Kévin", 72, sb)
A2 = Attaquant("Kevine", 83, sb)
A3 = Attaquant("Keveen", 64, sb)
A4 = Attaquant("Paul", 26, sr)
A5 = Attaquant("Pol", 74, sr)
A6 = Attaquant("Paulo", 98, sr)

G1 = Gardien("Timothée", 100, sb)
G2 = Gardien("Didier", 88, sr)

D1 = Defenseur("Philippe", 63, sb)
D2 = Defenseur("Philipe", 73, sb)
D3 = Defenseur("filipe", 35, sb)
D4 = Defenseur("Patrick", 77, sr)
D5 = Defenseur("Patrique", 89, sr)
D6 = Defenseur("Pastric", 92, sr)

M1 = Milieu("Michel", 57, sb)
M2 = Milieu("Michelle", 82, sb)
M3 = Milieu("Micheleu", 75, sb)
M4 = Milieu("Mishell", 80, sb)
M5 = Milieu("Jean", 63, sr)
M6 = Milieu("Jan", 92, sr)
M7 = Milieu("Gean", 78, sr)
M8 = Milieu("Jhan", 38, sr)

sb.remplissage([A1,A2,A3,G1,D1,D2,D3,M1,M2,M3,M4])
sr.remplissage([A4,A5,A6,G2,D4,D5,D6,M5,M6,M7,M8])

sb.liste_joueurs()
sb.note_club()
print("-----------------------------------")
sr.liste_joueurs()
sr.note_club()
print("-----------------------------------")

ligue1 = Championnat.Championnat("ligue 1")
ligue1.remplissage([sb, sr])

j1 = Journée.Journee(1, ligue1)

print(sb.score)
print(sr.score)

j1.match()

print(sb.score)
print(sr.score)