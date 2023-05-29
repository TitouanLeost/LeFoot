import sys
import Club
import Championnat
from Creation_BDD import creation_bdd, copie_bdd

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QStackedLayout, QWidget, QLabel, QTabWidget, QStackedWidget, QScrollArea)


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
        self.hide()


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
        self.resume_txt = ""
        self.club_txt = ""
        self.index_journee = 0
        self.index_match = 0
        self.index_details = 0

        # Création des onglets de navigation
        tabs = QTabWidget()

        # Onglet des résultats du championnat
        tab1 = self.resultatsTab()
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

        # Onglet des analyses du championnat
        tab5 = self.analysesTab()
        tabs.addTab(tab5, "Analyses")

        self.setCentralWidget(tabs)

    # Onglet des résultats.
    def resultatsTab(self):
        """
        Méthode permettant de générer l'onglet des résultats.
        """
        fenetre = QWidget()  # Création du widget correspondant à la visualisation des résultats
        layout = QVBoxLayout()  # Création du layout de la page
        self.stacked_layout_r = QStackedLayout()  # Création d'un layout pour empiler les résultats des journées
        label = QLabel(f"------==== CLASSEMENT FINAL DE {self.champ.nom} ====------")
        label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label)
        tableau = self.resultats_journee(14)  # Création du tableau des scores final
        layout.addWidget(tableau)  # Ajout du tableau au layout
        layout.addSpacing(30)
        selection = QComboBox()  # Création d'une boite de sélection pour les résultats de chaques journées
        for i in range(1, len(self.champ.journees_liste)):
            selection.addItem(f"Journée {i}")
            tableau = self.resultats_journee(i)  # Création du tableau des scores de la journée
            self.stacked_layout_r.addWidget(tableau)
        selection.currentIndexChanged.connect(self.index_resultats)
        layout.addWidget(selection)  # Ajout de la boite de sélection au layout
        layout.addLayout(self.stacked_layout_r)  # Ajout des tableaux des scores par journées au layout
        fenetre.setLayout(layout)  # Définition du layout de la fenêtre
        return fenetre


    def resultats_journee(self, num):
        """
        Méthode permettant d'afficher les résultats de la journée correspondante.

        num : numéro de la journée correspondant aux résultats.
        """
        resultats = QWidget()
        layout = QHBoxLayout()
        classement = open(f"C:\WorkspacePython\LeFoot\Fichiers\\classement clubs journée {num}.txt", 'rt')
        nom = open(f"C:\WorkspacePython\LeFoot\Fichiers\\nom clubs journée {num}.txt", 'rt')
        victoires = open(f"C:\WorkspacePython\LeFoot\Fichiers\\victoires clubs journée {num}.txt", 'rt')
        defaites = open(f"C:\WorkspacePython\LeFoot\Fichiers\\défaites clubs journée {num}.txt", 'rt')
        nuls = open(f"C:\WorkspacePython\LeFoot\Fichiers\\nuls clubs journée {num}.txt", 'rt')
        buts = open(f"C:\WorkspacePython\LeFoot\Fichiers\\buts clubs journée {num}.txt", 'rt')
        encaisses = open(f"C:\WorkspacePython\LeFoot\Fichiers\\encaissés clubs journée {num}.txt", 'rt')
        points = open(f"C:\WorkspacePython\LeFoot\Fichiers\\points clubs journée {num}.txt", 'rt')
        labels = []
        label_c = QLabel(classement.read())
        label_nom = QLabel(nom.read())
        label_v = QLabel(victoires.read())
        label_d = QLabel(defaites.read())
        label_nuls = QLabel(nuls.read())
        label_b = QLabel(buts.read())
        label_e = QLabel(encaisses.read())
        label_p = QLabel(points.read())
        labels.append(label_c)
        labels.append(label_nom)
        labels.append(label_v)
        labels.append(label_d)
        labels.append(label_nuls)
        labels.append(label_b)
        labels.append(label_e)
        labels.append(label_p)
        for l in labels:
            l.setContentsMargins(0, 0, 20, 0)
            l.setAlignment(Qt.AlignTop)
            layout.addWidget(l)
        layout.addStretch(1)  # On compacte l'affichage sur la gauche de l'écran
        layout.setContentsMargins(10, 10, 0, 0)
        resultats.setLayout(layout)
        classement.close()
        nom.close()
        victoires.close()
        defaites.close()
        nuls.close()
        buts.close()
        encaisses.close()
        points.close()
        return resultats

    def index_resultats(self, i):
        self.stacked_layout_r.setCurrentIndex(i)

    # Onglet des résumés des matchs.
    def resumeMatchTab(self):
        """
        Méthode permettant d'afficher les résumés des matchs dans un onglet.
        """
        resumeMatch = QWidget()  # Création du widget correspondant à la visualisation des résumés
        # Création d'un layout contenant les QComboBox, d'un second contenant l'affichage des résumés stackés et d'un
        # troisième contenant les deux premiers.
        layout = QVBoxLayout()
        bouton_layout = QHBoxLayout()
        self.stacked_layout_m = QStackedLayout()
        # Ajout des layouts des QComboBox et de l'affichage au layout principal.
        layout.addLayout(bouton_layout)
        layout.addLayout(self.stacked_layout_m)
        # Création des widgets participants à l'affichage.
        selection_journee = QComboBox()  # QComboBox permettant de sélectionner la journée
        self.selection_match_stack = QStackedWidget()  # Création d'un stack de widget pour la sélection des matchs
        selection_journee.setFixedHeight(30)
        self.selection_match_stack.setFixedHeight(30)

        # Ajout des items dans les boites de sélection de la journée et du match.
        for i, j in enumerate(self.champ.journees_liste, start=1):
            selection_journee.addItem(f"Journée {i}")
            selection_match = QComboBox()  # Création d'une QComboBox pour tous les matchs d'une journée
            # Ajout des matchs de la journée en cours dans la QComboBox.
            for m in j.matchs:
                selection_match.addItem(f"{m[0].nom} - {m[1].nom}")
                self.texte_resume_match(m[0], m[1], i)  # Création du texte du résumé du match
                label = ScrollLabel(self)
                label.setText(self.resume_txt)
                label.setContentsMargins(20, 15, 0, 0)
                label.setAlignment(Qt.AlignTop)
                self.stacked_layout_m.addWidget(label)  # Ajout du résumé à l'affichage stacké
                self.texte_details_match(m[0], m[1], i)  # Création du texte du résumé détaillé du match
                label = ScrollLabel(self)
                label.setText(self.resume_txt)
                label.setContentsMargins(20, 15, 0, 0)
                label.setAlignment(Qt.AlignTop)
                self.stacked_layout_m.addWidget(label)  # Ajout du résumé détaillé à l'affichage stacké
            self.selection_match_stack.addWidget(selection_match)  # Ajout de la QComboBox des matchs au stack de widget
            # Sélection de l'affichage correspondant au match choisi dans la seconde boite de sélection.
            selection_match.currentIndexChanged.connect(self.match_index_changed)
        selection_details = QComboBox()
        selection_details.addItem("Résumé")
        selection_details.addItem("Détails")
        selection_details.setFixedHeight(30)
        selection_details.currentIndexChanged.connect(self.details_index_changed)

        # Sélection de la QComboBox des matchs correspondant à la journée sélectionné dans la première boite de
        # sélection.
        selection_journee.currentIndexChanged.connect(self.journee_index_changed)
        # Ajout des deux boites de sélection au layout correspondant.
        bouton_layout.addWidget(selection_journee)
        bouton_layout.addWidget(self.selection_match_stack)
        bouton_layout.addWidget(selection_details)
        # Définition du layout de notre widget.
        resumeMatch.setLayout(layout)
        return resumeMatch

    def journee_index_changed(self, i):
        self.index_journee = i
        self.index_match = 0
        self.selection_match_stack.setCurrentIndex(i)
        self.stacked_layout_m.setCurrentIndex(8 * i + 2 * self.index_match + self.index_details)

    def match_index_changed(self, i):
        self.index_match = i
        self.stacked_layout_m.setCurrentIndex(8 * self.index_journee + 2 * i + self.index_details)

    def details_index_changed(self, i):
        self.index_details = i
        self.stacked_layout_m.setCurrentIndex(8 * self.index_journee + 2 * self.index_match + i)

    def texte_resume_match(self, c1, c2, num):
        """
        Méthode permettant d'afficher le résumé du match ayant opposé les clubs c1 et c2.

        c1 : club ayant jué à domicile.
        c2 : club ayant joué à l'extérieur.
        num : numéro de la journée à laquelle s'est déroulé le match.
        """
        self.resume_txt = ""  # Effacement de ce qui était précédemment écrit dans la variable self.club_txt
        # Lecture du fichier.
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\Journée {num}, match {c1.nom}-{c2.nom}.txt", 'rt')
        self.resume_txt += f.read()  # Écriture dans la variable
        f.close()

    def texte_details_match(self, c1, c2, num):
        """
        Méthode permettant d'afficher le résumé du match ayant opposé les clubs c1 et c2.

        c1 : club ayant jué à domicile.
        c2 : club ayant joué à l'extérieur.
        num : numéro de la journée à laquelle s'est déroulé le match.
        """
        self.resume_txt = ""  # Effacement de ce qui était précédemment écrit dans la variable self.club_txt
        # Lecture du fichier.
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\Journée {num}, match détaillé {c1.nom}-{c2.nom}.html", 'rt')
        self.resume_txt += f.read()  # Écriture dans la variable
        f.close()

    # Onglet des classements des joueurs.
    def classementJoueurTab(self):
        """
        Méthode permettant d'afficher les classements des joueurs.
        """
        classementJoueur = QWidget()
        # On crée un layout pour disposer les boutons et un second pour contenir les fiches des clubs stackées les unes
        # sur les autres.
        # On crée un troisième layout qui contiendra les deux premiers.
        layout = QVBoxLayout()
        bouton_layout = QHBoxLayout()
        self.stacked_layout_cla = QStackedLayout()
        # On ajoute les layouts des boutons et des fiches au layout principal.
        layout.addLayout(bouton_layout)
        layout.addLayout(self.stacked_layout_cla)
        # Création des boutons.
        btn = QPushButton("Buteurs")
        btn.pressed.connect(self.activate_buteurs)
        bouton_layout.addWidget(btn)
        btn = QPushButton("Gardiens")
        btn.pressed.connect(self.activate_gardiens)
        bouton_layout.addWidget(btn)
        # Création de l'affichage des classements.
        self.stacked_layout_cla.addWidget(self.classement_poste("buteurs"))
        self.stacked_layout_cla.addWidget(self.classement_poste("gardiens"))
        classementJoueur.setLayout(layout)
        return classementJoueur

    def activate_buteurs(self):
        self.stacked_layout_cla.setCurrentIndex(0)

    def activate_gardiens(self):
        self.stacked_layout_cla.setCurrentIndex(1)

    def classement_poste(self, poste):
        """
        Méthode permettant de générer l'affichage en colonne des classements des buteurs ou des gardiens.

        poste : "buteurs" ou "gardiens".
        """
        widget = QWidget()
        # Création d'un affichage en colonne
        layout = QHBoxLayout()
        classement = open(f"C:\WorkspacePython\LeFoot\Fichiers\\classement {poste}.txt", 'rt')
        nom = open(f"C:\WorkspacePython\LeFoot\Fichiers\\nom {poste}.txt", 'rt')
        club = open(f"C:\WorkspacePython\LeFoot\Fichiers\\club {poste}.txt", 'rt')
        if poste == "buteurs":
            buts = open(f"C:\WorkspacePython\LeFoot\Fichiers\\buts {poste}.txt", 'rt')
        else:
            buts = open(f"C:\WorkspacePython\LeFoot\Fichiers\\arrets {poste}.txt", 'rt')
        labels = []
        label_cla = QLabel(classement.read())
        label_n = QLabel(nom.read())
        label_clu = QLabel(club.read())
        label_b = QLabel(buts.read())
        labels.append(label_cla)
        labels.append(label_n)
        labels.append(label_clu)
        labels.append(label_b)
        for l in labels:
            l.setContentsMargins(0, 0, 40, 0)
            l.setAlignment(Qt.AlignTop)
            layout.addWidget(l)
        layout.addStretch(1)  # On compacte l'affichage sur la gauche de l'écran
        widget.setLayout(layout)
        classement.close()
        nom.close()
        club.close()
        buts.close()
        return widget

    # Onglet de visualisation des clubs.
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
        self.stacked_layout_c = QStackedLayout()
        layout.setContentsMargins(10, 20, 0, 0)
        bouton_layout.setContentsMargins(0, 0, 30, 0)
        # On ajoute les layouts des boutons et des fiches au layout principal.
        layout.addLayout(bouton_layout)
        layout.addLayout(self.stacked_layout_c)
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
            label = QLabel(self.club_txt)
            label.setAlignment(Qt.AlignTop)
            self.stacked_layout_c.addWidget(label)  # Ajout de la fiche au layout stacké
        bouton_layout.addStretch(1)
        # Définition du layout de notre widget
        visuClubs.setLayout(layout)
        return visuClubs

    def activate_tab_0(self):
        self.stacked_layout_c.setCurrentIndex(0)

    def activate_tab_1(self):
        self.stacked_layout_c.setCurrentIndex(1)

    def activate_tab_2(self):
        self.stacked_layout_c.setCurrentIndex(2)

    def activate_tab_3(self):
        self.stacked_layout_c.setCurrentIndex(3)

    def activate_tab_4(self):
        self.stacked_layout_c.setCurrentIndex(4)

    def activate_tab_5(self):
        self.stacked_layout_c.setCurrentIndex(5)

    def activate_tab_6(self):
        self.stacked_layout_c.setCurrentIndex(6)

    def activate_tab_7(self):
        self.stacked_layout_c.setCurrentIndex(7)

    def texte_club(self, nom):
        """
        Méthode permettant d'afficher les données contenues dans les fiches des clubs.

        nom : nom du club dont les données doivent être affichées.
        """
        self.club_txt = ""  # Effacement de ce qui était précédemment écrit dans la variable self.club_txt
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\fiche de {nom}.txt", 'rt')  # Lecture du fichier
        self.club_txt += f.read()  # Écriture dans la variable
        f.close()

    def analysesTab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        g = self.champ.donnees_analyse[0][0]
        a = self.champ.donnees_analyse[1][0]
        c1 = self.champ.donnees_analyse[2][0]
        c2 = self.champ.donnees_analyse[3][0]
        label = QLabel(f"<b><u>Le gardien le plus efficace :</u> {g.prenom[0]}.{g.nom}</b> ({g.club}) avec "
                       f"<b>{g.efficacite * 100:.1f}%</b> de tirs arrêtés")
        layout.addWidget(label)
        label = QLabel(f"<b><u>L'attaquant le plus efficace :</u> {a.prenom[0]}.{a.nom}</b> ({a.club}) avec "
                       f"<b>{a.efficacite * 100:.1f}%</b> de tirs marqués")
        layout.addWidget(label)
        label = QLabel(f"<b><u>La meilleur club en attaque :</u> <font color={c1.couleur}>{c1.nom}</font></b> avec "
                       f"<b>{self.champ.donnees_analyse[2][1]}</b> attaques réussies")
        layout.addWidget(label)
        label = QLabel(f"<b><u>La meilleur club en défense :</u> <font color={c2.couleur}>{c2.nom}</font></b> avec "
                       f"<b>{self.champ.donnees_analyse[3][1]}</b> défenses réussies")
        layout.addWidget(label)

        widget.setLayout(layout)
        return widget


class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()