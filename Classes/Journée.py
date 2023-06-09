import random as rd

class Journee():
    """
    Classe contenant les informations d'une journée de match.
    """
    def __init__(self, num, championnat):
        self.num = num
        self.matchs = []
        self.clubs_complet = championnat.liste_clubs.copy()  # liste contenant tous les clubs participant au championnat
        self.clubs = championnat.liste_clubs.copy()  # Liste contenant les clubs n'ayant pas encore joué sur la journée
        self.joueurs_cartons = []  # Liste contenant les joueurs ayant reçu un carton lors d'un match
        self.joueurs_blessures = []  # Liste contenant les joueurs s'étant blessé lors d'un match

    def __str__(self):
        return f"Journée n°{self.num}"

    def match(self):
        """
        Méthode permettant de simuler le déroulement d'un match.
        """
        c1 = self.clubs.pop()  # On récupère le dernier club de la liste tout en le retirant de celle-ci
        match_realise = False
        i = 0
        but_c1 = 0
        but_c2 = 0
        liste_buteurs = []
        liste_arrets = []
        self.joueurs_cartons = []  # On réinitialise la liste
        self.joueurs_blessures = []  # On réinitialise la liste
        # On crée différentes listes qui permettront de faire des tirages aléatoires.
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
        while not match_realise:
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
            else:  # Si c1 et c2 ont déjà fait leurs deux rencontres, on passe au club suivant
                i += 1

        # On prépare l'enregistrement en détail du match
        if dom_c1 == 1:  # Si c1 est à domicile
            self.matchs.append([c1, c2])
            f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\"
                     f"Journée {self.num}, match détaillé {c1.nom}-{c2.nom}.html", 'wt')  # titouan
            # f = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\"
            #          f"Journée {self.num}, match détaillé {c1.nom}-{c2.nom}.html", 'wt')  # hadrien
        else:  # Si c2 est à domicile
            self.matchs.append([c2, c1])
            f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\"
                     f"Journée {self.num}, match détaillé {c2.nom}-{c1.nom}.html", 'wt') # titouan
            # f = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\
            # Journée {self.num}, match détaillé {c2.nom}-{c1.nom}.html", 'wt')  # hadrien

        # On affiche les notes des équipes juste pour vérifier (Debug).
        c1.calcul_note_equipe()
        c2.calcul_note_equipe()
        diff_note = c1.note_equipe - c2.note_equipe  # On calcule l'écart de note entre les équipes
        print(diff_note)  # Debug
        # On détermine le nb d'actions qu'auront chaques clubs en fonction de tirages aléatoires, de la différence
        # et du caractère à domicile ou à l'extérieur de la rencontre.
        nb_act_c1 = max(l1_s[0] + round(diff_note * l3_s[0] * 0.1) + dom_c1 * rd.randint(0,2), 0)
        nb_act_c2 = max(l2_s[0] - round(diff_note * l4_s[0] * 0.1) + dom_c2 * rd.randint(0,2), 0)
        print(f"{c1} va avoir {nb_act_c1} actions.")
        print(f"{c2} va avoir {nb_act_c2} actions.")
        #print(f"dom_c1 = {dom_c1}")  # Debug
        #print(f"dom_c2 = {dom_c2}")
        print("")

        # Enregistrement de ces informations.
        f.write(f"L'équipe de <font color={c1.couleur}><b>{c1}</b></font> à une note de "
                f"<b><font color={c1.couleur}>{c1.note_equipe:.2f}</font></b>.<br>")
        f.write(f"L'équipe de <font color={c2.couleur}><b>{c2}</b></font> à une note de "
                f"<b><font color={c2.couleur}>{c2.note_equipe:.2f}</font></b>.<br>")
        f.write("<br>")
        f.write(f"<b>{c1}</b> va avoir <font color={c1.couleur}><b>{nb_act_c1} actions</b></font>.<br>")
        f.write(f"<b>{c2}</b> va avoir <font color={c2.couleur}><b>{nb_act_c2} actions</b></font>.<br>")
        f.write("<br>")

        # On met en place le déroulement des actions associées à la minute à laquelle elles se déroulent.
        liste_actions = []
        liste_temps = []
        for i in range(nb_act_c1):
            liste_actions.append("c1")
        for i in range(nb_act_c2):
            liste_actions.append("c2")
        # On crée une liste contenant les minutes de chaque action
        while len(liste_temps) < nb_act_c1 + nb_act_c2:
            tps = rd.randint(5, 90)
            if tps not in liste_temps:
                liste_temps.append(tps)
        rd.shuffle(liste_actions)  # On randomise l'ordre des actions de chaque équipe
        liste_temps.sort(reverse=True)  # On range la liste de temps dans l'ordre décroissant

        # On détermine l'issue des actions de chaque équipe.
        for a in liste_actions:
            t = liste_temps.pop()  # On récupère la minute à laquelle se déroule l'action
            if a == "c1":
                print(f"# Action de {c1} :")
                but, joueur, temps = self.action(c1, c2, dom_c1, dom_c2, t, f)  # On simule l'action
                if but == 1:
                    but_c1 += 1  # On met à jour le nombre de buts de c1 dans ce match
                    c1.nb_buts += 1  # On met à jour le nombre de buts totaux de c1 dans le championnat
                    c2.nb_buts_encaisses += 1  # On met à jour le nombre de buts encaissés par c2
                    liste_buteurs.append([joueur, temps])
                elif but == 0:
                    liste_arrets.append([joueur, temps])
            elif a == "c2":
                print(f"# Action de {c2} :")
                but, joueur, temps = self.action(c2, c1, dom_c2, dom_c1, t, f)  # On simule l'action
                if but == 1:
                    but_c2 += 1  # On met à jour le nombre de buts de c2 dans ce match
                    c2.nb_buts += 1  # On met à jour le nombre de buts totaux de c2 dans le championnat
                    c1.nb_buts_encaisses += 1  # On met à jour le nombre de buts encaissés par c1
                    liste_buteurs.append([joueur, temps])
                elif but == 0:
                    liste_arrets.append([joueur, temps])
                    print("joueur :", joueur)

        # On lance l'enregistrement du résumé du match.
        if dom_c1 == 1:
            self.resume_match_log(c1, c2, liste_buteurs, liste_arrets, but_c1, but_c2)
        else:
            self.resume_match_log(c2, c1, liste_buteurs, liste_arrets, but_c2, but_c1)

        # On détermine l'issue du match et on attribue les points en conséquence.
        if but_c1 > but_c2:
            c1.victoire()
            c2.nb_defaites += 1
            print(f"{c1} remporte le match contre {c2} avec un score de {but_c1} - {but_c2}.")
            print("----------------------------------------------------------------------------")
            f.write(f"<font color={c1.couleur}><b>{c1}</b></font> remporte le match contre "
                    f"<font color={c2.couleur}><b>{c2}</b></font> avec un score de <b>{but_c1} - {but_c2}</b>")
        elif but_c1 < but_c2:
            c2.victoire()
            c1.nb_defaites += 1
            print(f"{c2} remporte le match contre {c1} avec un score de {but_c2} - {but_c1}.")
            print("----------------------------------------------------------------------------")
            f.write(f"<font color={c2.couleur}><b>{c2}</b></font> remporte le match contre "
                    f"<font color={c1.couleur}><b>{c1}</b></font> avec un score de <b>{but_c2} - {but_c1}</b>")
        else:
            c1.nul()
            c2.nul()
            print(f"{c1} et {c2} font un match nul avec {but_c1} partout.")
            print("----------------------------------------------------------------------------")
            f.write(f"<font color={c1.couleur}><b>{c1}</b></font> et <font color={c2.couleur}><b>{c2}</b></font> "
                    f"font un match nul avec <b>{but_c1}</b> partout")

        # Mise à jour de la liste des scores
        c1.liste_score.append(c1.score)
        c2.liste_score.append(c2.score)

        f.close()

    def action(self, c1, c2, dom_c1, dom_c2, temps, f):
        """
        Méthode qui simule une action de c1 contre c2.

        c1 : club en attaque
        c2 : club en défense
        dom_c1 : domc1=1 si c1 est à domicile, 0 sinon
        dom_c2 : domc2=1 si c2 est à domicile, 0 sinon
        temps : minute à laquelle se déroule l'action
        f : fichier dans lequel on enregistre le déroulement détaillé des actions
        """
        f.write(f"<b>PHASE D'ACTION DE <font color={c1.couleur}>{c1.nom}</font></b> :<br>")

        note_att = 0
        note_def = 0
        # On détermine la note d'attaque de c1 et celle de défense de c2.
        # Les milieux participent au calcul des deux notes, mais avec un poids moindre.
        for j in c1.equipe:
            if j.poste == "Attaquant":
                note_att += j.note
            elif j.poste == "Milieu":
                note_att += 0.5*j.note
        for j in c2.equipe:
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

        # On enregistre ces données pour le détail du match.
        f.write(f"> Note attaque <b>{c1} = <font color={c1.couleur}>{note_att:.0f}</font></b><br>")
        f.write(f"----> Après randomisation : Puissance attaque <b>{c1} = "
                f"<font color={c1.couleur}>{puis_att:.0f}</font></b><br>")
        f.write(f"> Note défense <b>{c2} = <font color={c2.couleur}>{note_def:.0f}</font></b><br>")
        f.write(f"----> Après randomisation : Puissance défense <b>{c2} = "
                f"<font color={c2.couleur}>{puis_def:.0f}</font></b><br>")

        # On prend en compte la possibilité qu'un joueur se blesse et/ou qu'une faute soit commise.
        proba_blessure = rd.random()
        proba_faute = rd.random()
        if proba_blessure > 0.95:  # 5% de chance qu'un joueur se blesse
            # On choisit le joueur blessé au hasard dans l'équipe attaquante.
            ib = rd.randint(0, len(c1.equipe)-1)
            jb = c1.equipe[ib]
            # On change de joueur si ce n'est pas un attaquant ou un milieu.
            while jb.poste != "Attaquant" and jb.poste != "Milieu":
                ib = rd.randint(0, len(c1.equipe)-1)
                jb = c1.equipe[ib]
            jb.blessure(f)  # Détermination de la gravité de la blessure
            # On ajoute le joueur à la liste des blessés du match.
            if jb not in self.joueurs_blessures:
                self.joueurs_blessures.append(jb)
            seuil_faute = 0.7  # Si un joueur est blessé, 30% de chance qu'il y ait faute
        else:  # Si personne ne se blesse
            seuil_faute = 0.9  # Si aucun joueur n'est blessé, 10% de chance qu'il y ait faute

        if proba_faute > seuil_faute:
            # On choisit le joueur qui commet la faute au hasard dans l'équipe défenseuse.
            i_f = rd.randint(0, len(c2.equipe)-1)
            j_f = c2.equipe[i_f]
            # On change de joueur si ce n'est pas un défenseur.
            while j_f.poste != "Défenseur":
                i_f = rd.randint(0, len(c2.equipe)-1)
                j_f = c2.equipe[i_f]
            j_f.faute(f)
            # On ajoute le joueur à la liste de ceux ayant reçu un carton lors du match.
            if j_f not in self.joueurs_cartons:
                self.joueurs_cartons.append(j_f)
            # Si le joueur reçoit un carton rouge, il est exclu du match.
            if j_f.carton == 2:
                c2.equipe.remove(j_f)
            c2.nb_cartons += 1

        # On détermine l'issue de l'action.
        if puis_att > puis_def:
            print(f"=> {c1} perce la défense de {c2}")
            f.write(f"=> <b>{c1}</b> perce la défense de <b>{c2}</b><br>")
            c1.attaques_reussies += 1
            # On choisit un joueur au hasard pour effectuer le tir final.
            i = rd.randint(0, len(c1.equipe)-1)
            j = c1.equipe[i]
            gardien = c2[-1]  # On sélectionne le gardien de l'équipe en défense
            # Tant que le joueur sélectionné n'est pas un attaquant, on en sélectionne un autre.
            while j.poste != "Attaquant":
                i = rd.randint(0, len(c1.equipe)-1)
                j = c1.equipe[i]
            # On détermine les notes de frappes et d'arrêt en fonction des notes de l'attaquant et du gardien ainsi
            # que de la ferveur des supporters (domicile/extérieur).
            note_frappe = j.note * rd.random() + dom_c1 * 10
            note_arret = gardien.note * rd.random() + dom_c2 * 10
            j.nb_tirs += 1
            gardien.tentatives_arrets += 1
            # Affichage des notes (debug).
            print("note_frappe :", note_frappe)
            print("note_arret :", note_arret)
            # Enregistrement.
            f.write(f"<b>{j.prenom[0]}.{j.nom}</b> tir ! (Note de la frappe : "
                    f"<font color={c1.couleur}><b>{note_frappe:.1f}</b></font>)<br>")
            f.write(f"<b>{gardien.prenom[0]}.{gardien.nom}</b> plonge (Note de l'arrêt : "
                    f"<font color={c2.couleur}><b>{note_arret:.1f}</b></font>)<br>")

            # On détermine l'issue du tir.
            if note_frappe > note_arret:
                print(f"===> {j.prenom[0]}.{j.nom} marque un but pour {c1} à la {temps}ème minute !")
                print("- - - - - - - -")
                f.write(f"===> <b>{j.prenom[0]}.{j.nom} marque un but pour {c1} à la {temps}ème minute !</b><br>")
                f.write("<br>")
                j.but()
                return 1, j, temps  # S'il y a but, on renvoie le buteur et la minute du but
            else:
                print(f"===> {gardien.prenom[0]}.{gardien.nom} arrête le tir de {j.prenom[0]}.{j.nom}")
                print("- - - - - - - -")
                f.write(f"===> <b>{gardien.prenom[0]}.{gardien.nom} arrête le tir de {j.prenom[0]}.{j.nom}</b><br>")
                f.write("<br>")
                gardien.arret()
                return 0, gardien, temps  # S'il n'y a pas but, on renvoie le gardien et la minute de l'arrêt

        else:
            print(f"--> La défense de {c2} parvient à repousser l'offensive de {c1}")
            print("- - - - - - - -")
            f.write(f"===> <b>La défense de {c2} parvient à repousser l'offensive de {c1}</b><br>")
            f.write("<br>")
            c2.defenses_reussies += 1
            return 2, 0, 0

    def score_journee(self):
        """
        Méthode affichant le score de l'équipe sur une journée.
        """
        for c in self.clubs_complet:
            print(f"{c} termine la journée {self.num} avec un score de {c.score}")

    def deroulement(self):
        """
        Méthode simulant le déroulement d'une journée.
        """
        # Tant que tout les clubs n'ont pas joué.
        while len(self.clubs) > 0:
            self.match()  # Simulation d'un match
        self.score_journee()
        # Les joueurs récupèrent à chaque fin de journée.
        for c in self.clubs_complet:
            for j in c:
                if j.etat != 0:
                    j.recuperation()
                if j.carton != 0:
                    j.reinitialisation_cartons()

    def resume_match_log(self, c1, c2, liste_buteurs, liste_arrets, but_c1, but_c2):
        """
        Méthode permettant d'enregistrer le résumé d'un match dans un fichier texte.

        c1 : Le club qui joue à domicile.
        c2 : Le club qui joue à l'extérieur.
        liste_buteurs : Liste contenant tous les buteurs du match ainsi que la minute de leurs buts.
        liste_arrets : Liste contenant tous les arrêts du match ainsi que la minute de l'arrêt.
        but_c1 : Nombre de buts de c1.
        but_c2 : Nombre de buts de c2.
        """
        f = open(f"C:\WorkspacePython\LeFoot\Fichiers\\Journée {self.num}, match {c1.nom}-{c2.nom}.txt", 'wt') # titouan
        # f = open(f"C:\\Users\\hadrien dupuy\\PycharmProjects\\pythonProject6\\BDD\\Journée {self.num}, match {c1.nom}-{c2.nom}.txt", 'wt')
        # Affichage des buteurs.
        f.write("BUTEURS :\n")
        for i in range(len(liste_buteurs)):
            buteur = liste_buteurs[i][0]
            temps = liste_buteurs[i][1]
            f.write(f"  > {buteur.nom} ({temps}' - {buteur.club})\n")
        f.write("\n")
        # Affichage des arrêts.
        f.write("ARRETS :\n")
        for i in range(len(liste_arrets)):
            gardien = liste_arrets[i][0]
            temps = liste_arrets[i][1]
            f.write(f"  > {gardien.nom} ({temps}' - {gardien.club})\n")
        f.write("\n")
        # Affichage des cartons.
        for j in self.joueurs_cartons:
            if j.carton == 1:
                carton = "jaune"
            else:
                carton = "rouge"
            f.write(f"{j.nom} ({j.club}) à reçu un carton {carton}\n")
        f.write("\n")
        # Affichage des blessures.
        for j in self.joueurs_blessures:
            if j.etat == 1:
                blessure = "lègerement blessé"
            elif j.etat == 2:
                blessure = "blessé"
            else:
                blessure = "grièvement blessé"
            f.write(f"{j.nom} ({j.club}) s'est {blessure}\n")
        f.write("\n")
        # Affichage du score.
        f.write("SCORE :\n")
        f.write(f"   {c1.nom} - {c2.nom}\n")
        f.write(f"   {but_c1} - {but_c2}")
        f.close()
