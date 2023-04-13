import numpy as np
import random as rd

class Journee():
    """
    Classe contenant les informations d'une journée de match.
    """
    def __init__(self, num, championnat):
        self.num = num
        self.matchs = []
        self.clubs_complet = championnat.clubs.copy()  # liste contenant tous les clubs participant au championnat
        self.clubs = championnat.clubs.copy()  # Liste contenant les clubs n'ayant pas encore joué sur la journée


    def __str__(self):
        return f"Journée n°{self.num}"


    def match(self):
        """
        Fonction permettant le déroulement d'un match
        """
        c1 = self.clubs.pop()  # On récupère le dernier club de la liste tout en le retirant de celle-ci
        match_realise = False
        i = 0
        but_c1 = 0
        but_c2 = 0
        # On crée différentes listes permettront de faire des tirages aléatoires.
        l1 = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5]
        l2 = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5]
        l3 = [0, 1, 1, 2, 2, 3]
        l4 = [0, 1, 1, 2, 2, 3]
        # On mélange les listes précédentes pour mettre en place l'aléatoire.
        l1_s = rd.sample(l1, len(l1))
        l2_s = rd.sample(l2, len(l2))
        l3_s = rd.sample(l3, len(l3))
        l4_s = rd.sample(l4, len(l4))
        print(l1_s, l2_s, l3_s, l4_s)  # Debug

        # On cherche le club qui affrontera c1.
        while match_realise == False:
            c2 = self.clubs[i]
            if c2 not in c1.match_realise_dom:  # On vérifie que c1 n'a pas accueilli c2 à domicile
                del self.clubs[i]
                c1.ajout_match_realise(c2, "dom")
                c2.ajout_match_realise(c1, "ext")
                match_realise = True
                dom_c1 = 1
                dom_c2 = 0
                print(f"{c1} joue à domicile contre {c2}")
            elif c2 not in c1.match_realise_ext: # On vérifie que c2 n'a pas accueilli c1 à domicile
                del self.clubs[i]
                c1.ajout_match_realise(c2, "ext")
                c2.ajout_match_realise(c1, "dom")
                match_realise = True
                dom_c1 = 0
                dom_c2 = 1
                print(f"{c2} joue à domicile contre {c1}")
            else:
                i += 1

        # On affiche les notes des clubs juste pour vérifier (Debug).
        c1.calcul_note_club()
        c2.calcul_note_club()
        diff_note = c1.note_club - c2.note_club  # On calcul l'écart de note entre les clubs
        print(diff_note)  # Debug
        # On détermine le nb d'actions qu'auront chaques clubs en fonction de tirages aléatoires, de la différence
        # et du caractère à domicile ou à l'extérieur de la rencontre.
        nb_act_c1 = l1_s[0] + round(diff_note * l3_s[0] * 0.1) + dom_c1 * rd.randint(0,2)
        nb_act_c2 = l2_s[0] - round(diff_note * l4_s[0] * 0.1) + dom_c2 * rd.randint(0,2)
        print(f"{c1} va avoir {nb_act_c1} actions.")
        print(f"{c2} va avoir {nb_act_c2} actions.")
        #print(f"dom_c1 = {dom_c1}")  # Debug
        #print(f"dom_c2 = {dom_c2}")
        print("")

        print(f"# Phase d'action de {c1} :")
        print("")
        # On détermine l'issue des actions de c1.
        for i in range(nb_act_c1):
            act = self.action(c1, c2, dom_c1, dom_c2)
            if act == 1:
                but_c1 += 1  # On met à jour le nombre de buts de c1 dans ce match
                c1.nb_buts += 1  # On met à jour le nombre de buts totaux de c1 dans le championnat
        print(f"# Phase d'action de {c2} :")
        print("")
        # On détermine l'issue des actions de c2.
        for i in range(nb_act_c2):
            act = self.action(c2, c1, dom_c2, dom_c1)
            if act == 1:
                but_c2 += 1  # On met à jour le nombre de buts de c2 dans ce match
                c2.nb_buts += 1  # On met à jour le nombre de buts totaux de c2 dans le championnat

        # On détermine l'issue du match et on attribue les points en conséquence.
        if but_c1 > but_c2:
            c1.victoire()
            print(f"{c1} remporte le match contre {c2} avec un score de {but_c1} - {but_c2}.")
            print("----------------------------------------------------------------------------")
        elif but_c1 < but_c2:
            c2.victoire()
            print(f"{c2} remporte le match contre {c1} avec un score de {but_c2} - {but_c1}.")
            print("----------------------------------------------------------------------------")
        else:
            c1.nul()
            c2.nul()
            print(f"{c1} et {c2} font un match nul avec {but_c1} partout.")
            print("----------------------------------------------------------------------------")


    def action(self, c1, c2, dom_c1, dom_c2):
        """
        Fonction qui simule une action de c1 contre c2

        c1 : club en attaque
        c2 : club en défense
        dom_c1 : domc1=1 si c1 est à domicile
        dom_c2 : domc2=1 si c2 est à domicile
        """
        note_att = 0
        note_def = 0
        # On détermine la note d'attaque de c1 et celle de défense de c2.
        # Les milieux participent au calcul des deux notes, mais avec un poids moindre.
        for j in c1.joueurs:
            if j.poste == "Attaquant":
                note_att += j.note
            elif j.poste == "Milieu":
                note_att += 0.5*j.note
        for j in c2.joueurs:
            if j.poste == "Défenseur":
                note_def += j.note
            elif j.poste == "Milieu":
                note_def += 0.5*j.note
        # Affichage des notes (debug).
        print(f"Note attaque {c1} = {note_att}")
        print(f"Note défense {c2} = {note_def}")
        # On randomise ces notes en déterminant une puissance d'attaque et de défense.
        puis_att = note_att * rd.random()
        puis_def = note_def * rd.random()
        # Affichage des puissances (debug).
        print(f"Puissance attaque {c1} = {puis_att}")
        print(f"Puissance défense {c2} = {puis_def}")

        # On détermine l'issue de l'action.
        if puis_att > puis_def:
            print(f"--> {c1} perce la défense de {c2}")
            # On choisit un joueur au hasard pour effectuer le tir final.
            i = rd.randint(0,10)
            j = c1.joueurs[i]
            gardien = c2.joueurs[3]  # On sélectionne le gardien de l'équipe en défense
            # Tant que le joueur sélectionné n'est pas un attaquant, on en sélectionne un autre.
            while j.poste != "Attaquant":
                i = rd.randint(0,10)
                j = c1.joueurs[i]
            # On détermine les notes de frappes et d'arrêt en fonction des notes de l'attaquant et du gardien ainsi
            # que de la ferveur des supporters (domicile/extérieur).
            note_frappe = j.note * rd.random() + dom_c1 * 10
            note_arret = gardien.note * rd.random() + dom_c2 * 10
            # Affichage des notes (debug).
            print("note_frappe :", note_frappe)
            print("note_arret :", note_arret)

            # On détermine l'issue du tir.
            if note_frappe > note_arret:
                print(f"===> {j.nom} marque un but pour {c1} !")
                print("- - - - - - - -")
                return 1
            else:
                print(f"===> {gardien.nom} arrête le tir de {j.nom}")
                print("- - - - - - - -")
                return 0

        else:
            print(f"--> La défense de {c2} parvient à repousser l'offensive de {c1}")
            print("- - - - - - - -")


    def score_journee(self):
        """
        Fonction affichant le score de l'équipe sur une journée.
        """
        for c in self.clubs_complet:
            print(f"{c} termine la journée {self.num} avec un score de {c.score}")


    def deroulement(self):
        """
        Fonction simulant le déroulement d'une journée
        """
        while len(self.clubs) > 0:
            self.match()
        self.score_journee()