import sys
import Club
import Championnat
from Creation_BDD import creation_bdd, copie_bdd

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTabWidget


class MainWindow(QMainWindow):
    """
    Classe définissant la fenêtre principale de l'interface.
    """
    def __init__(self):
        super().__init__()
        self.champ = None  # Variable d'instance permettant de stocker le championnat
        self.w = None  # Variable d'instance permettant de stocker une autre fenêtre
        self.setWindowTitle("LeFoot")
        self.setMinimumSize(QSize(500, 400))

        layout = QVBoxLayout()  # On définit un affichage vertical

        # Mise en place du bouton permettant de créer le championnat.
        bouton_creer = QPushButton("Mise en place du championnat")
        layout.addWidget(bouton_creer)
        bouton_creer.clicked.connect(self.clique_bouton_creer)
        # Mise en place du bouton permettant de visualiser les fiches des clubs.
        self.bouton_visu = QPushButton("Visualiser les clubs")
        layout.addWidget(self.bouton_visu)
        self.bouton_visu.clicked.connect(self.clique_bouton_visu)
        self.bouton_visu.setDisabled(True)
        # Mise en place du bouton permettant de lancer la simulation.
        self.bouton_simu = QPushButton("Simuler")
        layout.addWidget(self.bouton_simu)
        self.bouton_simu.clicked.connect(self.clique_bouton_simu)
        self.bouton_simu.setDisabled(True)

        # On crée un widget permettant d'afficher les boutons
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def clique_bouton_creer(self):
        """
        Méthode déclenchée par l'appui sur le bouton "Mise en place du championnat". Elle permet de créer les clubs
        et le championnat.
        """
        # Création des différents clubs
        sb = Club.Club("Stade Brestois 29", "Philippe")
        sr = Club.Club("Stade Rennais FC", "Catherine")
        se = Club.Club("AS Saint-Etienne", "Etienne")
        gu = Club.Club("En Avant Guingamp", "Joel")
        fs = Club.Club("FC Silmi", "Félix")
        cc = Club.Club("Cagliari Calcio", "Charlie")
        sc = Club.Club("SM Caen", "Jacob")
        rl = Club.Club("RC Lens", "Simone")
        self.champ = Championnat.Championnat("ligue 1", [sb, sr, se, gu, fs, cc, sc, rl])  # Création du championnat
        self.champ.remplissage(True)  # Remplissage des effectifs des clubs
        self.champ.creation_fiche_clubs(False)  # Création des fiches des clubs
        # On active les boutons "Visualiser les clubs" et "Simuler".
        self.bouton_visu.setDisabled(False)
        self.bouton_simu.setDisabled(False)
        print("Création Ok")  # Debug

    def clique_bouton_visu(self):
        """
        Méthode déclenchée par l'appui sur le bouton "Visualiser les clubs". Elle permet d'ouvrir une nouvelle
        fenêtre qui contient l'affichage des fiches des clubs.
        """
        self.w = VisuClubs(self.champ.clubs)  # Création de la fenêtre
        self.w.show()  # Affichage de la fenêtre
        print("Visu Ok")  # Debug

    def clique_bouton_simu(self):
        """
        Méthode déclenchée par l'appui sur le bouton "Simuler". Elle permet de lancer la simulation.
        """
        self.champ.simuler()  # Simulation
        self.champ.creation_fiche_clubs()  # Enregistrement des données des clubs dans des fichiers texte
        print("Simulation OK")  # Debug


class VisuClubs(QMainWindow):
    """
    Classe définissant la fenêtre contenant les informations relatives aux clubs
    """
    def __init__(self, liste_clubs):
        super().__init__()
        self.setWindowTitle("Visualisation des clubs")
        self.setMinimumSize(1200, 100)
        self.texte = ""
        self.clubs = liste_clubs  # On enregistre la liste des clubs dans une variable d'instance

        # Création des onglets de navigation de chaque club.
        tabs = QTabWidget()
        for c in self.clubs:
            self.texte_club(c.nom)
            tab = QLabel(self.texte)
            tabs.addTab(tab, c.nom)

        self.setCentralWidget(tabs)

    def texte_club(self, nom):
        """
        Méthode permettant d'afficher les données contenues dans les fiches des clubs.

        nom : nom du club dont les données doivent être affichées.
        """
        self.texte = ""  # Effacement de ce qui était précédemment écrit dans la variable self.texte
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {nom}.txt", 'rt')  # Lecture du fichier
        self.texte += f.read()  # Écriture dans la variable



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()