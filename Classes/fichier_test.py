import Club
import Championnat
from Creation_BDD import creation_bdd, copie_bdd

# Création des clubs
sb = Club.Club("Stade Brestois 29", "Philippe")
sr = Club.Club("Stade Rennais FC", "Catherine")
se = Club.Club("AS Saint-Etienne", "Etienne")
gu = Club.Club("En Avant Guingamp", "Joel")
fs = Club.Club("FC Silmi", "Félix")
cc = Club.Club("Cagliari Calcio", "Charlie")
sc = Club.Club("SM Caen", "Jacob")
rl = Club.Club("RC Lens", "Simone")

# Lancement de la simulation
#creation_bdd()  # Création de la bdd
copie_bdd()  # Re remplissage de la table joueurs_reserve
ligue1 = Championnat.Championnat("ligue 1", [sb, sr, se, gu, fs, cc, sc, rl])  # Création du championnat
ligue1.simuler()  # Simulation
ligue1.creation_fiche_clubs()  # Enregistrement des données des clubs dans des fichiers texte

