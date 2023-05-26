import sys
import Club
import Championnat
from Creation_BDD import creation_bdd, copie_bdd

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QLabel, QTabWidget


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
        self.w = VisuComplet(self.champ)
        self.w.show()


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
            self.texte_club(c.nom)  # Création du contenu de la page associée à l'onglet
            tab = QLabel(self.texte)  # Affichage du contenu dans la page associée à l'onglet
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
        f.close()


class VisuComplet(QMainWindow):
    """
    Classe définissant la fenêtre affichée après la simulation du match.
    """
    def __init__(self, championnat):
        super().__init__()
        self.setWindowTitle("Visualisation finale")
        self.setMinimumSize(700, 300)
        self.champ = championnat
        self.resultats_txt = ""
        self.resume_txt = ""
        self.club_txt = ""

        # Création des onglets de navigation
        tabs = QTabWidget()

        # Onglet des résultats du championnat
        self.resultats()  # Création du texte à afficher pour les résultats
        tab1 = QLabel(self.resultats_txt)
        tabs.addTab(tab1, "Résultats")

        # Onglet des résumés des matchs
        tab2 = self.resumeMatchTab()
        tabs.addTab(tab2, "Résumé des matchs")

        # Onglet des classements des joueurs
        tab3 = self.classementJoueurTab()
        tabs.addTab(tab3, "Classement des joueurs")

        # Onglet des fiches des clubs
        tab4 = self.visuClubsTab()
        tabs.addTab(tab4, "Visualiser les clubs")

        self.setCentralWidget(tabs)

    def resultats(self):
        """
        Méthode permettant d'afficher les résultats finaux du championnat.
        """
        f = open("C:\WorkspacePython\LeFoot\Fichiers\\fichier des scores finaux.txt", 'rt')
        self.resultats_txt += f.read()
        f.close()

    def resumeMatchTab(self):
        resumeMatch = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Résumé des matchs"))
        resumeMatch.setLayout(layout)
        return resumeMatch

    def classementJoueurTab(self):
        classementJoueur = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Classement des Joueurs"))
        classementJoueur.setLayout(layout)
        return classementJoueur

    def visuClubsTab(self):
        """
        Méthode définissant l'affichage des fiches des clubs.
        """
        visuClubs = QWidget()  # Création du widget correspondant à la visualisation des fiches
        # On crée un layout pour disposer les boutons et un second pour contenir les fiches des clubs stackées les unes
        # sur les autres.
        # On crée un troisième layout qui contiendra les deux premiers.
        layout = QHBoxLayout()
        bouton_layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()
        bouton_layout.setContentsMargins(0, 0, 30, 0)
        # On ajoute les layouts des boutons et des fiches au layout principal.
        layout.addLayout(bouton_layout)
        layout.addLayout(self.stacked_layout)
        # Création des boutons, un par club.
        for i, c in enumerate(self.champ.clubs):
            btn = QPushButton(c.nom)
            # On lie tous les boutons à un signal permettant de changer d'onglet actif.
            if i == 0:
                btn.pressed.connect(self.activate_tab_0)
            elif i == 1:
                btn.pressed.connect(self.activate_tab_1)
            elif i == 2:
                btn.pressed.connect(self.activate_tab_2)
            elif i == 3:
                btn.pressed.connect(self.activate_tab_3)
            elif i == 4:
                btn.pressed.connect(self.activate_tab_4)
            elif i == 5:
                btn.pressed.connect(self.activate_tab_5)
            elif i == 6:
                btn.pressed.connect(self.activate_tab_6)
            elif i == 7:
                btn.pressed.connect(self.activate_tab_7)
            bouton_layout.addWidget(btn)  # Ajout des boutons au layout correspondant
            self.texte_club(c.nom)  # Création du texte à afficher pour la fiche du club
            self.stacked_layout.addWidget(QLabel(self.club_txt))  # Ajout de la fiche au layout stacké
        # Définition du layout de notre widget
        visuClubs.setLayout(layout)
        return visuClubs

    def activate_tab_0(self):
        self.stacked_layout.setCurrentIndex(0)

    def activate_tab_1(self):
        self.stacked_layout.setCurrentIndex(1)

    def activate_tab_2(self):
        self.stacked_layout.setCurrentIndex(2)

    def activate_tab_3(self):
        self.stacked_layout.setCurrentIndex(3)

    def activate_tab_4(self):
        self.stacked_layout.setCurrentIndex(4)

    def activate_tab_5(self):
        self.stacked_layout.setCurrentIndex(5)

    def activate_tab_6(self):
        self.stacked_layout.setCurrentIndex(6)

    def activate_tab_7(self):
        self.stacked_layout.setCurrentIndex(7)

    def texte_club(self, nom):
        """
        Méthode permettant d'afficher les données contenues dans les fiches des clubs.

        nom : nom du club dont les données doivent être affichées.
        """
        self.club_txt = ""  # Effacement de ce qui était précédemment écrit dans la variable self.club_txt
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {nom}.txt", 'rt')  # Lecture du fichier
        self.club_txt += f.read()  # Écriture dans la variable
        f.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()